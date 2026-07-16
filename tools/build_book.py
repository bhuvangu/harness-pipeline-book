#!/usr/bin/env python3
"""Build the two-document HTML site (User Guide + API & Entity Reference)
from guide/ and api-reference/ markdown. Output: a single self-contained
page with an AWS-docs-style collapsible tree sidebar and a doc switcher."""
import markdown, re, html, pathlib

ROOT = pathlib.Path('/home/user/harness-pipeline-book')
OUT = pathlib.Path('/tmp/claude-0/-home-user-harness-pipeline-book/'
                   'f4afcf7c-faa4-5453-95da-10110d650dd6/scratchpad/'
                   'harness-pipeline-book.html')

# (id, nav label, path, parent_id or None). Parents form the tree.
GUIDE = [
 ('home', 'What is the Harness pipeline offering?', 'guide/README.md', None),
 ('concepts', 'Pipeline concepts', 'guide/concepts/README.md', None),
 ('scopes', 'Scopes', 'guide/concepts/scopes.md', 'concepts'),
 ('identifiers', 'Identifiers and names', 'guide/concepts/identifiers.md', 'concepts'),
 ('structure', 'Pipeline structure', 'guide/concepts/pipeline-structure.md', 'concepts'),
 ('storage', 'YAML and Git storage', 'guide/concepts/yaml-and-storage.md', 'concepts'),
 ('apigen', 'The two API generations', 'guide/concepts/api-generations.md', 'concepts'),
 ('inputs', 'Configuring pipeline inputs', 'guide/inputs/README.md', None),
 ('runtime', 'Runtime inputs and expressions', 'guide/inputs/runtime-inputs.md', 'inputs'),
 ('inputsets', 'Input sets and overlays', 'guide/inputs/input-sets.md', 'inputs'),
 ('variables', 'Variables', 'guide/inputs/variables.md', 'inputs'),
 ('triggers', 'Starting pipelines with triggers', 'guide/triggers/README.md', None),
 ('webhook', 'Webhook triggers', 'guide/triggers/webhook-triggers.md', 'triggers'),
 ('cron', 'Scheduled triggers', 'guide/triggers/scheduled-triggers.md', 'triggers'),
 ('artifact', 'Artifact and manifest triggers', 'guide/triggers/artifact-triggers.md', 'triggers'),
 ('exec', 'Managing executions', 'guide/executions/README.md', None),
 ('statuses', 'Statuses and the execution graph', 'guide/executions/statuses-and-graph.md', 'exec'),
 ('failure', 'Failure handling', 'guide/executions/failure-handling.md', 'exec'),
 ('retry', 'Retrying and rerunning', 'guide/executions/retry-and-rerun.md', 'exec'),
 ('approvals', 'Approvals', 'guide/executions/approvals.md', 'exec'),
 ('ci', 'Building with CI stages', 'guide/ci/README.md', None),
 ('buildinfra', 'Choosing a build infrastructure', 'guide/ci/build-infrastructure.md', 'ci'),
 ('codebase', 'Configuring the codebase', 'guide/ci/codebase.md', 'ci'),
 ('cisteps', 'CI steps', 'guide/ci/ci-steps.md', 'ci'),
 ('ti', 'Test Intelligence', 'guide/ci/test-intelligence.md', 'ci'),
 ('cacheintel', 'Cache Intelligence', 'guide/ci/cache-intelligence.md', 'ci'),
 ('cd', 'Deploying with CD stages', 'guide/cd/README.md', None),
 ('services', 'Services', 'guide/cd/services.md', 'cd'),
 ('environments', 'Environments and infrastructure', 'guide/cd/environments.md', 'cd'),
 ('overrides', 'Service overrides', 'guide/cd/service-overrides.md', 'cd'),
 ('strategies', 'Strategies and rollback', 'guide/cd/strategies-and-rollback.md', 'cd'),
 ('freeze', 'Deployment freeze', 'guide/cd/deployment-freeze.md', 'cd'),
 ('connect', 'Connecting to your infrastructure', 'guide/connect/README.md', None),
 ('delegates', 'Delegates', 'guide/connect/delegates.md', 'connect'),
 ('connectors', 'Connectors', 'guide/connect/connectors.md', 'connect'),
 ('secrets', 'Secrets and secret managers', 'guide/connect/secrets.md', 'connect'),
 ('templates', 'Reusing configuration with templates', 'guide/reuse/templates.md', None),
 ('walk', 'Walkthroughs', 'guide/walkthroughs/README.md', None),
 ('buildlife', 'Life of a build', 'guide/walkthroughs/life-of-a-build.md', 'walk'),
 ('deploylife', 'Life of a deployment', 'guide/walkthroughs/life-of-a-deployment.md', 'walk'),
]
REF = [
 ('ref', 'API & Entity Reference', 'api-reference/README.md', None),
 ('entities', 'Entity reference', 'api-reference/entity-reference.md', None),
 ('relationships', 'Relationship diagrams', 'api-reference/relationships.md', None),
 ('glossary', 'Glossary', 'api-reference/glossary.md', None),
 ('openq', 'Known issues and open questions', 'api-reference/open-questions.md', None),
]

md = markdown.Markdown(extensions=['tables', 'fenced_code', 'sane_lists'])

def slug(t):
    return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

def render(pages, docname):
    sections, extra_children = [], {}
    for sid, label, fname, parent in pages:
        text = (ROOT / fname).read_text()
        text = re.sub(r'\[([^\]]+)\]\((?:\.\./)*[0-9a-zA-Z\-_/]+\.md(?:#[^)]*)?\)', r'\1', text)
        body = md.convert(text); md.reset()
        body = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>',
                      lambda m: '<pre class="mermaid">' + m.group(1) + '</pre>',
                      body, flags=re.S)
        if sid == 'entities':  # per-entity sub-navigation, AWS API-reference style
            kids = []
            def addid(m):
                t = re.sub(r'<[^>]+>', '', m.group(1))
                i = 'e-' + slug(t)
                kids.append((i, t))
                return f'<h2 id="{i}">{m.group(1)}</h2>'
            body = re.sub(r'<h2>(.*?)</h2>', addid, body)
            extra_children[sid] = kids
        sections.append((sid, label, body, parent))

    parents = {p[0] for p in pages if any(q[3] == p[0] for q in pages)} | set(extra_children)
    nav = []
    for sid, label, _, parent in sections:
        a = f'<a href="#{sid}">{html.escape(label)}</a>'
        if parent is None and sid in parents:
            kids = ''.join(
                f'<a class="child" href="#{k}">{html.escape(l)}</a>'
                for k, l, _b, p in sections if p == sid)
            kids += ''.join(
                f'<a class="child" href="#{k}">{html.escape(l)}</a>'
                for k, l in extra_children.get(sid, []))
            nav.append('<div class="tnode"><div class="trow">'
                       f'<button class="tw" aria-label="expand section"></button>{a}</div>'
                       f'<div class="tkids">{kids}</div></div>')
        elif parent is None:
            nav.append(f'<div class="tnode"><div class="trow leaf">{a}</div></div>')
    content = '\n'.join(f'<section id="{sid}">\n{b}\n</section>' for sid, _, b, _p in sections)
    return '\n'.join(nav), content

gnav, gcontent = render(GUIDE, 'guide')
rnav, rcontent = render(REF, 'ref')

CSS = """
:root{
  --accent:#0f6674; --accent-soft:#0f66741a;
  --ink:#22313a; --muted:#5b6e77; --ground:#fafbfb; --surface:#ffffff;
  --code-bg:#f0f4f5; --border:#dce4e6; --callout:#eef4f5;
  --serif:Charter,"Bitstream Charter","Iowan Old Style",Georgia,serif;
  --sans:system-ui,"Segoe UI","Helvetica Neue",Arial,sans-serif;
  --mono:ui-monospace,"SF Mono","Cascadia Code",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){:root{
  --accent:#4fb3c4; --accent-soft:#4fb3c426;
  --ink:#d9e2e6; --muted:#8fa3ac; --ground:#131a1e; --surface:#1a2429;
  --code-bg:#1e2a30; --border:#2a363d; --callout:#18262c;
}}
:root[data-theme="dark"]{
  --accent:#4fb3c4; --accent-soft:#4fb3c426;
  --ink:#d9e2e6; --muted:#8fa3ac; --ground:#131a1e; --surface:#1a2429;
  --code-bg:#1e2a30; --border:#2a363d; --callout:#18262c;
}
:root[data-theme="light"]{
  --accent:#0f6674; --accent-soft:#0f66741a;
  --ink:#22313a; --muted:#5b6e77; --ground:#fafbfb; --surface:#ffffff;
  --code-bg:#f0f4f5; --border:#dce4e6; --callout:#eef4f5;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font-family:var(--serif);font-size:17px;line-height:1.65}
.topbar{display:flex;align-items:center;gap:1.5rem;padding:.7rem 1.5rem;
  border-bottom:1px solid var(--border);background:var(--surface);
  font-family:var(--sans);position:sticky;top:0;z-index:5}
.topbar .brand{font-weight:700;font-size:1rem;letter-spacing:-.01em}
.topbar .brand small{display:block;font-weight:400;color:var(--muted);
  font-size:.7rem;text-transform:uppercase;letter-spacing:.09em}
.doctabs{display:flex;gap:.25rem;margin-left:auto}
.doctabs button{font-family:var(--sans);font-size:.83rem;padding:.42rem .9rem;
  border:1px solid var(--border);background:none;color:var(--muted);
  border-radius:6px;cursor:pointer}
.doctabs button.active{background:var(--accent);border-color:var(--accent);color:#fff}
.doctabs button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.layout{display:flex;min-height:calc(100vh - 53px)}
nav.sidebar{width:290px;flex:0 0 290px;position:sticky;top:53px;
  height:calc(100vh - 53px);overflow-y:auto;border-right:1px solid var(--border);
  background:var(--surface);padding:1rem 0 3rem;font-family:var(--sans)}
.tnode{margin:0}
.trow{display:flex;align-items:center}
.trow.leaf{padding-left:1.55rem}
.tw{flex:0 0 1.55rem;height:1.9rem;border:none;background:none;cursor:pointer;
  color:var(--muted);position:relative}
.tw::before{content:"";position:absolute;left:.62rem;top:.72rem;
  border-left:5px solid currentColor;border-top:4px solid transparent;
  border-bottom:4px solid transparent;transition:transform .12s}
@media (prefers-reduced-motion: reduce){.tw::before{transition:none}}
.tnode.open>.trow .tw::before{transform:rotate(90deg)}
nav.sidebar a{display:block;flex:1;padding:.34rem .9rem .34rem 0;
  color:var(--ink);text-decoration:none;font-size:.86rem;line-height:1.35}
nav.sidebar a.child{padding-left:2.3rem;color:var(--muted);font-size:.83rem}
nav.sidebar a:hover{color:var(--accent)}
nav.sidebar a.active{color:var(--accent);font-weight:600}
nav.sidebar a:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
.tkids{display:none}
.tnode.open>.tkids{display:block}
main{flex:1;min-width:0;padding:2.5rem 3rem 6rem}
section{max-width:72ch;margin:0 auto 4rem;scroll-margin-top:70px}
section+section{border-top:1px solid var(--border);padding-top:3rem}
h1,h2,h3,h4{font-family:var(--sans);line-height:1.25;text-wrap:balance;color:var(--ink)}
h1{font-size:1.9rem;font-weight:650;letter-spacing:-.015em;margin:0 0 1rem}
h2{font-size:1.35rem;font-weight:650;margin:2.4rem 0 .8rem;scroll-margin-top:70px}
h3{font-size:1.08rem;font-weight:650;margin:1.9rem 0 .6rem}
p{margin:.75rem 0}
a{color:var(--accent)}
strong{font-weight:650}
code{font-family:var(--mono);font-size:.82em;background:var(--code-bg);
  padding:.1em .35em;border-radius:3px}
pre{background:var(--code-bg);border:1px solid var(--border);border-radius:6px;
  padding:.9rem 1.1rem;overflow-x:auto;line-height:1.5;margin:1rem 0}
pre code{background:none;padding:0;font-size:.8rem}
pre.mermaid{background:var(--surface);text-align:center}
blockquote{margin:1.5rem 0;padding:.9rem 1.2rem;background:var(--callout);
  border-left:3px solid var(--accent);border-radius:0 6px 6px 0}
blockquote p{margin:.5rem 0}
table{border-collapse:collapse;font-size:.85rem;font-family:var(--sans);
  display:block;overflow-x:auto;margin:1.1rem 0;font-variant-numeric:tabular-nums}
th,td{border:1px solid var(--border);padding:.45rem .7rem;text-align:left;vertical-align:top}
th{background:var(--code-bg);font-weight:650;white-space:nowrap}
li{margin:.3rem 0}
hr{border:none;border-top:1px solid var(--border);margin:2rem 0}
body[data-doc="guide"] .doc-ref{display:none}
body[data-doc="ref"] .doc-guide{display:none}
@media (max-width:900px){
  .layout{display:block}
  nav.sidebar{position:static;width:auto;height:auto;max-height:45vh;
    border-right:none;border-bottom:1px solid var(--border)}
  main{padding:1.5rem 1.2rem 4rem}
}
@media print{.topbar,nav.sidebar{display:none}main{padding:0}
  body[data-doc="guide"] .doc-ref,body[data-doc="ref"] .doc-guide{display:block}}
@media (prefers-reduced-motion: no-preference){html{scroll-behavior:smooth}}
"""

JS = """
(function(){
  var body=document.body;
  var docOf={};
  document.querySelectorAll('.doc-guide section,.doc-guide h2[id]').forEach(function(e){
    if(e.id)docOf[e.id]='guide';});
  document.querySelectorAll('.doc-ref section,.doc-ref h2[id]').forEach(function(e){
    if(e.id)docOf[e.id]='ref';});
  function setDoc(d){
    body.setAttribute('data-doc',d);
    document.querySelectorAll('.doctabs button').forEach(function(b){
      b.classList.toggle('active',b.dataset.doc===d);
    });
    document.querySelectorAll('nav.sidebar > .docnav').forEach(function(n){
      n.style.display=(n.dataset.doc===d)?'':'none';
    });
  }
  document.querySelectorAll('.doctabs button').forEach(function(b){
    b.addEventListener('click',function(){setDoc(b.dataset.doc);window.scrollTo(0,0);});
  });
  document.querySelectorAll('.tw').forEach(function(t){
    t.addEventListener('click',function(){t.closest('.tnode').classList.toggle('open');});
  });
  function activate(){
    var id=location.hash.replace('#','');
    if(id&&docOf[id]) setDoc(docOf[id]);
    document.querySelectorAll('nav.sidebar a').forEach(function(a){
      var on=a.getAttribute('href')==='#'+id;
      a.classList.toggle('active',on);
      if(on){var n=a.closest('.tnode');if(n)n.classList.add('open');}
    });
  }
  window.addEventListener('hashchange',activate);
  setDoc('guide');
  activate();
})();
"""

page = f"""<title>Harness Pipelines Documentation</title>
<style>{CSS}</style>
<header class="topbar">
  <div class="brand">Harness Pipelines<small>Documentation</small></div>
  <div class="doctabs">
    <button data-doc="guide" class="active">User Guide</button>
    <button data-doc="ref">API &amp; Entity Reference</button>
  </div>
</header>
<div class="layout">
<nav class="sidebar" aria-label="Contents">
  <div class="docnav" data-doc="guide">{gnav}</div>
  <div class="docnav" data-doc="ref" style="display:none">{rnav}</div>
</nav>
<main>
<div class="doc-guide">
{gcontent}
</div>
<div class="doc-ref">
{rcontent}
</div>
</main>
</div>
<script>{JS}</script>
"""
OUT.write_text(page)
print(OUT, len(page))

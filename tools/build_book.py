import markdown, re, html, pathlib

BOOK = pathlib.Path('/home/user/harness-pipeline-book/book')
OUT  = pathlib.Path('/tmp/claude-0/-home-user-harness-pipeline-book/f4afcf7c-faa4-5453-95da-10110d650dd6/scratchpad/harness-pipeline-book.html')

files = [
 ('intro','Start here','README.md'),
 ('ch01','1 · The resource model','01-resource-model.md'),
 ('ch02','2 · The pipeline aggregate','02-pipeline-aggregate.md'),
 ('ch03','3 · Parameterization','03-parameterization.md'),
 ('ch04','4 · Triggers and events','04-triggers-and-events.md'),
 ('ch05','5 · Execution','05-execution.md'),
 ('ch06','6 · CI stages','06-ci-stages.md'),
 ('ch07','7 · CD stages','07-cd-stages.md'),
 ('ch08','8 · The connectivity layer','08-connectivity-layer.md'),
 ('ch09','9 · Reuse','09-reuse.md'),
 ('ch10','10 · Life of a build & deployment','10-life-of-a-pipeline.md'),
 ('appa','A · Entity reference','appendix-a-entity-reference.md'),
 ('appb','B · Relationship diagrams','appendix-b-relationships.md'),
 ('appc','C · Glossary','appendix-c-glossary.md'),
 ('appd','D · Open questions','appendix-d-open-questions.md'),
]

md = markdown.Markdown(extensions=['tables','fenced_code','sane_lists'])

sections = []
for sid, label, fname in files:
    text = (BOOK/fname).read_text()
    # strip links to local md files in README table -> plain text
    text = re.sub(r'\[([^\]]+)\]\((?:[0-9a-z\-]+\.md)\)', r'\1', text)
    body = md.convert(text); md.reset()
    # mermaid fences -> native artifact mermaid blocks
    body = re.sub(
        r'<pre><code class="language-mermaid">(.*?)</code></pre>',
        lambda m: '<pre class="mermaid">' + m.group(1) + '</pre>',
        body, flags=re.S)
    sections.append((sid, label, body))

navparts = []
for sid, label, _ in sections:
    cls = ' class="nav-app"' if sid.startswith('app') else ''
    if sid == 'appa':
        navparts.append('<div class="nav-label">Appendices</div>')
    navparts.append('<a href="#%s"%s>%s</a>' % (sid, cls, html.escape(label)))
nav = '\n'.join(navparts)

content = '\n'.join(f'<section id="{sid}">\n{body}\n</section>' for sid, _, body in sections)

css = """
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
.layout{display:flex;min-height:100vh}
nav.sidebar{width:250px;flex:0 0 250px;position:sticky;top:0;height:100vh;
  overflow-y:auto;border-right:1px solid var(--border);background:var(--surface);
  padding:1.5rem 0 3rem;font-family:var(--sans)}
nav.sidebar .brand{padding:0 1.25rem 1rem;border-bottom:1px solid var(--border);margin-bottom:.75rem}
nav.sidebar .brand strong{font-size:.95rem;letter-spacing:.01em;display:block}
nav.sidebar .brand span{font-size:.72rem;color:var(--muted);text-transform:uppercase;letter-spacing:.09em}
nav.sidebar a{display:block;padding:.34rem 1.25rem;color:var(--muted);
  text-decoration:none;font-size:.85rem;line-height:1.35;border-left:3px solid transparent}
nav.sidebar a:hover{color:var(--accent);background:var(--accent-soft)}
nav.sidebar a:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
nav.sidebar a.nav-app{font-size:.8rem}
nav.sidebar .nav-label{padding:.9rem 1.25rem .25rem;font-size:.68rem;color:var(--muted);
  text-transform:uppercase;letter-spacing:.1em}
main{flex:1;min-width:0;padding:2.5rem 3rem 6rem}
section{max-width:72ch;margin:0 auto 4rem;scroll-margin-top:1.5rem}
section+section{border-top:1px solid var(--border);padding-top:3rem}
h1,h2,h3,h4{font-family:var(--sans);line-height:1.25;text-wrap:balance;color:var(--ink)}
h1{font-size:1.9rem;font-weight:650;letter-spacing:-.015em;margin:0 0 1rem}
h2{font-size:1.35rem;font-weight:650;margin:2.4rem 0 .8rem}
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
blockquote h3{margin-top:.2rem;color:var(--accent)}
blockquote p{margin:.5rem 0}
.table-wrap,table{max-width:100%}
table{border-collapse:collapse;font-size:.85rem;font-family:var(--sans);
  display:block;overflow-x:auto;margin:1.1rem 0;font-variant-numeric:tabular-nums}
th,td{border:1px solid var(--border);padding:.45rem .7rem;text-align:left;vertical-align:top}
th{background:var(--code-bg);font-weight:650;white-space:nowrap}
li{margin:.3rem 0}
hr{border:none;border-top:1px solid var(--border);margin:2.5rem 0}
img{max-width:100%}
@media (max-width:900px){
  .layout{display:block}
  nav.sidebar{position:static;width:auto;height:auto;border-right:none;
    border-bottom:1px solid var(--border)}
  main{padding:1.5rem 1.2rem 4rem}
}
@media (prefers-reduced-motion: no-preference){html{scroll-behavior:smooth}}
"""

page = f"""<title>The Harness Pipeline Book</title>
<style>{css}</style>
<div class="layout">
<nav class="sidebar" aria-label="Chapters">
  <div class="brand"><span>Domain model · CI/CD</span><strong>The Harness Pipeline Book</strong></div>
  {nav}
</nav>
<main>
{content}
</main>
</div>
"""
# fix nav grouping wrapper (we injected a closing div without opener; simpler: remove that hack)
OUT.write_text(page)
print(OUT, len(page))

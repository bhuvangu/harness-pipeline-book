# Secrets and secret managers

Secrets hold sensitive values — text, files, or SSH credentials — encrypted
at rest and referenced from YAML by expression:

```yaml
envVariables:
  SECRET: <+secrets.getValue("secretfile")>
```

Secrets exist at account, organization, or project scope, and log output is
sanitized so secret values don't appear in logs.

> **Note**
> Anyone with permission to run a pipeline can pass expressions through its
> runtime inputs, which can expose secret values. The documentation
> recommends OPA policies that block `<+secrets.getValue` in runtime input.

## Secret managers

A secret manager is the backend where secrets actually live. The built-in
default is Harness Secret Manager Google KMS. You can instead use AWS KMS,
HashiCorp Vault, Azure Key Vault, GCP Secrets Manager, AWS Secrets Manager,
or a custom secret manager.

The two architectures differ in what leaves your systems:

| | KMS type (Google KMS, AWS KMS) | Vault type (Vault, AKV, ASM, GCP SM) |
|---|---|---|
| The backend stores | Only the encryption key | Keys and secret values |
| Harness stores | The encrypted secret and encrypted data key (envelope encryption) | Only a reference |

## Where decryption happens

Harness Manager does not have access to your key management system. Only the
delegate, which runs in your private network, has access to it. The delegate
exchanges keys with the secret manager over an encrypted connection, uses
them, and discards them — the keys never leave the delegate. This is the
core security property of the design: the SaaS plane never holds your keys.

Consequences to plan for:

- Any secret manager requires a running delegate with direct access to it.
- KMS key rotation is not supported; removing old key versions loses access
  to the secrets they encrypted.
- Secrets are cached (encrypted) for 30 minutes, except with HashiCorp
  Vault.
- With Git Experience, the "Connect Through Manager" mode has Harness
  Manager decrypt Git-sync secrets; "Connect Through Delegate" keeps
  decryption in your network.

---
**Sources:** docs/platform/secrets/secrets-management/harness-secret-manager-overview.md
(all secret-manager behavior, quoted claims);
docs/platform/secrets/add-use-text-secrets.md;
yaml_examples/platform__secrets__add-use-text-secrets.md.yaml;
docs/platform/secrets/secrets-management/secrets-and-log-sanitization.md;
docs/platform/variables-and-expressions/runtime-inputs.md (OPA
recommendation); corpus/entity_schemas.md (Secret identity pattern).

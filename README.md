# Re8ch

Re8ch connects supported AI clients to the tools authorized for the signed-in
RE8CH organization. The plugin provides tenant-scoped infrastructure,
application, service, monitoring and workflow operations through an OAuth
protected remote MCP server.

The public package contains configuration and usage guidance only. Credentials,
access tokens, Kubernetes configuration and administrator policy remain on the
RE8CH service.

## Supported clients

- Cursor: install the Agent Plugin from this repository.
- Gemini CLI: install with
  `gemini extensions install https://github.com/8iops/re8ch-plugin`.
- Other MCP clients: connect to
  `https://tools.service.re8ch.com/tenant/mcp` and complete OAuth sign-in.

## Authentication and authorization

The MCP server resolves the active organization from the authenticated session.
It does not accept a tenant name from prompt text as an authorization decision.
Available tools and write permissions depend on the current organization's
grants and live platform capabilities.

## Safety

Inspect current state before a write, use plan-before-write operations when they
are available, and retain returned operation references. Never place tokens,
passwords, kubeconfigs, private keys or secret values in prompts or repository
files.

## Support

Contact `business@re8ch.com` for marketplace and connection support. Security
reports should not include credentials, tokens or private customer data.

## License

Package metadata and documentation are licensed under the MIT License. Access
to the hosted RE8CH service is governed separately by its applicable terms.

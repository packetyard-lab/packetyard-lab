# Security

Packetyard is a static, single-file web app. There is no server, no login, no database and no analytics. Everything runs in your browser.

## What the app does to stay safe

- **Nothing leaves your browser.** The page never calls a server; simulated "Internet" traffic is only animation. The Content-Security-Policy sets `connect-src 'none'`, so the page can't make network requests even if a bug tried to.
- **Strict Content-Security-Policy** in the GitHub Pages build (`index.html`):
  - only the app's own script may run, pinned by its SHA-256 hash, so injected `<script>` tags or inline handlers such as `onerror=` are blocked;
  - no plugins (`object-src 'none'`), no frames, no workers, no form submissions, and `base-uri 'none'`;
  - fonts only from Google Fonts. Without them, the page falls back to system fonts.
- **No referrer leaks:** `<meta name="referrer" content="no-referrer">`.
- **Untrusted project files are sanitized.** A `.pkyard` / `.json` file someone sends you, pasted project text, and browser autosave all go through the same checks before loading:
  - size limit 8 MB, maximum 400 devices and 2000 cables;
  - device names are limited to letters, digits, `-`, `_` and `.`;
  - `<`, `>`, quotes and backticks are replaced in every text field;
  - `__proto__`, `constructor` and `prototype` keys are dropped (prototype pollution);
  - cables that point at missing devices or ports are removed;
  - malformed device settings fall back to safe defaults instead of crashing.
- **Host names typed in the console** (`hostname`, the name field) are restricted the same way.
- **Your work stays local.** Saved projects use the browser's `localStorage` on your own device. Clearing site data removes them; download a `.pkyard` file to keep a copy.

## Recommended GitHub settings

1. **Settings → Pages:** tick **Enforce HTTPS**.
2. **Settings → Branches:** add a branch protection rule for `main` (require a pull request before merging) if others can push.
3. Turn on **two-factor authentication** for your GitHub account.
4. Only add collaborators you trust; anyone with write access can change the published site.

## Editing the code

The Content-Security-Policy allows exactly one script: the current one, identified by its SHA-256 hash. If you change anything inside `<script>…</script>` in `index.html`, run:

```bash
python3 update-csp.py
```

It recomputes the hash and updates the policy. Without that step the browser blocks the edited script and the page stays empty.

## Reporting a problem

If you find a security issue, open a GitHub issue **without** exploit details and ask for a private contact, or use GitHub's **Report a vulnerability** button under the repository's Security tab if it's enabled.

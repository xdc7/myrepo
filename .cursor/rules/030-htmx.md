### HTMX rules
- Use HTMX for progressive enhancement; avoid SPA complexity.
- Detect HTMX with `request.headers.get("HX-Request") == "true"`.
- Return partial templates for HTMX requests; full templates otherwise.
- Place partials under `templates/<app>/partials/`.
- Use `hx-get`/`hx-post` on triggers; set `hx-target` and `hx-swap` appropriately.
- Always include `{% csrf_token %}` in forms; CSRF cookie is sent automatically.
- Keep responses small; do not render the whole page for HTMX calls.

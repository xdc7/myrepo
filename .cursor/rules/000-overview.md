### Purpose
- **Keep it Python-first and junior-friendly.** Use Django for backend and server-rendered frontend; add HTMX for small, incremental interactivity. Avoid SPAs unless required.
- **Simplicity over cleverness.** Prefer standard Django features before adding new libraries.

### Stack
- **Language**: Python 3.11+
- **Framework**: Django (prefer LTS when available)
- **Frontend**: Django Templates + HTMX; minimal vanilla JS only when needed
- **DB**: SQLite (dev), PostgreSQL (prod)
- **Static (prod)**: WhiteNoise
- **Server**: Gunicorn behind a simple reverse proxy (or a PaaS)

### High-level rules
- **Prefer server-rendered pages.** Use HTMX for partial updates and forms.
- **Keep views thin; move logic to services.** Put domain logic in `services.py`.
- **Type hints where they help.** Especially in services and complex views.
- **Add tests with each feature.** Forms and views at minimum.
- **Secure by default for prod.** `DEBUG=False`, `ALLOWED_HOSTS`, secure cookies, HTTPS.
- **Document small.** Update `README.md` and keep comments brief but useful.

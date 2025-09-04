### Settings
- Split settings: `project/settings/base.py`, `dev.py`, `prod.py`.
- Use `django-environ`; read `.env` for `SECRET_KEY`, DB URL, `DEBUG`.
- **base.py**: `INSTALLED_APPS`, `MIDDLEWARE`, templates, internationalization, static setup.
- **dev.py**: `DEBUG=True`, SQLite, console email, `ALLOWED_HOSTS=["*"]`.
- **prod.py**: `DEBUG=False`, Postgres, WhiteNoise, secure cookies, `SECURE_*` headers, logging.
- Static: configure `STATIC_URL`, `STATIC_ROOT`; run `collectstatic` in prod.
- Media (if needed): `MEDIA_URL`, `MEDIA_ROOT`; prefer cloud storage for user uploads in prod.

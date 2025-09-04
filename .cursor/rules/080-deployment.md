### Deployment
- Gunicorn app: `gunicorn project.wsgi:application --bind 0.0.0.0:8000`.
- Use WhiteNoise for static in prod; set `STATIC_ROOT` and run `collectstatic`.
- Reverse proxy (e.g., Nginx) or PaaS. Enforce HTTPS; set security headers.
- Environment: configure `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, DB, cache.
- Optional container: `python:3.12-slim`, non-root user, `gunicorn` entrypoint.

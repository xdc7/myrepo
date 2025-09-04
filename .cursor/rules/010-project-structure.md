### Project structure
- **Root**: `manage.py`, `requirements.txt`, `.env`, `.gitignore`, `README.md`
- **Project config**: `project/` with `settings/` split: `base.py`, `dev.py`, `prod.py`; `urls.py`, `wsgi.py`.
- **App**: Start with a single app `core/`: `models.py`, `views.py`, `urls.py`, `forms.py`, `admin.py`, `services.py`, `templates/core/`, `templates/core/partials/`, `static/core/`.
- **Templates**: Include `templates/base.html` and `templates/partials/` for shared layout.

### Rules
- Keep one app (`core`) until clear domain boundaries emerge.
- Put non-trivial domain logic in `services.py` with pure functions/classes.
- Views stay thin; forms handle validation; templates handle presentation.
- Register models in `admin.py` for early visibility.

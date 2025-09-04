# Ideas Portal (Phase 0)

## Setup

- Python 3.11+
- Create venv and install deps:
  - `python3 -m venv .venv && source .venv/bin/activate`
  - `pip install -r requirements.txt`
- Environment:
  - Copy `.env.example` to `.env`

## Commands

- Run dev server: `python manage.py runserver`
- Migrate DB: `python manage.py migrate`
- Lint: `ruff check .`
- Format: `black .`
- Tests: `pytest`

## Endpoints

- Health (HTML): `/health/`
- Health (JSON): `/api/health/`
- API Schema: `/api/schema/`
- Swagger UI: `/api/docs/`
- Redoc: `/api/redoc/`

## Notes

- Settings split under `project/settings/` using `django-environ`
- WhiteNoise configured; `collectstatic` ready
- HTMX included in `templates/base.html`
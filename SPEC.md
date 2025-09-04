### App Spec: Ideas Portal (Django + HTMX + DRF)

#### Overview and goals
- **Goal**: A simple web app where users sign up, log in, submit ideas, and view ideas approved by admins. Admins manage users and approve/reject ideas. JSON APIs exist for each action. Everything is test-driven with clear documentation.
- **Architecture**: Simple n‑tier
  - **Presentation**: Django Templates + HTMX, minimal vanilla JS; DRF schema docs.
  - **Application**: Django views for pages; DRF APIViews for JSON APIs; orchestration in services.
  - **Domain**: Django ORM models and business rules.
  - **Data**: SQLite (dev), Postgres (prod).
- **Key constraints**: Junior-friendly, conventional Django; minimal deps; secure defaults in prod.

#### Stack
- Python 3.11+, Django (latest stable/LTS), Django REST Framework, drf-spectacular, django-environ, WhiteNoise, HTMX (via CDN include), Black/Ruff/isort, pytest + pytest-django (optional) or Django test runner.

#### Core domain
- `Idea`
  - Fields: `title` (str, ≤200), `description` (text), `status` (choices: PENDING, APPROVED, REJECTED), `created_by` (FK User), `created_at`, `updated_at`.
  - Constraints: non-empty title/description; default status PENDING.
  - Indexes: `status`, `created_at`.
- Permissions
  - Anonymous: signup, login only.
  - Authenticated: create idea; list approved ideas; view/track their own ideas in “My Ideas”.
  - Admin (staff): approve/reject ideas; manage users; access admin site; access admin APIs.

---

## Phases

### Phase 0 — Project bootstrap and tooling
- Goals: Create project, basic settings split, quality tooling, CI placeholder, baseline docs.
- Scope
  - Create Django project `project/` and apps `accounts/`, `ideas/`.
  - Settings split: `project/settings/{base.py,dev.py,prod.py}` using `django-environ`.
  - Add DRF and drf-spectacular; add HTMX include partial for templates.
  - Add WhiteNoise; static config; `collectstatic` ready.
  - Tooling: Black, Ruff, isort, pre-commit; tests scaffold.
  - Healthcheck view `/health/` (HTML) and `/api/health/` (JSON).
- Deliverables
  - Running server, health endpoints, lint/format commands, README setup.
- Tests
  - Health endpoints 200; settings load in dev; simple template render.
- DoD
  - `runserver` works; `ruff check` and `black --check` pass; tests pass.

### Phase 1 — Accounts: signup/login/logout (pages + APIs)
- Goals: Users can create accounts, log in/out via pages and JSON APIs.
- Scope
  - Forms: `SignupForm` (username, email optional, password1/2 validation).
  - Views (pages): `/signup`, `/login`, `/logout` with CSRF, redirects.
  - APIs: `POST /api/auth/signup/`, `POST /api/auth/login/`, `POST /api/auth/logout/` (session auth).
  - Templates: `accounts/signup.html`, `accounts/login.html`; base layout and messages.
- Deliverables
  - Working auth flows; DRF endpoints; docstrings.
- Tests
  - Form validation (dupes, weak passwords), page GET/POST flows, API success/error paths, session behavior, CSRF.
- DoD
  - Users can sign up and log in via UI and API; coverage for success/failure.

### Phase 2 — Ideas domain model, services, and admin
- Goals: Implement `Idea` model with services and admin actions.
- Scope
  - Model `Idea` with fields and choices; migrations.
  - Admin registration: list, filters (status, user), search (title), actions (approve, reject).
  - Services `ideas/services.py`: `submit_idea(user, title, description)`, `approve_idea(idea, admin_user)`, `reject_idea(idea, admin_user)` with permission checks and state transitions.
- Deliverables
  - Admin can approve/reject; services enforce rules; migrations committed.
- Tests
  - Model constraints, `__str__`, ordering; services behavior (permissions, idempotency, transitions); admin actions restricted to staff.
- DoD
  - Admin approve/reject functions via admin; green tests on services and model.

### Phase 3 — Ideas pages (server-rendered + HTMX)
- Goals: Basic UX with minimal JS using HTMX.
- Scope
  - Routes: `/ideas/` (approved only), `/ideas/new` (submit), `/ideas/mine/` (user’s ideas all statuses).
  - Templates: `ideas/list.html` (full), `ideas/partials/idea_list.html` (partial), `ideas/form.html`, `ideas/mine.html`.
  - Views: class-based for lists; function/class for create; HTMX partials when `HX-Request` present.
- Deliverables
  - Users can submit via form (creates PENDING); list shows only APPROVED; “My Ideas” shows own ideas.
- Tests
  - Views: access control; list content correctness; HTMX partial response returns only the fragment; create redirects or returns partial.
- DoD
  - Pages functional with HTMX enhancements; tests cover primary flows.

### Phase 4 — Ideas user APIs (JSON)
- Goals: Provide API parity for user actions.
- Scope
  - Endpoints
    - `GET /api/ideas/` → approved only (paginated)
    - `POST /api/ideas/` → create PENDING
    - `GET /api/ideas/mine/` → user’s ideas (all statuses)
  - DRF: APIViews or ViewSets; serializers in `ideas/serializers.py`; permissions in `ideas/permissions.py`.
- Deliverables
  - Authenticated JSON APIs matching page behaviors.
- Tests
  - Endpoint auth, serialization, filtering by status/owner, validation errors.
- DoD
  - APIs return correct data and statuses; schema includes endpoints.

### Phase 5 — Admin APIs and permission hardening
- Goals: Admin can approve/reject over JSON; ensure strict access control.
- Scope
  - Endpoints (admin only)
    - `POST /api/ideas/{id}/approve/`
    - `POST /api/ideas/{id}/reject/`
    - `PATCH /api/admin/users/{id}/` (activate/deactivate minimal)
  - Permissions: custom DRF permission `IsStaff` as needed; ensure non-staff blocked.
- Deliverables
  - Admin JSON controls; permission coverage; structured error responses.
- Tests
  - 403 for non-staff; 200 for staff; state changes reflected in queries.
- DoD
  - Admin flows pass; no privilege escalation paths.

### Phase 6 — Documentation and schema
- Goals: Clear, accessible documentation for devs and API consumers.
- Scope
  - DRF schema with drf-spectacular at `/api/schema/`; Swagger UI `/api/docs/` and Redoc `/api/redoc/`.
  - README updates: setup, commands, environment, architecture, API curl examples, HTMX notes.
  - Optional: export `openapi.json` to repo for reference.
- Deliverables
  - Interactive API docs; comprehensive README.
- Tests
  - Schema endpoint 200; spot-check for key routes appearing.
- DoD
  - Docs accurate and reflect current API; lint passes.

### Phase 7 — Production hardening and deploy (optional)
- Goals: Make the app production-friendly.
- Scope
  - WhiteNoise for static; `prod.py` security (`DEBUG=False`, `ALLOWED_HOSTS`, `CSRF_TRUSTED_ORIGINS`, secure cookies, HSTS), logging config.
  - Gunicorn command; simple container file (optional); healthcheck.
- Deliverables
  - Run behind reverse proxy or PaaS; `collectstatic` works.
- Tests
  - Smoke test with prod settings; static served; minimal e2e run in CI if containerized.
- DoD
  - App runs with secure defaults; operational notes in README.

---

## API reference (initial)
- Auth
  - `POST /api/auth/signup/` → 201; {username,email} + passwords; returns user summary
  - `POST /api/auth/login/` → 200; {username,password}; sets session cookie
  - `POST /api/auth/logout/` → 204
- Ideas (user)
  - `GET /api/ideas/` → 200; approved ideas; query `?page=`; fields id,title,description,created_by,created_at
  - `POST /api/ideas/` → 201; {title,description}; status=PENDING
  - `GET /api/ideas/mine/` → 200; user’s ideas (all statuses)
- Ideas (admin)
  - `POST /api/ideas/{id}/approve/` → 200
  - `POST /api/ideas/{id}/reject/` → 200
- Users (admin)
  - `PATCH /api/admin/users/{id}/` → 200; {is_active}

## Page map
- `/signup`, `/login`, `/logout`
- `/ideas/` (approved list)
- `/ideas/new` (submit idea form)
- `/ideas/mine/` (my ideas)
- `/admin/` (Django admin)

## Testing strategy
- Test levels: unit (forms, services), integration (views, serializers), API (end-to-end), permissions.
- Tools: Django test runner or pytest + pytest-django; factory patterns optional.
- Coverage: aim ≥85% lines for `accounts` and `ideas`.
- Continuous checks: lint, format, tests on push.

## Directory structure (target)
- `project/` → settings (`base.py`, `dev.py`, `prod.py`), `urls.py`, `wsgi.py`
- `accounts/` → `forms.py`, `views.py`, `urls.py`, `api.py`, `serializers.py`, `services.py`, `templates/accounts/`, `tests/`
- `ideas/` → `models.py`, `views.py`, `urls.py`, `api.py`, `serializers.py`, `permissions.py`, `services.py`, `admin.py`, `templates/ideas/` (+ `partials/`), `tests/`
- `templates/base.html`, `templates/partials/_messages.html`
- `static/` (per-app static under their own dirs)

## Non-functional requirements
- Security: CSRF, session auth, secure cookies in prod; staff-only admin APIs.
- Performance: Paginate list endpoints; simple N+1 avoidance via `select_related`.
- Observability: Basic logging; request ID optional.
- Internationalization: Ready but English-only by default.

## Implementation notes
- Prefer CBVs for CRUD; function views acceptable for HTMX fragments.
- Detect HTMX via `HX-Request` header and return partials accordingly.
- Keep views thin; put domain logic in services with type hints.
- Use Django messages for UX feedback on forms.

## Definition of Done (global)
- All phases: tests green, lint/format pass, docs updated, migrations committed, admin registered where needed.

### Conventions
- **Views**: Prefer class-based (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`). Use function views for tiny endpoints and HTMX partials.
- **Forms**: Define in `forms.py`; perform validation there; keep views thin.
- **Services**: Place domain logic in `services.py`. Functions should be pure where possible and typed.
- **URLs**: Route in app `urls.py`; project `urls.py` only includes app routers.
- **Templates**: Use inheritance from `base.html`. Keep logic minimal; use template tags/filters when necessary.
- **Admin**: Register models early for debugging/ops; use `list_display`, `search_fields`.
- **Typing**: Add type hints in services and complex views; avoid `Any`.

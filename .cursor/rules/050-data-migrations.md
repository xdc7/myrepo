### Data and migrations
- Commit all migrations; keep them in each app’s `migrations/`.
- Create atomic, focused migrations; avoid editing old migrations once merged.
- Use constraints (`UniqueConstraint`, `CheckConstraint`) in models where appropriate.
- Provide optional fixtures under `fixtures/` or a custom `manage.py` command for seeding.
- Avoid raw SQL unless required; prefer ORM.

### HTMX view pattern
- In a view, render a full template normally; render a partial when `HX-Request` is true.
- Example decision:
  - `is_htmx = request.headers.get("HX-Request") == "true"`
  - `template = "core/partials/item_list.html" if is_htmx else "core/items.html"`

### HTMX template tips
- Wrap replaceable sections in elements with stable IDs/classes.
- Choose `hx-swap` intentionally (`outerHTML`, `innerHTML`, `beforeend`, etc.).
- Use `hx-push-url` only when the partial represents a navigable state.

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.template.loader import render_to_string


def html_health(request: HttpRequest) -> HttpResponse:
    html = render_to_string("base.html", {"title": "OK"}, request=request)
    return HttpResponse(html)


def api_health(request: HttpRequest) -> JsonResponse:
    return JsonResponse({"status": "ok"})

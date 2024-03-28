from django.http import HttpResponse


def index(request) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")

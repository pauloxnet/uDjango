from django.conf import settings
from django.core.handlers import asgi
from django.http import JsonResponse
from django.urls import path

settings.configure(ALLOWED_HOSTS="*", ROOT_URLCONF=__name__)

app = asgi.ASGIHandler()


async def root(request):
    return JsonResponse({"message": "Hello World"})


urlpatterns = (path("", root),)
from django import conf, http, urls
from django.core.handlers.asgi import ASGIHandler

conf.settings.configure(ALLOWED_HOSTS="*", ROOT_URLCONF=__name__)

app = ASGIHandler()


async def root(request):
    return http.JsonResponse({"message": "Hello World"})


urlpatterns = [urls.path("", root)]

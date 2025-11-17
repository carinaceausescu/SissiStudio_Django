import datetime
from urllib.parse import urlparse
from .views import get_ip, lista_accesari, Accesare


class MiddlewareNou:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = get_ip(request)
        url = request.build_absolute_uri()
        acc = Accesare(ip = ip, url = url, data = datetime.datetime.now())
        lista_accesari.append(acc)
        response = self.get_response(request)
        return response

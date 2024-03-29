from django.http import HttpResponse
from django.views import View
from django.http  import JsonResponse

from .models      import Basic

class BasicView(View):
    def get(self, request):
        basics = list(Basic.objects.values())
        return JsonResponse(basics, safe=False, status=200)


def ping(request):
    return HttpResponse('pong')

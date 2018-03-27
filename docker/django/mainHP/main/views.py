from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index for user. \n 準備中")

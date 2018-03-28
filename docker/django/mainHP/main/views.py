from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


@login_required
def mypage(request):
    return render(request, 'main/mypage.html')


@login_required
def redilect(request):
    return render(request, 'main/redilect.html')

from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # path('mypage', views.mypage, name='mypage'),
    # path('redilect', views.redilect, name='redilect'),
    # path(
    #     '^login',
    #     auth_views.login,
    #     {'template_name': 'app/login.html'},
    #     name='login'
    # ),
    # path(
    #     '^logout',
    #     auth_views.logout,
    #     {'template_name': 'app/logout.html'},
    #     name='logout'
    # ),
]

from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
        url(r'^login/$',views.login,name="login"),
]

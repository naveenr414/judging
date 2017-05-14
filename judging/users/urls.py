from django.conf.urls import include,url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

app_name="users"
urlpatterns = [
        url(r'^login/$',views.login,name="login"),
	url(r'^register/$',views.register,name="register"),
	url(r'^registercomplete/$',views.registerComplete,name="registerComplete"),
]

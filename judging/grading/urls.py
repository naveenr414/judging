from django.conf.urls import url

from . import views

app_name = "grading"
urlpatterns = [
	url(r'^$',views.index,name="index"),
	url(r'^problem/$',views.problem,name="problem"),
	url(r'^submit/$',views.submit,name="submit"),
]

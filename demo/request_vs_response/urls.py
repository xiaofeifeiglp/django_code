
from django.conf.urls import  url

from request_vs_response import views

urlpatterns = [
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),
]
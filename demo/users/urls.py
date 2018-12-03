from django.conf.urls import url

from users import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),
    url(r'^url_reverse/$', views.url_reverse),
    url(r'^demoview/$', views.demo_view),

]
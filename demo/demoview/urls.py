from django.conf.urls import url

from demoview import views
from demoview.views import my_decorator

urlpatterns = [
    url(r'^indexview/$', views.index_view),
    url(r'^indexcount/$', views.index_count),
    # 类视图, 注册
    url(r'^register/$', views.RegisterView.as_view()),
    url(r'^demo/$', views.Demoview.as_view()),  # 第二种方式
    # url(r'^demo/$', my_decorator(views.Demoview.as_view())),  # 第一种方法
    url(r'^index/$', views.index)
]
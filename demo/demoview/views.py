from _datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# 创建视图函数 indexview
# /demovie/indexview
from django.template import loader
from django.utils.decorators import method_decorator

# demoview/index
def index(request):
    # # 1.获取模板
    # template=loader.get_template('index.html')
    # context={'city':'王菲'}
    # # 2.渲染模板
    # return HttpResponse(template.render(context))

    # context = {'city':'北京'}
    # return render(request, 'index.html', context)

    context = {
        'city':'北京',
        'adict':{
            'name':'西游记',
            'author':'吴承恩'
        },
        'alist':[1,2,3,4,5],
        'now_date':datetime.now()
    }
    return render(request, 'index.html', context)

def index_view(request):
    # 获取请求方法, 判断是GET/PODT请求
    if request.method == 'GET':
        # 根据不同的请求方式,做不同的操作处理
        return HttpResponse('indexview get func')
    else:
        # 根据不同的请求方式,做不同的操作处理
        return HttpResponse('indexview post func')

# /demoview/indexcount
def index_count(request):
    return HttpResponse('hello world')


# 导入类视图的父类view
# demoview/register
from django.views.generic import View

class RegisterView(View):
    """类视图 处理注册"""
    def get(self, request):
        '''处理GET请求, 返回注册页面'''
        # return render(request, 'register.html')
        return HttpResponse('这里实现注册逻辑')

    def post(self, request):
        '''处理POST请求, 实现注册逻辑'''
        return HttpResponse('这里实现注册逻辑')

# 装饰器函数
# demoview/
def my_decorator(view_func):
    def wrapper(request, *args, **kwargs):
        print("装饰器函数被调用...")
        print("请求方式为: %s" % request.method)
        return view_func(request, *args, **kwargs)
    return wrapper

# @method_decorator(my_decorator, name='get')
class Demoview(View):
    @method_decorator(my_decorator)  # dispatch = my_decorator(dispatch)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        print("get方法被调用")
        return HttpResponse("OK")

    def post(self, request):
        print('post方法被调用')
        return HttpResponse('ok')

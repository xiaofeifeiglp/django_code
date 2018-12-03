from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# flask
# @api.route('/index')
# def index():
#     return 'hello world'

# /index
def index(request):
    return HttpResponse('helo world')

from django.urls import reverse
def url_reverse(request):
    res_url = reverse('users:index')
    return HttpResponse('OK')

# users/demoview
def demo_view(request):
    print('view视图被调用')
    return HttpResponse('OK')

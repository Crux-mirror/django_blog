from django.shortcuts import render
from django.http import HttpResponse
from blog import models
# Create your views here.
def hello(request):
    return HttpResponse("Heelo,world")

def orm(request):
    #models.Article.objects.create(title='新增标题1',category_id=3,body='增加内容-',user_id=1)
    print(request.path)
    print(request.get_full_path())
    print(request.method)
    print(request.body)
    print(request.GET)
    print(request.COOKIES)
    return HttpResponse('orm')

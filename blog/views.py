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

def index(request):
    sitename = 'Django blog 展示网站'
    url = 'www.django.cn'
    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    mydict = {
        'name':'crux',
        'qq':'34536',
        'wx':'vipdjango',
        'email':'4898237@qq.com',
        'Q群':'124345',
    }
    #把变量封装到上下文
    context = {
            'sitename':sitename,
            'url':url,
            'list':list,
            'mydict':mydict
            }
    #传递到模板中
    return render(request,'index.html',context)


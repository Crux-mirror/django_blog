from django.shortcuts import render
from django.http import HttpResponse
from blog import models
from .models import Article,Banner,Link
from .models import Category,Tags
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

def test(request):
    sitename = 'Django blog 展示网站'
    url = 'www.django.cn'
    allarticle = Article.objects.all()
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
            'mydict':mydict,
            'allarticle':allarticle,
            }
    #传递到模板中
    return render(request,'tmp.html',context)

def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    tui = Article.objects.filter(tui__id=1)[:3]
    allarticle = Article.objects.all().order_by('-id')[0:10]
    hot = Article.objects.all().order_by('views')[:10]
    remen = Article.objects.filter(tui__id=2)[:6]
    tags = Tags.objects.all()
    link = Link.objects.all()
    context = {
            'allcategory':allcategory,
            'banner':banner,
            'tui':tui,
            'allarticle':allarticle,
            'hot':hot,
            'remen':remen,
            'tags':tags,
            'link':link,
            }
    return render(request,'index.html',context)

def show(request,sid):
    show = Article.objects.get(id=sid)#查询指定ID的文章
    allcategory = Category.objects.all()#导航上的分类
    tags = Tags.objects.all()#右侧所有标签
    remen = Article.objects.filter(tui__id=2)[:6]#右侧热门推荐
    hot = Article.objects.all().order_by('?')[:10]#内容下面的您可能感兴趣的文章，随机推荐
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'show.html', locals())
def list(request,lid):
    list = Article.objects.filter(category_id=lid)
    cname = Category.objects.get(id=lid)
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tags = Tags.objects.all()
    page = request.GET.get('page')#在URL中获取当前页面数
    paginator = Paginator(list, 5)#对查询到的数据对象list进行分页，设置超过5条数据就分页
    try:
        list = paginator.page(page)#获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)#如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'list.html', locals())
def tag(request,tag):
    list = Article.objects.filter(tags__name=tag)#通过文章标签进行查询文章
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    tname = Tags.objects.get(name=tag)#获取当前搜索的标签名
    page = request.GET.get('page')
    tags = Tags.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1)  # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'tags.html', locals())

def search(request):
    ss=request.GET.get('search')#获取搜索的关键词
    list = Article.objects.filter(title__icontains=ss)#获取到搜索关键词通过标题进行匹配
    remen = Article.objects.filter(tui__id=2)[:6]
    allcategory = Category.objects.all()
    page = request.GET.get('page')
    tags = Tags.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page) # 获取当前页码的记录
    except PageNotAnInteger:
        list = paginator.page(1) # 如果用户输入的页码不是整数时,显示第1页的内容
    except EmptyPage:
        list = paginator.page(paginator.num_pages) # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
    return render(request, 'search.html', locals())
def about(request):
    pass

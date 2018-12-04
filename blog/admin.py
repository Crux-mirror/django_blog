from django.contrib import admin
#导入需要管理的库
from .models import Banner,Category,Tags,Tui,Article,Link
# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #文章想要显示的字段
    list_display = ('id','category','title','tui','user','views','created_time')
    #分页
    list_per_page = 50
    #后台数据排列方式
    ordering = ('-created_time',)
    #设置字段可编辑
    list_display_links = ('id','title')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','text_info','img','link_url','is_active')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','index')

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id','name','link_url')


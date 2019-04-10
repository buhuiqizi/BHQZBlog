from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#-------------文章分类---------------
class Category(models.Model):
    #表的两个字段
    name = models.CharField('博客分类', max_length = 100)
    index = models.IntegerField(default = 999, verbose_name = '分类排序')
    #元类 verbose_name是在网页中显示的名称 _pluarl是复数显示(但中文没有单复数)
    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

#-------------文章标签---------------
class  Tag(models.Model):
    name = models.CharField('文章标签', max_length = 100)
    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField('标题', max_length = 70)
    Category = models.ForeignKey(Category, on_delete = models.DO_NOTHING, \
                                verbose_name = '分类', blank = True, null = True)
    tags = models.ManyToManyField(Tag, verbose_name = '标签', blank = True)
    img = models.ImageField(upload_to = 'article_img/%Y/%m/%d', verbose_name = '文章图片', \
                            blank = True, null = True)
    body = models.TextField()
    view = models.PositiveIntegerField('阅读量', default = 0)
    created_time = models.DateTimeField('发布时间', auto_now_add = True)
    modifield_time = models.DateTimeField('修改时间', auto_now = True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    def __str__(self):
        return self.title

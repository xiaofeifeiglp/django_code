from django.test import TestCase

# Create your tests here.
# 设置Django运行所依赖的环境变量
import os
if not os.environ.get('DJANGO_SETTINGS_MODULE'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

# 让Django进行一次初始化
import  django
django.setup()

from  booktest.models import BookInfo, HeroInfo

# if __name__ == '__main__':
#     '''
#     # 1. 查询id为1的图书      属性名称__⽐较运算符=值
#     # 2. 查询书名包含'传'的图书。
#     # 3. 查询书名不为空的图书。
#     # 4. 查询编号为1或3或5的图书。
#     # 5. 查询编号大于3的图书。
#     # 6. 查询编号不等于3的图书。
#     # 7. 查询1980年发表的图书。
#     # 8. 查询1980年1月1日后发表的图书。
#     '''
#
#     # 1. 查询id为1的图书
#     book = BookInfo.objects.get(id=1)
#     print(book)
#     book1 = BookInfo.objects.filter(id__exact=1)
#     print(book1)
#     # 2. 查询书名包含'传'的图书。
#     book2 = BookInfo.objects.filter(btitle__contains='传')
#     print(book2)
#     # 3. 查询书名不为空的图书。
#     book3 = BookInfo.objects.filter(btitle__isnull=False)
#     print(book3)
#     # 4. 查询编号为1或3或5的图书。
#     book4 = BookInfo.objects.filter(id__in=[1,3,5])
#     print(book4)
#     # 5. 查询编号大于3的图书。
#     book5 = BookInfo.objects.filter(id__gt=3)
#     print(book5)
#     # 6. 查询编号不等于3的图书。
#     book6 = BookInfo.objects.exclude(id=3)
#     print(book6)
#     # 7. 查询1980年发表的图书。
#     book7 = BookInfo.objects.filter(bpub_date__year=1980)
#     print(book7)
#     # 8. 查询1980年1月1日后发表的图书。
#     book8 = BookInfo.objects.filter(bpub_date__gt='1980-1-1')
#     print(book8)

# if __name__ == '__main__':
#     '''
#     # F对象: 查询时字段之间的比较
#     # 1. 查询阅读量大于等于评论量的图书。
#     # 2. 查询阅读量大于2倍评论量的图书。
#
#     # Q对象: 用于查询时多个条件之间的逻辑关系 &(且) |(或) ~(非)
#     # 1. 查询阅读量大于20，并且编号小于3的图书。
#     # 2. 查询阅读量大于20，或编号小于3的图书。
#     # 3. 查询编号不等于3的图书。
#     '''
#     # F对象:查询时字段之间的比较
#     from django.db.models import F
#     # 1. 查询阅读量大于等于评论量的图书。
#     book1 = BookInfo.objects.filter(bread__gt=F('bcomment'))
#     print(book1)
#     # 2. 查询阅读量大于2倍评论量的图书。
#     book2 = BookInfo.objects.filter(bread__gt=F('bcomment')*2)
#     print(book2)
#     # Q对象: 用于查询时多个条件之间的逻辑关系 &(且) |(或) ~(非)
#     from django.db.models import Q
#     # 1. 查询阅读量大于20，并且编号小于3的图书。
#     # book3 = BookInfo.objects.filter(bread__gt=20, id__lt=3)
#     book3 = BookInfo.objects.filter(Q(bread__gt=20)&Q(id__lt=3))
#     print(book3)
#     # 2. 查询阅读量大于20，或编号小于3的图书。
#     book4 = BookInfo.objects.filter(Q(bread__gt=20) | Q(id__lt=3))
#     print(book4)
#     # 3. 查询编号不等于3的图书。
#     book5 = BookInfo.objects.filter(~Q(id=3))
#     print(book5)

# if __name__ == '__main__':
#     '''
#     # 聚合: count sum avg max min
#     # 1. 查询图书的总阅读量。
#     # 2. 查询图书总数。
#     # 3. 对所有图书按照阅读量从大到小进行排序。
#     '''
#     from django.db.models import Count, Sum, Avg, Max, Min
#     # 1. 查询图书的总阅读量。
#     res1 = BookInfo.objects.aggregate(Sum('bread'))
#     print(res1)
#     # 2. 查询图书总数。
#     res_counut = BookInfo.objects.count()
#     print(res_counut)
#     res2 = BookInfo.objects.aggregate(Count('id'))
#     print(res2)
#     # 3. 对所有图书按照阅读量从小到大进行排序。
#     book1 = BookInfo.objects.order_by('bread')
#     print(book1)
#     # 4. 对所有图书按照阅读量从大到小进行排序。
#     book2 = BookInfo.objects.order_by('-bread')
#     print(book2)

# if __name__ == '__main__':
#     # 更新
#     hero = HeroInfo.objects.get(id=19)
#     hero.hname = '猪无能'
#     hero.save()
#
#     # 返回是更新行数
#     res = HeroInfo.objects.filter(hname='沙悟净').update(hname='沙僧')
#     print(res)
#
#     # 删除
#     hero = HeroInfo.objects.get(id=13)
#     hero.delete()
#
#     HeroInfo.objects.get(id=10).delete()


# if __name__ == '__main__':
#     '''
#     # 查询和对象关联的信息
#     # 1.查询和id为1的图书关联的英雄人物信息
#     # 获取和book关联的英雄的数据
#     # 2.查询和西游记关联的英雄人物信息
#     # 3.查询和id为1的英雄人物关联的图书信息
#     # 获取和hero关联的图书对象
#     # 4.查询和孙悟空关联的图书信息
#     '''
#     # 查询和对象关联的信息
#
#     # 1.查询和id为1的图书关联的英雄人物信息
#     heros = HeroInfo.objects.filter(hbook_id=1)
#     print(heros)
#     # 获取和book关联的英雄的数据
#     book = BookInfo.objects.get(id=1)
#     print(book)
#     heros = book.heroinfo_set.all()
#     print(heros)
#     # 2.查询和西游记关联的英雄人物信息
#     book = BookInfo.objects.get(btitle='西游记')
#     heros = book.heroinfo_set.all()
#     print(heros)
#     # 3.查询和id为1的英雄人物关联的图书信息
#     heros = HeroInfo.objects.get(id=1)
#     print(heros)
#     # 获取和hero关联的图书对象
#     book = heros.hbook
#     print(book)
#     # 4.查询和孙悟空关联的图书信息
#     heros = HeroInfo.objects.get(hname='孙悟空')
#     book = heros.hbook
#     print(book)

if __name__ == '__main__':
    '''
    # 通过模型类实现关联查询
    # 1.查询图书,要求图书英雄为"孙悟空"
    # 2.查询图书,要求图书中英雄的描述包含'八'
    # 3.查询书名为'天龙八部'的所有英雄
    # 4.查询图书阅读量大于30的所有英雄
    '''
    # # 通过模型类实现关联查询
    # # 1.查询图书,要求图书英雄为"孙悟空"
    # heros = HeroInfo.objects.get(hname='孙悟空')
    # book = heros.hbook
    # print(book)
    #
    # books = BookInfo.objects.filter(heroinfo__hname='孙悟空')
    # print(books)
    # print('----------------------------')
    # # 2.查询图书,要求图书中英雄的描述包含'空'
    # heros = HeroInfo.objects.get(hname__contains='空')
    # book = heros.hbook
    # print(book)
    #
    # books = BookInfo.objects.filter(heroinfo__hname__contains='空')
    # print(books)
    # # 3.查询书名为'天龙八部'的所有英雄
    # book = BookInfo.objects.get(bread=36)
    # heros = book.heroinfo_set.all()
    # print(heros)
    #
    # heros = HeroInfo.objects.filter(hbook__bread=36)
    # print(heros)
    #
    # # 4.查询图书阅读量大于30的所有英雄
    #
    # heros = HeroInfo.objects.filter(hbook__bread__gt=30)
    # print(heros)



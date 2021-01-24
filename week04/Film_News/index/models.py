from django.db import models

# Create your models here.
class Type(models.Model):
    typename = models.CharField(max_length=20)

class Name(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    starts = models.CharField(max_length=10)


# python manage.py makemigrations
# python manage.py migrate 

#数据库操作
#python manage.py shell 
# from index.models import * 
# n = Name()
# n.name = '红楼梦'
# n.author = '曹雪芹'
# n.starts = 9.6
# n.save()

# Name.objects.create(name = '红楼梦', author = '曹雪芹',starts = 9.6)
# Name.objects.create(name = '活  着', author = '余  华',starts = 9.4)
# Name.objects.create(name = '平凡的世界', author = '路遥',starts = 9.4)
# Name.objects.create(name = '穆斯林的葬礼', author = '霍达',starts = 9.4)
# Name.objects.create(name = '挪威的森林', author = '村上春树',starts = 9.4)
# Name.objects.create(name = '基督山伯爵', author = '大仲马',starts = 9.4)
# Name.objects.create(name = '教父', author = '普佐',starts = 9.4)
# Name.objects.create(name = '苏菲的世界', author = '乔斯坦·贾德',starts = 9.4)
# Name.objects.create(name = '麦田里的守望者', author = '塞林格',starts = 9.4)
# Name.objects.create(name = '白鹿原', author = '陈忠实',starts = 9.4)


# Name.objects.create(name = '破碎的四月', author = '卡达莱',starts = 9.4)
# Name.objects.create(name = '万历十五年', author = '黄仁宇',starts = 9.4)
# Name.objects.create(name = '美的历程', author = '李泽厚',starts = 9.4)
# Name.objects.create(name = '围城', author = '钱钟书',starts = 9.4)
# Name.objects.create(name = '汤姆叔叔的小屋', author = '斯托夫人',starts = 9.4)
# Name.objects.create(name = '尘埃落定', author = '阿来',starts = 9.4)
# Name.objects.create(name = '根', author = '亚历克·黑尔',starts = 9.4)
# Name.objects.create(name = '生命从明天开始', author = '心曼 春曼',starts = 9.4)
# Name.objects.create(name = '许三观卖血记', author = '余华',starts = 9.4)
# Name.objects.create(name = '牛虻', author = '伏尼契',starts = 9.4)

# Name.objects.get(id=2).name

# Name.objects.filter(name = '汤姆叔叔的小屋').update(name = '汤姆叔叔的小屋XXXX')

# Name.objects.filter(name = '汤姆叔叔的小屋XXXX').delete()
# Name.objects.all()
# Name.objects.all().delete()
# Name.objects.all()[0]
# Name.objects.all()[0].name

# n = Name.objects.all()[0].name
# n[0]
# Name.objects.values_list('name')
# Name.objects.values_list('name').count()
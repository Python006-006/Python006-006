from django.db import models

# Create your models here.
from datetime import datetime


class Orders(models.Model):
    """
    订单
    """
    orderid = models.CharField(
        max_length=30, verbose_name='订单id', default='abc')
    order = models.CharField(max_length=30, verbose_name='订单内容', default='abc')
    createtime = models.DateTimeField(auto_now_add=True)
    # 第一次migrations需注释掉owner
    owner = models.ForeignKey(
        'auth.User', related_name='orders', on_delete=models.CASCADE)

    class Meta:
        ordering = ['createtime']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        super(Orders, self).save(*args, **kwargs)
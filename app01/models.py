from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

class Product_number(models.Model):
    name = models.CharField(verbose_name='产品名称', max_length=64, unique=True)
    xl_number = models.CharField(verbose_name='新罗编号', max_length=64)
    duw_number = models.CharField(verbose_name='得物编号', max_length=64)
    xz_number = models.CharField(verbose_name='小猪编号', max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['name']]


class Duw_product_price(models.Model):
    """ 得物价格模型 """
    name = models.ForeignKey(verbose_name='产品名称',to='Product_number',to_field='name',
                             related_name='duw_name', on_delete=models.CASCADE)
    size = models.CharField(verbose_name='规格', max_length=24)
    duw_price = models.DecimalField(verbose_name='得物价格',max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name='日期')


    # def get_xl_number_display(self):
    #     return self.xl_number.xl_number
    #
    # def get_xz_number_display(self):
    #     return self.xz_number.xz_number
    #
    # def get_duw_number_display(self):
    #     return self.duw_number.duw_number
    #
    # class Meta:
    #     verbose_name_plural = 'Duw_product_prices'


class Xz_product_price(models.Model):
    """ 小猪价格模型 """
    name = models.ForeignKey(verbose_name='产品名称', to='Product_number', to_field='name',
                             related_name='xz_name', on_delete=models.CASCADE)
    size = models.CharField(verbose_name='规格', max_length=24)
    xz_price = models.DecimalField(verbose_name='小猪价格',max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name='日期')

from rest_framework import serializers
from .models import Product_number, Duw_product_price, Xz_product_price
from django.contrib.auth import get_user_model


class Product_numberSerializers(serializers.Serializer):

    name = serializers.CharField(max_length=64)
    xl_number = serializers.CharField(max_length=64)
    duw_number = serializers.CharField(max_length=64)
    xz_number = serializers.CharField(max_length=64)


class Duw_product_priceModelSerializers(serializers.ModelSerializer):

    name = serializers.PrimaryKeyRelatedField(queryset=Product_number.objects.all())
    class Meta:
        model = Duw_product_price
        fields = '__all__'




class Xz_product_priceModelSerializers(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(queryset=Product_number.objects.all())
    class Meta:
        model = Xz_product_price
        fields = '__all__'




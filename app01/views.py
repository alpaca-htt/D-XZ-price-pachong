from django.shortcuts import render,HttpResponse

from rest_framework.views import APIView
from django.http import Http404
from .models import Product_number, Duw_product_price, Xz_product_price
from .serializers import Product_numberSerializers, Duw_product_priceModelSerializers, Xz_product_priceModelSerializers
from rest_framework.response import Response
import json
import ast
# Create your views here.

class PriceView(APIView):
    # def get(self,request):
    #     # request_meta = request.META.get('HTTP_X_REAL_IP')
    #     # print(request_meta)
    #     # 获取访问用户的IP地址
    #     x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    #     if x_forwarded_for:
    #         ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    #     else:
    #         ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    #     if ip != '192.168.3.12':
    #         return Response('无法访问')
    #     return Response()
    def post(self,request):
        if request.data.get('product'):



            product_list = Product_number.objects.filter(xl_number=request.data.get('product')).first()
            if not product_list:
                response_data = {
                    "name": None,
                    "size": None,
                    "d_price": None,
                    "d_create_time": None,
                    "xz_price": None,
                    "xz_create_time": None
                }
                return Response(response_data,status=200)
            print(product_list)
            duw_product_price = product_list.duw_name.all().first()
            xz_product_price = product_list.xz_name.all().first()
            print(duw_product_price)
            print(xz_product_price)
            # for item in product_price:
            #     print(item.name)
            #     print(item.size)
            #     print(item.duw_price)
            #     print(item.create_time)
            #     print('------------')
            duw_serializer = Duw_product_priceModelSerializers(instance=duw_product_price)
            xz_serializer = Xz_product_priceModelSerializers(instance=xz_product_price)
            # response_data = {
            #     'duw_product_price': duw_serializer.data,
            #     'xz_product_price': xz_serializer.data
            # }

            response_data = {
                "name": duw_serializer.data['name'],
                "size": duw_serializer.data['size'],
                "d_price": duw_serializer.data['duw_price'],
                "d_create_time": duw_serializer.data['create_time'],
                "xz_price": xz_serializer.data['xz_price'],
                "xz_create_time": xz_serializer.data['create_time']
            }
            return Response(response_data,status=200)
        elif request.data.get('list'):
            product_list = ast.literal_eval(request.data['list'])
            print(product_list)
            print(type(product_list))
            data_list = []
            for product in product_list:
                queryset = Product_number.objects.filter(xl_number=product).first()
                if not product_list:
                    response_data = {
                        "name": None,
                        "size": None,
                        "d_price": None,
                        "d_create_time": None,
                        "xz_price": None,
                        "xz_create_time": None
                    }
                    data_list.append(response_data)
                duw_product_price = queryset.duw_name.all().first()
                xz_product_price = queryset.xz_name.all().first()
                duw_serializer = Duw_product_priceModelSerializers(instance=duw_product_price)
                xz_serializer = Xz_product_priceModelSerializers(instance=xz_product_price)
                response_data = {
                    "name": duw_serializer.data['name'],
                    "size": duw_serializer.data['size'],
                    "d_price": duw_serializer.data['duw_price'],
                    "d_create_time": duw_serializer.data['create_time'],
                    "xz_price": xz_serializer.data['xz_price'],
                    "xz_create_time": xz_serializer.data['create_time']
                }
                data_list.append(response_data)
            return Response(data_list, status=200)

        return Response(status=404)
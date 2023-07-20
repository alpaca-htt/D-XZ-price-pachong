from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    re_path(r'^price/$', views.PriceView.as_view()),
    re_path(r'^price/(?P<pk>[0-9]+)$', views.PriceView.as_view()),]

urlpatterns = format_suffix_patterns(urlpatterns)
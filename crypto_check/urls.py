# from django.conf.urls import url
from django.urls import path
from crypto_check.views import *

urlpatterns = [
    path(r'price/btc',  PriceDetails.as_view({'get': 'get_details'}),name="check_price"),
]
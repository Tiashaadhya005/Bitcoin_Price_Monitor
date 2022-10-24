from django.shortcuts import render
from datetime import datetime
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from crypto_check.models import CryptoDataStore
from crypto_check.serializer import CryptoDataStoreSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status, viewsets
from rest_framework.decorators import action


class PriceDetails(viewsets.ModelViewSet):
    """
    Functionality to fetch price of bitcoin for a particular day
    """
    # pagination_class = LimitOffsetPagination
    serializer_class = CryptoDataStoreSerializer

    queryset = CryptoDataStore.objects.all()
    # import pdb;pdb.set_trace()

    @action(detail=False,methods=['get'],url_name="check_price",url_path="/api/price/btc")
    def get_details(self, request):
        """
        req param : date=DD-MM-YYYY
        """
        try:
            request_date= request.GET.get('date')
            print(request_date)
            if not request_date :
                return Response(data= "Please provide a date in request parameter" ,status=400)

            date = datetime.strptime(request_date,"%d-%m-%Y").date()

            if date > datetime.utcnow().date():
                return Response(data= "Please provide a date which not greater than today (utc)" ,status=400)

            query_result= CryptoDataStore.objects.filter(processing_date= date)
            print(len(query_result))
            if query_result.exists():
                page = self.paginate_queryset(query_result)
                if page is not None:
                    serializer = self.get_serializer(page, many=True)
                    return self.get_paginated_response(serializer.data)
                
                serializer = self.get_serializer(page, many=True)
                print(serializer.data)
                return Response(serializer.data)
            else:
                return Response(data="Sorry No Record Found For This Date!!!", status= 404)
            
        except Exception as err:
            return Response(data=str(err),status=500)

# def list(self,request):
#     country_data = Country.objects.all()

#     page = self.paginate_queryset(country_data)
#     if page is not None:
#        serializer = self.get_serializer(page, many=True)
#        return self.get_paginated_response(serializer.data)

#     serializer = self.get_serializer(country_data, many=True)
#     return Response(serializer.data)

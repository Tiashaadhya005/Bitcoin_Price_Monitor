from rest_framework import serializers
from crypto_check.models import *

time_fmt = "%Y-%m-%d %H: %M: %S"

class CryptoDataStoreSerializer(serializers.ModelSerializer):
    
    timestamp = serializers.SerializerMethodField()

    def get_timestamp(self,obj):
        formatted_time = datetime.strftime(obj.timestamp,time_fmt)
        return formatted_time

    class Meta:
        model = CryptoDataStore
        fields = ("timestamp","price","coin")
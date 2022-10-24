from datetime import datetime
from django.db import models
import django.utils.timezone as dz

# Create your models here.

class CryptoDataStore(models.Model):
    processing_date= models.DateField(default= dz.now().date())#datetime.utcnow().date())
    timestamp =  models.DateTimeField(default=datetime.utcnow())
    price = models.FloatField(null= True)
    coin = models.CharField(default= "btc",max_length=256)

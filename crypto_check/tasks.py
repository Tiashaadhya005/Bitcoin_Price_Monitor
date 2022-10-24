from pycoingecko import CoinGeckoAPI
from datetime import datetime
from crypto_monitor_app.settings import EMAIL_HOST_USER
from crypto_monitor_app.configurations import DEFAULT_MAX, DEFAULT_MIN, MAX_VALUE,MIN_VALUE
import os

from datetime import datetime as dt

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_monitor_app.settings')
from django.core.mail import send_mail

from celery import Celery

from celery import shared_task
from crypto_check.models import CryptoDataStore


from django.conf import settings

if not MAX_VALUE:
    MAX_VALUE=DEFAULT_MAX

if not MIN_VALUE:
    MIN_VALUE=DEFAULT_MIN

MAX_VALUE= int(MAX_VALUE)
MIN_VALUE = int(MIN_VALUE)

@shared_task()
def send_mail_task(price):
    """
    This is a celery task for sending email. It tries to send mail via Mailtrap api.
    :param data:
    :return:
    """
    if price>MAX_VALUE :
        increase_amount = price - MAX_VALUE
        MESSAGE_ = f"BITCOIN price increased than it's maximum value by :{increase_amount}usd \n Price : {price}"
    if price<MIN_VALUE :
        decrease_amount =  MIN_VALUE - price 
        MESSAGE_ =  f"BITCOIN price decreased than it's minimum value by {decrease_amount}usd\n Price : {price}"
    data={
        "subject":"ALERT : BITCOIN VALUE",
        "message": MESSAGE_
    }
    print(data)
    try:
        EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
        from crypto_monitor_app.configurations import recipient_list
        
        send_mail(
            data["subject"],
            data["message"],
            EMAIL_HOST_USER,
            recipient_list,
            html_message=data['message'],
            fail_silently=False,
        )
        return
        
    except Exception as e:
        msg = f"Send mail task failed for %s" % e
        print(msg)


from time import sleep
@shared_task
def check_coin_value():
    print("30 second cron to update price ")
    while(True):
        cg = CoinGeckoAPI()
        price = cg.get_price(ids='bitcoin', vs_currencies='usd')
        price = price.get('bitcoin').get('usd')
        CryptoDataStore.objects.create(**{"price":price})
        with open("/opt/test1.txt","a+") as f: 
            msg = f"INFO: [{datetime.utcnow()}] -- price of bitcoin : {price} \n "
            f.write(msg)
        print("PRICE - ",price)
        if price >MAX_VALUE or price < MIN_VALUE:
            send_mail_task.apply_async([price])
        
        sleep(30)


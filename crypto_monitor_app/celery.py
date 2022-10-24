from calendar import week
from datetime import datetime, timedelta
import os
from celery import Celery
from celery.schedules import crontab
import celery
from time import sleep


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crypto_monitor_app.settings")
app = Celery("crypto_monitor_app", include=['crypto_check.tasks'])

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# FUTURE SCOPE : IF THE CELERY CRON NEEDS TO BE CHANGED YOU CAN CHANGE THE VARIABLE 'SCHEDULLING_MINUTE' TO CHANGE THE MINUTE
processing_date=datetime.utcnow()
hour=processing_date.hour
#start after 5 min of container start
minute = (processing_date+timedelta(minutes=5)).minute
weekday= processing_date.weekday()
day = processing_date.day
month=processing_date.month
app.conf.beat_schedule = {
    'group_1q': {
        'task': 'crypto_check.tasks.check_coin_value',
        'schedule': crontab(minute = minute)#, hour= hour, day_of_week= weekday, day_of_month = day, month_of_year = month)
    }
}


# Bitcoin_Price_Monitor

## Project Summary :
Bit COIN Price Monitor App:

Purpose of the django project :
-------------------------------------
* check the price of bitcoin in every 30 sec.
* If the price increases/decreases than the limit value then send mail to receipant mail.
* through the api : `/api/price/btc?<date=DD-MM-YYYY>` show all the prices of bitcoin in usd  for any particular date  

Steps For Deployment:
-------------------------------------
* Take pull from this git repo inside suitable folder.
* go inside the main folder `cd crypto_monitor_app`
* build the image `bash docker/docker_build.sh`
    * It will take the `MAX_VALUE` and `MIN_VALUE` input .
    * This values are optional if you missed it , system will automatically update the MAX_VALUE as 2000 and MIN_VALUE as 1000
    * You can change these default values by changing the variable `DEFAULT_MAX` and `DEFAULT_MIN ` inside crypto_monitor_app(inside folder)/configurations.py
    * The 30s cron will start 5 min after the container up, you can change the default time the above configuration file through the variable `DEFAULT_START_TIME`
    * you can also add your email under `recipient_list` of the same file if you want to receive the email notification.
    (https://mailtrap.io/inboxes/1932448/messages/3078307821)
    

* finally run this to up the container : `cd docker && docker-compose up`
* Now you can open `0.0.0.0:8000` in your browser and check api 


#!/bin/bash

printf "\n\n------------- BUILDING DOCKER IMAGE -------------\n\n"

printf "ENTER MAX & MIN PRICE\n"
printf "INPUT MAX_VALUE: " && read MAX_VALUE
printf "INPUT MIN_VALUE: " && read MIN_VALUE

# update password and username in configuration
sed -i -e "s#\(MAX_VALUE = \).*#\1'${MAX_VALUE:=2000}'#g" -e "s#\(MIN_VALUE = \).*#\1'${MIN_VALUE:=1000}'#g" crypto_monitor_app/configurations.py



python3 -m pip install --upgrade pip
pip3 install -r requirements.txt --upgrade --no-deps


# pull the base image
sudo docker pull python:3.9.7-slim-buster
# python3 -m pip install --upgrade pip
# pip3 install -r requirements.txt --upgrade --no-deps

sudo docker  build -t bitcoin_check_image1 -f ./docker/Dockerfile . 


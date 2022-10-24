FROM python:3.9-slim-buster AS base
WORKDIR /crypto_monitor_app
ADD requirements.txt  /crypto_monitor_app

FROM base
WORKDIR /crypto_monitor_app
COPY --from=base /crypto_monitor_app /crypto_monitor_app
# ENV PYTHONPATH="${PYTHONPATH}:/crypto_monitor_app/cli/source"
# ENV PYTHONPATH="${PYTHONPATH}:/crypto_monitor_app/cli/source/pytransform"
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt --upgrade --no-deps
#--upgrade --no-deps
ADD . /crypto_monitor_app
RUN ls

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
# RUN python3 manage.py runserver
# RUN python -m celery -A crypto_monitor_app worker -l info

# ADD . /crypto_monitor_app

# ENTRYPOINT ["python3 ../manage.py runserver"]
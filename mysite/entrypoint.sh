#!/bin/sh

gunicorn --workers=2 --bind=0.0.0.0:8000 mysite.wsgi:application


python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input
# python manage.py runserver 0.0.0.0:8000
DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

#!/bin/sh

# For deployment
set -e

python manage.py wait_for_db

# Collect static into settings.STATIC_ROOT
python manage.py collectstatic --noinput

python manage.py migrate

# master: master daemon (foreground)
# app.wsgi: django
uwsgi --socket :9000 --workers 4 --master --enable-threads --module app.wsgi

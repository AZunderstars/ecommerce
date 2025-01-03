#!/bin/sh

set -e

python manage.py collectsttaic --noinput
python manage.py migrate

uwsgi --socket :9000 --workers 4 --master --enable-threades --module app.wsgi

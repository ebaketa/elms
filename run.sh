#!/bin/bash

cd /var/www/elms

source .venv/bin/activate

exec python manage.py runserver 0.0.0.0:8000

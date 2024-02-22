#! /usr/bin/env sh
set -e

python manage.py migrate
exec daphne  -b 0.0.0.0 --port 8000 project.asgi:application


#! /usr/bin/env sh
set -e

python manage.py migrate
exec uvicorn --reload --host 0.0.0.0 --port 8000 --log-level info "project.asgi:application"

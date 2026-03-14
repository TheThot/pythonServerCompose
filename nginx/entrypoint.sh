#!/bin/sh
set -e

# Кастомизация порта
envsubst '${BACKEND_PORT}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf

# Запуск nginx
exec nginx -g 'daemon off;'
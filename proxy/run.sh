#!/bin/sh

set -e

envsubst < /etc/nginx/default.conf.tpl > /etc/nginx/conf.d/defualt.conf
nginx -g 'daemon off;'

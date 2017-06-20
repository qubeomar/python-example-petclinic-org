#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $DIR/
set -o allexport
#source env-init.sh

#uwsgi --http "${DEFAULT_LISTENER_HOST}":"${DEFAULT_LISTENER_PORT}" --http-keepalive --add-header "Connection: keep-alive" --pyargv "--debug" --module qube.src.api.app --callable app --no-site --pythonpath=/usr/local/lib/python3.5 --pythonpath=/usr/local/lib/python3.5/site-packages --processes "${DEFAULT_PROCESS_COUNT}" --buffer-size 8192 --enable-threads 2>&1 > nohup.out

#uwsgi --http 0.0.0.0:8080 --http-keepalive --add-header "Connection: keep-alive" --pyargv "--debug" --module petclinic.main --callable app --no-site --pythonpath=/usr/local/lib/python2.7 --pythonpath=/usr/local/lib/python2.7/site-packages --processes 3 --buffer-size 8192 --enable-threads 2>&1 > nohup.out

uwsgi --http "${DEFAULT_LISTENER_HOST}":"${DEFAULT_LISTENER_PORT}" --http-keepalive --add-header "Connection: keep-alive" --pyargv "--debug" --module petclinic.main --callable app --no-site --pythonpath=/usr/local/lib/python3.5 --pythonpath=/usr/local/lib/python3.5/site-packages --processes 3 --buffer-size 8192 --enable-threads 2>&1 > nohup.out

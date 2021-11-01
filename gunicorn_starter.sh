#!/bin/sh
# running gunicorn server with default port 8000 if PORT variable is not set
thePort=${PORT:-8000}
gunicorn projet_p13.wsgi:application --bind 0.0.0.0:$thePort

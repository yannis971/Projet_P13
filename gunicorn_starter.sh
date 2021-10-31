#!/bin/sh
thePort=${PORT:-8000}
gunicorn projet_p13.wsgi:application --bind 0.0.0.0:$thePort

#!/usr/bin/env bash

export FEED_URL=http://revistaautoesporte.globo.com/rss/ultimas/feed.xml

export POSTGRES_DB=postgres
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
export POSTGRES_HOST=database
export POSTGRES_PORT=5432

export REDIS_HOST=localhost
export REDIS_PORT=6379
export REDIS_DB=0

export DEV=$1

gunicorn --bind 0.0.0.0:8000 wsgi:application

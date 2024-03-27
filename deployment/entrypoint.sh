#!/bin/bash
set -e

case $1 in
  web)
    echo "Starting api server"
    exec gunicorn -c deployment/gunicorn.conf.py
  ;;

  deplayed_jobs)
    echo "Starting celery workers"
    exec celery -A base.base_celery:app worker --concurrency=2 --loglevel=INFO
  ;;

  dev)
    echo "Starting dev server"
    exec python manage.py runserver 0.0.0.0:8000
  ;;

  migrate)
    echo "Starting migrations"
    exec python manage.py migrate
  ;;

  scheduled_jobs)
    echo "Starting celery beat"
    exec celery -A base.base_celery:app beat --loglevel=INFO
  ;;

  uvicorn)
    echo "Starting uvicorn"
    exec uvicorn base.asgi:application --log-level debug --app-dir=/app --host 0.0.0.0 --port 8000
  ;;

  migrate_db)
    echo "Migrate db"
    exec python manage.py migrate --no-input
  ;;

  collectstatic)
    echo "Collected static files"
    exec python manage.py collectstatic --no-input
  ;;

  *)
    exec "$@"
  ;;
esac

exit 0
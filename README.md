# flask_gunicorn_celery_example

----

# usage

0. pre work
  - pip install -r requirement.txt

1. flask and celery
  - celery -A tcelery.celery_app worker
  - python main.py
  
2. flask and gunicorn
  - gunicorn unicorn:app -b 0.0.0.0:5000 -w [worker node count]

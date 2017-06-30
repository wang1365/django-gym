
FROM python:2.7.13

MAINTAINER wang1365@foxmail.com

ENV basedir /var/django-learning/

RUN mkdir -p $basedir

COPY ./* $basedir

WORKDIR $basedir

RUN pip install -r requirements.txt

RUN pip install uwsgi

CMD ["uwsgi", "--ini", "uwsgi.ini"]
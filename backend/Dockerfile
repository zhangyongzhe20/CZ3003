FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt /user/home/requirements.txt
RUN apk add zlib-dev jpeg-dev gcc musl-dev && apk add build-base libffi-dev  openssl-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps
RUN cd /user/home && python -m venv venv 
RUN source /user/home/venv/bin/activate && \
    pip install -U pip && pip install -U setuptools && \
    cd /user/home && pip install -r requirements.txt
RUN apk del .tmp-build-deps
RUN mkdir /user/home/mazerunner
WORKDIR /user/home/mazerunner
COPY ./mazerunner /user/home/mazerunner
COPY ./index.html /user/home/venv/lib/python3.7/site-packages/django/contrib/admin/templates/admin/index.html
COPY ./sites.py /user/home/venv/lib/python3.7/site-packages/django/contrib/admin/sites.py
RUN chmod -R 777 /user/home/mazerunner
RUN chmod -R 777 /user/home/venv

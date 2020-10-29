FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

ADD ./requirements.txt /requirements.txt
RUN apk add zlib-dev jpeg-dev gcc musl-dev
RUN apk add build-base libffi-dev  openssl-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps
RUN pip install -U pip && pip install -U setuptools
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /mazerunner
WORKDIR /mazerunner
COPY ./mazerunner /mazerunner

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user

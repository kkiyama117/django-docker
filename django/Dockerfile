FROM python:3.6
ENV PYTHONUNBUFFERED 1

ADD . /uwsgi

RUN mkdir -p /mainHP
RUN mkdir -p /static
ADD mainHP /mainHP
ADD static /static

WORKDIR /uwsgi
RUN pip install -r requirements.in

WORKDIR /mainHP
RUN pip install -r requirements.in
CMD init.sh

WORKDIR /uwsgi

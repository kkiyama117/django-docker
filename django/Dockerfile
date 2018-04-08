FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /static
ADD static /static

RUN mkdir -p /mainHP
ADD requirements.in  /mainHP/
RUN ["pip", "install", "-r", "mainHP/requirements.in"]

ADD mainHP/* /mainHP/
COPY uwsgi.ini init.sh /mainHP/
RUN ["pip", "install", "-r", "mainHP/requirements.in"]

WORKDIR /mainHP
RUN ["chmod", "+x", "./init.sh"]
ENTRYPOINT bash -c './init.sh && uwsgi --ini uwsgi.ini'

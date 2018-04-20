FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install postgresql -y

RUN mkdir -p /static
ADD static /static

RUN mkdir -p /mainHP
ADD requirements.in  /mainHP/
RUN ["pip", "install", "-r", "mainHP/requirements.in"]

COPY uwsgi.ini init.sh /mainHP/
RUN ["chmod", "+x", "/mainHP/init.sh"]
RUN ["chmod", "+r", "/mainHP/uwsgi.ini"]
ADD mainHP/* /mainHP/
ADD mainHP/requirements/* /mainHP/requirements/
RUN ["pip", "install", "-r", "mainHP/requirements/production.txt"]

WORKDIR /mainHP
CMD ["./init.sh"]

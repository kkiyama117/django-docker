FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /static
ADD static /static

RUN mkdir -p /mainHP
ADD requirements.in  /mainHP/
RUN ["pip", "install", "-r", "mainHP/requirements.in"]

COPY uwsgi.ini init.sh /mainHP/
RUN ["chmod", "+x", "/mainHP/init.sh"]
RUN ["chmod", "+r", "/mainHP/uwsgi.ini"]
ADD mainHP/* /mainHP/
RUN ["pip", "install", "-r", "mainHP/requirements.in"]

WORKDIR /mainHP
CMD ["./init.sh"]
ENTRYPOINT ["uwsgi","--ini"]
CMD ["./uwsgi.ini"]

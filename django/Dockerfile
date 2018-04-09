FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /static
ADD static /static

RUN mkdir -p /mainHP
ADD requirements.in  /mainHP/
RUN ["pip", "install", "-r", "mainHP/requirements.in"]

COPY uwsgi.ini init.sh /
RUN ["chmod", "+x", "/init.sh"]
RUN ["chmod", "+r", "/uwsgi.ini"]
ADD mainHP/* /mainHP/
RUN ["pip", "install", "-r", "mainHP/requirements.in"]

WORKDIR /mainHP
ENTRYPOINT ["./init.sh", "&&"]
CMD uwsgi --ini uwsgi.ini

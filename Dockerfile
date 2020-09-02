FROM ubuntu:18.04

MAINTAINER Adithya <adithya.ajith05@gmail.com>

RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3.6-dev curl gnupg
RUN apt-get -yqq install ffmpeg

WORKDIR /usr/src/app/splitrax/

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "192.168.99.100:8000"]
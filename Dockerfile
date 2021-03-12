FROM ubuntu:18.04

MAINTAINER Vivek Mogili "vivekmogili@gmail.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip \
  && pip3 install pytest

COPY logs/ /user/logs/
COPY logs_nested/ /user/logs_nested/
COPY configs/ /user/configs/
COPY scripts/ /user/scripts/ 
COPY test/ /user/test/

WORKDIR /user

RUN cat /user/configs/messages.csv
RUN pytest test

CMD python3 scripts/log_parser_notifier.py -d logs -u configs/users.csv -m configs/messages.csv
#CMD python3 /user/scripts/log_parser_notifier.py -d /user/logs_nested -u /user/configs/users.csv -m /user/configs/messages.csv
#CMD python3 /user/scripts/log_parser_notifier.py -d /user/logs_nested -u /user/configs/users2.csv -m /user/configs/messages2.csv

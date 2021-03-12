FROM ubuntu:18.04

MAINTAINER Vivek Mogili "vivekmogili@gmail.com"

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

COPY logs/ /user/logs/
COPY logs_nested/ /user/logs_nested/
COPY configs/ /user/configs/
COPY scripts/ /user/scripts/ 

RUN cat /user/configs/messages.csv

CMD python3 /user/scripts/log_parser_notifier.py -d /user/logs -u /user/configs/users.csv -m /user/configs/messages.csv
#CMD python3 /user/scripts/log_parser_notifier.py -d /user/logs_nested -u /user/configs/users.csv -m /user/configs/messages.csv
#CMD python3 /user/scripts/log_parser_notifier.py -d /user/logs_nested -u /user/configs/users2.csv -m /user/configs/messages2.csv

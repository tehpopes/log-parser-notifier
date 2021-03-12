# log-parser-notifier
Python cli tool that reads in ASCII log files and “alert” (i.e. print to standard out) when a log message that a user is subscribed to appears. The directory in which the log files exist is to be passed into the program via command line. This directory has an arbitrary number of subdirectories in which log files may exist.

## Basic Usage
usage: log_parser_notifier.py [-h] -d DIRECTORY -u USERS -m MESSAGES

reads ASCII log files and "alerts" when a log message that a user is subscribed to appears.

arguments:
  -d DIRECTORY, --directory DIRECTORY
                        path to log directory
  -u USERS, --users USERS
                        path to users.csv file
  -m MESSAGES, --messages MESSAGES
                        path to messages.csv file

optional arguments:
  -h, --help            show this help message and exit

## Run on Docker (Ubuntu 18.04)
In root of repo run following:
$ docker build -t {image_name}:{tag} .
$ docker run {image_name}:{tag}

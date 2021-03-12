# Language: Python3
# OS: Ubuntu 18.04

import csv
import argparse
import pathlib
from collections import defaultdict

def parse_input():
  parser = argparse.ArgumentParser(description='reads ASCII log files and "alerts" when a log message that a user is subscribed to appears.')
  parser.add_argument('-d', '--directory', type=pathlib.Path, required=True, help='enter path to log directory')
  parser.add_argument('-u', '--users', type=open, required=True, help='enter path to users.csv file')
  parser.add_argument('-m', '--messages', type=open, required=True, help='enter path to messages.csv file')
  args = parser.parse_args()

  return args.directory, args.users, args.messages

def parse_messages_csv(messages):
  message_to_id_dict = {}

  next(messages) # Skip header row
  for message in csv.reader(messages, delimiter=','):
    message_to_id_dict[message[1]] = int(message[0])

  return message_to_id_dict

def parse_users_csv(users):
  id_to_users_dict = defaultdict(set)

  next(users) # Skip header row
  for user in csv.reader(users, delimiter=','):
    if user[3] != '':
      for id in user[3:]:
        id_to_users_dict[int(id)].add(user[0])

  return dict(id_to_users_dict)

def alert_users(log_file, message_to_id_dict, id_to_users_dict):
  for line in log_file:
    for message, id in message_to_id_dict.items():
      if id in id_to_users_dict and message in line:
        for user in id_to_users_dict[id]:
          print(f'Notifying {user} of {id}! {message}')

def read_logs(directory, id_to_users_dict, message_to_id_dict):
  for log_f in directory.resolve().glob('**/*'):
    if log_f.is_file():
      alert_users(open(log_f,'r'), id_to_users_dict, message_to_id_dict)

if __name__ == '__main__':
  directory, users, messages = parse_input()
  
  message_to_id_dict = parse_messages_csv(messages)
  id_to_users_dict = parse_users_csv(users)
  
  read_logs(directory, message_to_id_dict, id_to_users_dict)   

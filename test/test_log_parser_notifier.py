# Run following in root of repo
# pytest test

import pytest
import subprocess

def test_help():
  out = str(subprocess.check_output(['python3','scripts/log_parser_notifier.py','-h']))
  usage_str = 'usage: log_parser_notifier.py [-h] -d DIRECTORY -u USERS -m MESSAGES' 
  assert usage_str in out

def test_basic_example():
  out = str(subprocess.check_output(['python3','scripts/log_parser_notifier.py','-d','logs/','-u','configs/users.csv','-m','configs/messages.csv']))
  alerts = ['Notifying Bill of 0! Error: build during 2018-12-10 01:02:03 failed!',
            'Notifying Bill of 1! Warning: build of repository did not complete!',
            'Notifying Bill of 2! Invalid build specified for repository \'tyvak\'.',
            'Notifying Jessica of 2! Invalid build specified for repository \'tyvak\'.'] 
  for alert in alerts: 
    assert alert in out

def test_nested_example():
  out = str(subprocess.check_output(['python3','scripts/log_parser_notifier.py','-d','logs_nested/','-u','configs/users.csv','-m','configs/messages.csv']))
  alerts = ['Notifying Bill of 0! Error: build during 2018-12-10 01:02:03 failed!',
            'Notifying Bill of 1! Warning: build of repository did not complete!',
            'Notifying Bill of 2! Invalid build specified for repository \'tyvak\'.',
            'Notifying Jessica of 2! Invalid build specified for repository \'tyvak\'.'] 
  for alert in alerts: 
    assert out.count(alert) == 3

def test_other_nested_example():
  out = str(subprocess.check_output(['python3','scripts/log_parser_notifier.py','-d','logs_nested/','-u','configs/users2.csv','-m','configs/messages2.csv']))
  alerts = ['Notifying Vivek of 1! PROPFIND /svn/[xxxx]/Extranet/branches/SOW-101 HTTP/1.1',
            'Notifying Sam of 1! PROPFIND /svn/[xxxx]/Extranet/branches/SOW-101 HTTP/1.1',
            'Notifying Vivek of 0! Error: build during 2018-12-10 01:02:03 failed!',
            'Notifying Sam of 2! Debug: Could not find specified path.',
            'Notifying Bayley of 0! Error: build during 2018-12-10 01:02:03 failed!']
    
  for alert in alerts: 
    assert out.count(alert) == 3

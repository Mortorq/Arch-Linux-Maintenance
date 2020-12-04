#!/usr/bin/env python

import os
import getpass
import sys
import subprocess
import json

from subprocess import check_call

premade_text = { "new_repo": "Neues Backup-Repository erstellen?",
                 "encrypt_repo": "Backup-Repository verschlüsseln?",
                 "change_repo_path": "Anderen Pfad zum Repo festlegen?",
                 "new_dir": "Zielpfad existiert nicht.\nNeues Verzeichnis erstellen?"}

with open('/home/{}/.config/maint.conf'.format(getpass.getuser()), 'r') as json_conf:
    config = json_conf.read()

config_obj = json.loads(config)

def interact(question, default="yes"):
    valid = { "yes": True, "y": True, "ye": True,
             "no": False, "n": False }

    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("Invalid default value!")
        exit(1)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.wirte("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def check_path(path):
    if os.path.isdir(path) is True:
        return True
    else:
        return False

def create_path(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and check_path(path):
            pass
        else:
            raise

def create_repo(question):
    if question is True:
        while check_path(config_obj['path']) is False:
            if interact(premade_text['new_dir']) is True:
                create_path(config_obj['path'])
            else:
                sys.stdout.write("OK - cannot create new Path.\nBye.")
                exit(0)

        try:
            check_call( [ 'borg init --encryption={0} {1}'.format(config_obj['encryption_method'],
                                                                  config_obj['path']) ], shell=True )
        except subprocess.CalledProcessError:
            pass
        #else:
        #    raise
    elif question is False:
        sys.stdout.write("OK - not doing anything!")
        exit(0)
    else:
        exit(1)
#def create_repo(question):
#    if question is True:
#        if check_path(config_obj['path']) is True:
#            try:
#                check_call( [ 'borg init --encryption={0} {1}'.format(config_obj['encryption_method'],
#                                                                  config_obj['path']) ], shell=True )
#            except subprocess.CalledProcessError:
#                pass
#            else:
#                raise
#        elif check_path(config_obj['path']) is False:
#            if interact(premade_text['new_dir']) is True:
#                create_path(config_obj['path'])
#            else:
#                sys.stdout.write("OK - cannot create new Borg Repository. Bye.")
#                exit(0)
#    elif question is False:
#        sys.stdout.write("OK - not doing anything!")
#        exit(0)
#    else:
#        exit(1)

create_repo(interact(premade_text['new_repo']))



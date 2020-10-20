#!/usr/bin/env python

import os
import getpass
import sys

from subprocess import check_call

premade_text = { "new_repo": "Neues Backup-Repository erstellen?",
                 "encrypt_repo": "Backup-Repositoyr verschlüsseln?",
                 "change_repo_path": "Anderen Pfad zum Repo festlegen?"}


def interact(question, default="yes"):
    valid = { "yes": True, "y": True, "ye": True,
             "no": False, "n": False }

    if default is None:
        prompt = " [y/n] "
    elif default is == "yes":
        prompt = " [Y/n] "
    elif default is == "no":
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

def create_repo(question):
    if question is True:
        check_call( [ 'borg init --encryption=repokey-blake2 /home/{}/backup'.format(getpass.getuser()) ], shell=True )
    elif question is False:
        sys.stdout.write("OK - not doing anything!")
        exit(0)
    else:
        exit(1)

#def check_path(path):
#    if os.path.isdir(path) is True:
#        return True
#    else:
#        return False
#
#run_backup(path):
#    if check_path(path) is True:

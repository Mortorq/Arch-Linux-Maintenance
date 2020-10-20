#!/usr/bin/env python

import getpass
import sys

from subprocess import check_call

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
        raise ValueError("invalid answer")
        exit(0)

    while True:
        sys.stdout.write(question + prompt)
        choice = input().lower()
        if default is not None and choice == '':
            return valid[default]
            print(valid[default])
        elif choice in valid:
            return valid[choice]
            print(valid[choice])
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


if interact("Neues, verschlüsseltes Backup Repository erstellen?", "yes") is True:
    check_call( [ 'borg init --encryption=repokey-blake2 /home/{}/backup'.format(getpass.getuser()) ], shell=True )
else:
    exit(1)

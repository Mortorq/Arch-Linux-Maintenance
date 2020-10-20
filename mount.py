#!/usr/bin/env python

import getpass

from os.path import expanduser
from subprocess import check_call

check_call( [ 'sudo mount -t cifs -o username={0} //172.19.3.5/Cevo/cevo/USER/{0} /home/{0}/backup'.format(getpass.getuser()) ], shell=True )

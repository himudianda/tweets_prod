#!/usr/bin/python
import sys
import logging

# These 2 lines are required if u install python packages inside a virtualenv
activate_this = '/var/www/admin/.venv/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/admin/")

from app import app as application
application.secret_key = 'Add your secret key'

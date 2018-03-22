# RailsAlchemy
# About: Transform raw text into up and running app
# Version: 1.0 - 2018/03/22
# Author: walid.daboubi@gmail.com


import sys
import commands
import os
import random
import string
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
import argparse


# strip colors if stdout is redirected
init(strip=not sys.stdout.isatty())

def gen_random_id(size=10, chars=string.ascii_lowercase + string.digits):
    return 'RailsCharm_generated_app_'+''.join(random.choice(chars) for _ in range(size))

def execute_cmd(cmd):
    result = commands.getstatusoutput(cmd)
    if result[0] == 0:
        return result[1]
    else:
        return 1

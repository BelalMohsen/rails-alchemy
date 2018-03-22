# RailsAlchemy
# About: Transform raw text into up and running app
# Version: 1.0 - 2018/03/22
# Author: walid.daboubi@gmail.com

from utilities import *
from args import *
from alchemy import *

# Welcome message
cprint(figlet_format('RailsAlchemy'),'green')

print 'You app description:'
print args['app_description']
print '\nThe Alchimist is analyzing your requirements..'

entities, actions, roles, all_text_data = get_data_from_text(args['app_description'].split('.'))
gen_app(args['destination_folder'],gen_random_id(),entities,roles)

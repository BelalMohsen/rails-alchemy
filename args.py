
# RailsAlchemy
# Version 1.0 - 2018/03/22
# Contact: walid.daboubi@gmail.com

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--app_description", help="The wanted application requirement", required=True)
parser.add_argument("-d", "--destination_folder", help="The application destination folder", required=True)
parser.add_argument("-e", "--execute", help="Launch the app server once built", required=False, choices = ['yes', 'no'])

args = vars(parser.parse_args())

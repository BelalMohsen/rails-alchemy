# RailsAlchemy
# About: Transform raw text into up and running app
# Version: 1.0 - 2018/03/22
# Author: walid.daboubi@gmail.com

from utilities import *
from editors import *
from args import *
from analyzers import *

def gen_app(dest_path, app_name, entities, roles):
    error_standard = 'Something went wrong'
    # Create the rails app
    result = execute_cmd('rails new {}/{}'.format(dest_path,app_name))
    if result != 1:
        os.chdir('{}/{}'.format(dest_path,app_name))

        # Add devise to the Gemfile
        update_gemfile('.', 'gem \'devise\'')

        print '-> Installing Gems'
        if execute_cmd('bundle install') == 1:
            print '{} installing Gemfile'.format(error_standard)
            sys.exit(1)

        print '-> Installing devise'
        if execute_cmd('rails generate devise:install') == 1:
            print '{} installing devise'.format(error_standard)
            sys.exit(1)

        # Create devise user and add role column
        print '-> Creating devise user..'
        if execute_cmd('rails generate devise User role:string') == 1:
            print '{} creating user table'.format(error_standard)
            sys.exit(1)


        # Generate devise views
        print '-> Creating devise views..'
        if execute_cmd('rails generate devise:views') == 1:
            print '{} creating devise views'.format(error_standard)
            sys.exit(1)

        # Create a scaffold for each model
        for model in entities:
            if model not in roles:
                print '-> Creating a scaffold for '+model
                if execute_cmd('rails g scaffold {} name:string'.format(model)) == 1:
                    print 'Something went wrong generating the model {}'.format(model)
                    sys.exit(1)
        print '-> Adding before action to application controller'
        add_before_action()
        print '-> Adding role options to signup'
        add_role_options(roles)

        print '-> Migrating the database'
        if execute_cmd('rake db:migrate') == 1:
            print 'Something went wrong migrating the database'
            sys.exit(1)


        if args['execute'] == 'yes':
            print '-> Launching rails server'
            if execute_cmd('rails s') == 1:
                print 'Something went wrong launching the server'
                sys.exit(1)
        else:
            print 'Yay! Your application has successfully been built'
            print 'To launch it, run the following commands'
            print '\t$ cd {}/{}'.format(dest_path,app_name)
            print '\t$ rails s'
            print 'And visit http:/0.0.0.0:3000'
            print 'To get your main URLs, run the following command'
            print '\t$ rake routes'
    else:
        print 'Something wen wrong creating the app'
        sys.exit(1)

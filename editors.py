# RailsAlchemy
# About: Transform raw text into up and running app
# Version: 1.0 - 2018/03/22
# Author: walid.daboubi@gmail.com

def update_gemfile(path, update):
    with open('{}/Gemfile'.format(path), 'a') as myfile:
        myfile.write(update)

def add_before_action():
    # Edit application controller and add before action authentication
    controller_file = './app/controllers/application_controller.rb'
    controller_reader = open(controller_file,'r')
    app_controller_lines = controller_reader.readlines()
    controller_reader.close()
    controller_writer = open(controller_file,'w')
    for i in range(0, len(app_controller_lines) - 1):
        controller_writer.write(app_controller_lines[i])
    controller_writer.write('before_action :authenticate_user!')
    controller_writer.write('\nend')

def add_role_options(roles):
    # Edit ./app/views/devise/registrations/new.html.erb and add role
    view_file = './app/views/devise/registrations/new.html.erb'
    view_reader = open(view_file, 'r')
    devise_registration_view_lines = view_reader.readlines()
    view_reader.close
    devise_registration_view_writer = open(view_file, 'w')
    i = 0
    while i < len(devise_registration_view_lines):
        if 'actions' not in devise_registration_view_lines[i]:
            devise_registration_view_writer.write(devise_registration_view_lines[i])
            i+=1
        else:
            break
    role_options = []
    for role in roles:
        role_options.append([role,role])
    devise_registration_view_writer.write('<%= f.select :role, options_for_select({}) %>'.format(str(role_options)))
    while i < len(devise_registration_view_lines):
        devise_registration_view_writer.write(devise_registration_view_lines[i])
        i += 1
    devise_registration_view_writer.close()

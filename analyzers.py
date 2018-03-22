# RailsAlchemy
# About: Transform raw text into up and running app
# Version: 1.0 - 2018/03/22
# Author: walid.daboubi@gmail.com

import nltk
import os

def get_word_definition(word):
    definition = ''
    dictionary = open('{}/dictionary/wb1913_{}.html'.format(os.path.dirname(os.path.realpath(__file__)),word[0]),'r')
    for line in dictionary.readlines():
        if '<P><B>{}</B>'.format(word.title()) in line:
            definition += line
    return definition

def is_it_a_role(definition):
    indicators = ['One who','A person','parent', 'One ']
    rejectors = ['A place']
    this_is_a_role = False
    for indicator in indicators:
        if indicator in definition:
            this_is_a_role = True
            break
    for rejector in rejectors:
        if rejector in definition:
            this_is_a_role = False
            break
    return this_is_a_role

def get_data_from_text(phrases):
    entities, actions, roles, text_data = [], [], [], []
    for phrase in phrases:
        if len(phrase) > 1:
            phrase = phrase.lower()
            phrase_data = {}
            phrase_data['raw'], phrase_data['entities'], phrase_data['actions'], phrase_data['roles'] = phrase, [], [], []
            words = nltk.word_tokenize(phrase)
            for entity in nltk.pos_tag(words):
                # Get singluar from plural
                current_word = entity[0]
                if 'NNS' in entity[1]:
                    current_word = current_word[0:len(current_word) - 1]
                if 'VB' in entity[1] :
                    if current_word not in actions:
                        actions.append(current_word.lower())
                    if current_word not in phrase_data['actions']:
                        phrase_data['actions'].append(current_word.lower())
                if 'NN' in entity[1]:
                    if current_word.lower() not in entities:
                        entities.append(current_word.lower())
                    if current_word.lower() not in phrase_data['entities']:
                        phrase_data['entities'].append(current_word.lower())
                if 'NN' in entity[1] and is_it_a_role(get_word_definition(current_word.lower())):
                    if current_word.lower() not in roles:
                        roles.append(current_word.lower())
                    if current_word.lower() not in phrase_data['roles']:
                        phrase_data['roles'].append(current_word.lower())
            text_data.append(phrase_data)
    return entities, actions, roles, text_data

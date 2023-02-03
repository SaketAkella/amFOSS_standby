from pathlib import Path
import re
import os
filename = input('Enter the name of the template file you wish to use: ')
lib = open('{0}/{1}.txt'.format(os.getcwd(), filename))
string = lib.read()

replaced = 0
madlib_regex = re.compile(r'(NOUN|VERB|ADVERB|ADJECTIVE)')
matches = madlib_regex.findall(string)

for found in matches:
    sub = input('Enter a ' + found + ': ')
    string = string.replace(found, sub, 1)

print(string)


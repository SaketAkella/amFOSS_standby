import re

def strip(string, rm):
    if rm != '':
        strip_regex = re.compile(rm)
        newString = strip_regex.sub('', string)
        return newString
    else:
        strip_regex = re.compile('^\s*')
        newString = strip_regex.sub('', string)
        strip_regex = re.compile('\s*$')
        newString = strip_regex.sub('', newString)
        return newString

string = input('Enter: ')
rm= input('Enter characters to be removed (Press enter for whitepsace)')
newString = strip(string, rm)
print(newString)
import re
def strongPassword(password):
    z=0
    for regex in criterias:
        if regex.search(password) is None:
            print('Password not strong enough..')
            break
        else:
            z+=1
            continue
    if z == 4:
        print('Password strong enough...')

lengthPassword_of_password= re.compile('.{8,}')
lowerCase_in_password = re.compile('[a-z]+')
upperCase_in_password= re.compile('[A-Z]+')
digits_in_password= re.compile('[\d]+')
criterias = [lengthPassword_of_password,
              lowerCase_in_password,
              upperCase_in_password,
              digits_in_password]

password = input('Please type in a password: ')
strongPassword(password)

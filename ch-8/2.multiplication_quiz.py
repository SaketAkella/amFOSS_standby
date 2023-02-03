import pyinputplus as pyip
import random, time

'''
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response= pyip.inputYesNo(prompt)

    if response=='no':
        break
print('Thankyou') '''


numberOfQuestions=10
correctAnswers=0

for questionNumber in range(numberOfQuestions):
    num1=random.randint(0,9)
    num2=random.randint(0,9)
prompt='#%s=%s x %s' %(questionNumber,num1,num2)

try:
    pyip.inputStr(allowRegexes=['^#%s' % (num1 * num2)], blockRegexes=['.*', 'Incorrect!'], timeout=10, limit=3)

except pyip.TimeoutException:
    print('You\'ve run of out of time')
except pyip.RetrylimitException:
    print('You\'ve run of entries')

else: 
    print('correct')
    correctAnswers+=1

time.sleep(1)
print('Score %s/%s'%(correctAnswers, numberOfQuestions))

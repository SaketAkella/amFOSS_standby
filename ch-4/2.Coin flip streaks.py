import random
numberOfStreaks = 0
x=[]
t=0
h=0
for experimentNumber in range(10000):
    for i in range(100):
        x.append(random.randit(0,1))

    for j in range(len(x)):
        if (x[j]==1):
            h=+1
        if(x[j]==0):
            t=+1
        if(h==6 or t==6):
            h=0
            t=0
            numberOfStreaks+=1
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
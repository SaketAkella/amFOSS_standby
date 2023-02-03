import re
import calendar

dateRegex=re.compile(r'^([0-3]/d)\/([0-1])')

def datefind(text):
    n=0
    heh=re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    reg=heh.search(text)
    date=int(reg.group(1))
    month=int(reg.group(2))
    year=int(reg.group(3))
    if date in range(1,32) and month in range(1,13) and year in range(1000,3000):
        if month==4 or  month==6 or month==9 or month==11 and date in range(1,31):
            print("Valid")
            n=n+1
        if month==2 and date in range(0,30):
            if year%4==0 and date in range(0,30):
                print("Valid")
                n+=1
            elif date in range(0,29):
                print("Valid")
                n+=1
        if month==1 or  month==3 or month==5 or month==7 or month==8 or month==10 or month==12 and date in range(1,32):
            print("Valid")
            n+=1
    if n==0:
        print("Not Valid")

inp=input("> ")
datefind(inp)

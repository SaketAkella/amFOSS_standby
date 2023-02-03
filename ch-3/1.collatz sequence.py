global n
def collatz(number):
        if (number%2==0):
            n= number//2
            print(n)
            return n
        elif (number%2!=0):
            n= 3*number+1
            print(n)
            return n    
            
print("Enter a number:")

try:
    number=int(input())
    while n!=1:
        n=number
        collatz(number)
except ValueError:
    print("Invalid entry!")

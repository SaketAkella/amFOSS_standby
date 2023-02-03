def items():
    x=list(input('Enter items: ').split())
    if(len(x)==0):
        print('Given list has no values')
    
    for i in range(len(x)):
        if (x[i]!=x[len(x)-1] and x[i]!=x[len(x)-2]):
            print(x[i], end=" , ")
        if (x[i]==x[len(x)-2]):
            print(x[i], end="and ")
        if (x[i]==x[len(x)-1]):
            print(x[i])

items()

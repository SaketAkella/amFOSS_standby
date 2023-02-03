import pyinputplus as pyip

price={'wheat':1, 'white':2, 'sour-dough': 3,
         'chicken':1, 'turkey':2, 'ham':3, 'tofu':4,
         'cheddar':1, 'swiss':2, 'mozzarella':3,
         'mayo':1, 'lettuce':2,'mustard':3, 'ketchup':4}
bill=0

while True:
    bread=pyip.inputMenu(['wheat','white','sour-dough'],
           prompt='Please enter your bread type: \n')
    protein=pyip.inputMenu(['chicken','turkey','ham','tofu'], 
           prompt='Please enter your protein type: \n')
    #add-ons:
    cheese=pyip.inputYesNo('Do you want cheese in your sandwich? \n')
    if cheese=='yes':
        cheeseType=pyip.input(['cheddar','swiss','mozzarella'])
    if cheeseType==item:
        print(f'{item}={price}')
        bill+=price
    mayo= pyip.inputYesNo('Do you want mayo in your sandwich? \n')
    if mayo=='yes':
        print(f'{item}={price}')
        bill+=price
    lettuce= pyip.inputYesNo('Do you want lettuce in your sandwich? \n')
    if lettuce=='yes':
        print(f'{item}={price}')
        bill+=price
    mustard= pyip.inputYesNo('Do you want mustard in your sandwich? \n')
    if mustard=='yes':
        print(f'{item}={price}')
        bill+=price
    ketchup= pyip.inputYesNo('Do you want ketchup in your sandwich? \n')
    if mustard=='yes':
        print(f'{item}={price}')
        bill+=price
    
    count=pyip.input(prompt='Enter number of sandwiches: \n', min=1)    
    print(f'Each sandwich cost X sandwich count={bill}*{count}=' f'{bill*count}')

    break


    
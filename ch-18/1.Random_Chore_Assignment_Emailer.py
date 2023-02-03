import ezgmail,random
email=['karriabhinav15@gmail.com','saketakella37@gmail.com','sachinshreekumarquora@gmail.com']
chores=['Wash Clothes','Sweeping','Dishes']

variety_check={'karriabhinav15@gmail.com':'Clean room','saketakella37@gmail.com' :'Sweeping'}

for i in range(len(email)):
    randomchore=random.choice(chores)
    chores.remove(randomchore)
    ezgmail.send(email[i],'This is to inform you about your chore',f'Your chore for the week is {randomchore}')
    variety_check.setdefault(email[i],randomchore)


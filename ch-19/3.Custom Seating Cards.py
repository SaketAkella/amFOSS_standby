from PIL import Image,ImageFont,ImageDraw

file=open('guests.txt')
names=file.readlines()

for i in names:
    inv=i[:-1]
    im = Image.new('RGBA', (288, 360),'white')
    image=Image.open('flower.png')
    image=image.resize((288,360))
    im.paste(image,(0,0))

    draw=ImageDraw.Draw(im)
    draw.text((8,250),'It would be a pleasure to have the company of',fill='blue')
    draw.text((130,270),inv,fill='blue')
    draw.text((39,290),'at 11010 Memory Lane on April 1st',fill='blue')
    draw.rectangle((2,2,285,355),outline='yellow')

    im.save(f'{inv}sinvitation.png')
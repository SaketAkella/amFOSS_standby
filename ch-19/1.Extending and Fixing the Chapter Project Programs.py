import os
from PIL import Image

size = 300
logo= 'catlogo.png'

logo = Image.open(logo)
logoWidth, logoHeight = logo.size

os.makedirs('withLogo', exist_ok=True)

for filename in os.listdir('.'):
    if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
            or filename.lower().endswith('.gif') or filename.lower().endswith('bmp')) \
            or filename == logo:
        continue

    im = Image.open(filename)
    width, height = im.size


    if width > size and height > size:

        if width > height:
            height = int((size / width) * height)
            width = size
        else:
            width = int((size / height) * width)
            height = size


    print('Resizing {}...'.format(filename))
    im = im.resize((width, height))
    width, height = im.size
    if width < logoWidth * 2 or height < logoHeight * 2:
        '''print("The logo wouldn't look good on an image this size so "
              "it is being skipped. The unadorned image will still be saved "
              "to the 'withLogo' directory.")'''
    else:
        print('Adding logo to {}...'.format(filename))
        im.paste(logo, (width - logoWidth, height - logoHeight), logo
    )
    im.save(os.path.join('withLogo', filename))
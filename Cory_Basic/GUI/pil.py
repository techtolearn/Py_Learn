'''https://www.youtube.com/watch?v=6Qs3wObeWwc&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=61
Image Manipulation with Pillow
'''

from PIL import Image,ImageFilter
import os


# image1 = Image.open('Tanvi.jpg')
# image1.save('Tanvi.png')

#image conversion from jpg to png
# for f in os.listdir('.'): #it search from current directory
#     if f.endswith('jpg'):
#         i = Image.open(f)
#         fn, fextn = os.path.splitext(f)
#         #print(fn,' ',fextn)
#         i.save('png/{}.png'.format(fn))  #it will save the jpg into png under the png folder

#save with particular pixel
# size_300 = (300,300)
# for f in os.listdir('.'): #it search from current directory
#     if f.endswith('jpg'):
#         i = Image.open(f)
#         fn, fextn = os.path.splitext(f)
#         i.thumbnail(size_300)
#         i.save('300/{}_300{}'.format(fn,fextn))  #it will save the jpg into png under the png folder


# image1 = Image.open('Tanvi.jpg')
# #image1.rotate(90).save('Tanvi1.jpg')
# image1.convert(mode='L').save('Tanvi2.jpg')  #black white conversion

image1 = Image.open('cast_Add.jpg')
image1.filter(ImageFilter.GaussianBlur()).save('cast_Add1.jpg')  #blur the image



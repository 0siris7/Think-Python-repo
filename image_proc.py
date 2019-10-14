#Flipping an image
"""This here is a image inversion programs"""
from PIL import Image

img = Image.open('inverted.png') #open image
#Transpose or flip
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)  #Bunch of matrix

#Convert to understandable format

transposed_img.save('Reinverted.png')


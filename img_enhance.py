""" Here is a program to enhance a program"""

import cv2
#open image
img = cv2.imread("inverted.png") #CLAHE contrast limited adaptive histogram equilization

#Prep for CLAHE
clahe = cv2.createCLAHE()

#convert to grey scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#enhancement
enhanced = clahe.apply(gray)
recolor = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)
cv2.imwrite('enhanced.png', recolor)
print("DONE")
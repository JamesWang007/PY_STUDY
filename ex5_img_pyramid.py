# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
## - Load an image
## - 3 ways


# image path
img_path_01 = 'd:/MyData/imgs/cv_img_01.jpg'

#image folder
img_folder = 'd:/MyData/imgs/img_h_01'

# way 1 - using matplotlib.image

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('d:/MyData/imgs/cv_img_01.jpg')
plt.figure()
imgplot = plt.imshow(img)
plt.show()



# not working
# way 2 - using Image
from PIL import Image

image = Image.open('d:/MyData/imgs/cv_img_01.jpg')
image.show()



# way 3 - using cv2
import cv2
import matplotlib.pyplot as plt

im = cv2.imread(img_path_01)
#im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)

plt.imshow(cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
plt.show()


## - load files from a directory
## - use some multithreading
## - 

# - using multiprocessing
from multiprocessing import Pool
import os

path1 = img_folder
path2 = img_folder

listing = os.listdir(path1)

p = Pool(5) # process 5 images simultaneously

def process_fpath(path):
    im = Image.open(path1 + path)
    im.resize((50, 50))     # NEED TO DO SOME MORE PROCESSING HERE
    im.save(os.path.join(path2, path), "JPEG")
    
p.map(process_fpath, listing)



# - use glob to read the images one by one w/o knowing the name
import glob
from PIL import Image
import random

images = glob.glob(img_folder+"/*")
for image in images:
    img = Image.open(image)
    img1 = img.resize((50, 50))
    img1.save(img_folder+"/newfolder/" + str(random.randrange(100)) + ".jpg")



# load images files from a folder one by one w/o knowing the name
import time
    
for image in images:
    img = Image.open(image)
    img.show()
    time.sleep(0.5)

































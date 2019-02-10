# -*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

#       0
img = cv2.imread ("images/Lenna.png", cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_UNCHANGED = -1

#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
# nothing ~haha
plt.imshow(img, cmap='gray')
plt.plot([50, 100], [80, 100], 'c', linewidth = 5)
plt.show()

cv2.imwrite('images/myLenna.png', img)

# --- also work
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



img = cv2.imread('images/Lenna.png', -1)
rows,cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)
dst = cv2.warpAffine(img,M,(cols,rows))

plt.imshow(M)
plt.show()    

plt.imshow(img)
plt.show()    

plt.imshow(dst)
plt.show()
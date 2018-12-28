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

plt.imshow(img, cmap='gray')
plt.plot([50, 100], [80, 100], 'c', linewidth = 5)
plt.show()

cv2.imwrite('images/myLenna.png', img)
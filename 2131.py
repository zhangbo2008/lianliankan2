import cv2
aa=cv2.imread('fordebug/0_0.png')
import numpy as np
bb=np.sum(aa==np.zeros_like(aa))>np.size(aa)*0.8
print(21)
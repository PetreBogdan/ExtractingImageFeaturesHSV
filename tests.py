import scipy
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from skimage.io import imshow, imread
from scipy import misc
import scipy.misc
from PIL import Image
import cv2

img = imread("F:\Projects\MEDH_projects\ExtractingImageFeaturesHSV\EuroSAT\\2750\AnnualCrop\AnnualCrop_1.jpg")

array=np.asarray(img)
# arr=(array.astype(float))/255.0
img_hsv = colors.rgb_to_hsv(array)
#
# lu1=img_hsv[...,0].flatten()
# plt.hist(lu1*360,bins=360,range=(0.0,360.0),histtype='stepfilled', label='Hue')
# plt.title("Hue")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.legend()
# plt.show()

print(img.shape)                                                                                           
h, _, _ = cv2.split(img_hsv)
print(h.shape)
# # h_histogram = np.zeros(360)
# # for i in h:                                          
# #     print(i)
# #     h_histogram[i] += 1
# # print(h_histogram)
# print(h)








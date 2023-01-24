import scipy
from scipy import ndimage
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
from skimage.io import imshow, imread
from scipy import misc
import scipy.misc
from PIL import Image

# img = imread("E:\Projects\ExtractingImageFeaturesHSV\VOCdevkit\VOC2007\JPEGImages\\000020.jpg")
img_pil = Image.open("E:\Projects\ExtractingImageFeaturesHSV\VOCdevkit\VOC2007\JPEGImages\\000023.jpg")
new_img = img_pil.resize((256, 256))
img = np.array(new_img)
img_hsv = colors.rgb_to_hsv(img[...,:3])
(hist, _) = np.histogram(img_hsv.ravel(), bins=np.arange(0,128+1), range=(0,128))
hist = hist.astype("float")
hist /= (hist.sum() + 1e-6)

print(hist)

# array=np.asarray(img)
# arr=(array.astype(float))/255.0
# img_hsv = colors.rgb_to_hsv(arr[...,:3])
#
# lu1=img_hsv[...,0].flatten()
# plt.hist(lu1*360,bins=360,range=(0.0,360.0), label='Hue')
# plt.title("Hue")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.legend()
# plt.show()
#
# print(lu1)
# print(len(lu1))


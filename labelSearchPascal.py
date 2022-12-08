import os
from xml.etree import ElementTree
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imshow, imread
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn import ensemble
from sklearn.metrics import accuracy_score
import cv2
from sklearn.multiclass import OneVsRestClassifier


annotations_path = "F:\Projects\MEDH_projects\DatabasesConstructor\VOCdevkit\VOC2007\Annotations"
images_path = "F:\Projects\MEDH_projects\DatabasesConstructor\VOCdevkit\VOC2007\JPEGImages"
segmentation_path = "F:\Projects\MEDH_projects\DatabasesConstructor\VOCdevkit\VOC2007\SegmentationClass"
# dataset_dict = {}
#
#
# file_path = os.path.join(annotations_path, "000001.xml")
# dom = ElementTree.parse(file_path)
# objects = dom.findall("object")
# for object in objects:
#     if len(objects) == 1:
#         object_label = object.find("name").text
#     elif object.find("truncated").text == "1":
#         continue
#     else:
#         object_label = object.find("name").text
#         break
#
#
# print(object_label)



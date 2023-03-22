import os
import shutil

import cv2

# class_name = ['black-pin', 'blister-fold', 'breakage', 'break-pin',
#               'curved-pin', 'dirt', 'empty-blister', 'loss-packaging',
#               'multi-pin', 'ok', 'other', 'outplace-pin', 'poor-packaging',
#               'skewing-pin']
#
# for c in class_name:
#     print(r"D:\Download\云龙数据集\V_1.0.1\{}".format(c) + r"\json")

# img = cv2.imread('D:/Download/yunlong/V_1.0.1/black-pin/bmp/955.bmp')
# print(img)

# class_name = ['black-pin', 'blister-fold', 'breakage', 'break-pin',
#               'curved-pin', 'dirt', 'empty-blister', 'loss-packaging',
#               'multi-pin', 'outplace-pin', 'poor-packaging',
#               'skewing-pin']
# # class_name = ['empty-blister']
# for c in class_name:
# IMAGE_INPUT_PATH = r"D:\Download\yunlong\V_1.0.1\{}".format(c) + r"\bmp"
# XML_INPUT_PATH = r"D:\Download\yunlong\V_1.0.1\{}".format(c) + r"\xml"
IMAGE_PATH = r'D:\ProjectG\yolox37\datasets\VOCdevkit\VOC2007\JPEGImages'
XML_PATH = r'D:\ProjectG\yolox37\datasets\VOCdevkit\VOC2007\Annotations'
xmllist = os.listdir(IMAGE_PATH)
imglist = os.listdir(XML_PATH)

# print(c)
xml = []
for i in xmllist:
    i = i.split('.')[0]
    xml.append(i)
    # print(len(xml))

for i in imglist:
    img = i.split('.')[0]
    if img not in xml:
        print(i)
        # shutil.move(IMAGE_PATH + r"\{}".format(i), r"D:\Download\yunlong\V_1.0.1\{}".format(c))




import os
import numpy as np
import cv2
from PIL import Image, ImageEnhance
import math
from skimage import measure
import cv2
import numpy as np


img = Image.open("190.png")
# img = Image.open("1.jpg")
img = np.array(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray,3)
# Image.fromarray(gray).show()
images1 = gray[:400, :]
images2 = gray[400:, :]

clahe = cv2.createCLAHE(clipLimit=50, tileGridSize=(8, 8))
gray = clahe.apply(images1)
gray = cv2.medianBlur(gray, 5)
# Image.fromarray(gray).show()

means, dev = cv2.meanStdDev(gray)
print(means, dev)
dt = dev / 3
# tl = 1 * dt
th = means - 2 * dev
th = th + 5 * dt
print(th)
# Image.fromarray(gray).show()
ret, binary = cv2.threshold(gray, int(th), 255, cv2.THRESH_BINARY_INV)
# Image.fromarray(binary).show()

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opened = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)
Image.fromarray(opened).show()

num_objects, labels = cv2.connectedComponents(opened)
# res = remove_small_points(opened, 1)
# Image.fromarray(res).show()
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(3, 3))
# NpKernel = np.uint8(np.ones((3,3)))
# Nperoded = cv2.erode(binary,NpKernel)
# Image.fromarray(Nperoded).show()



#
# def img_processing(img):
#     # 灰度化
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     ret, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_OTSU)
#     # canny边缘检测
#     Image.fromarray(binary).show()
#     edges = cv2.Canny(binary, 10, 200, apertureSize=1)
#     return edges
#
#
# def line_detect(img):
#     img = Image.open(img)
#     img = ImageEnhance.Contrast(img).enhance(3)
#     # img.show()
#     img = np.array(img)
#     result = img_processing(img)
#     # 霍夫线检测
#     lines = cv2.HoughLinesP(result, 1, 1 * np.pi / 180, 10, minLineLength=10, maxLineGap=5)
#     # print(lines)
#     print("Line Num : ", len(lines))
#
#     # 画出检测的线段
#     for line in lines:
#         for x1, y1, x2, y2 in line:
#             cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)
#         pass
#     img = Image.fromarray(img, 'RGB')
#     # img.show()
#
#
# if __name__ == "__main__":
#     line_detect("1.png")
#     pass

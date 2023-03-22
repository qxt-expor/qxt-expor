# 颜色阈值分割
import math
import os
import random
from tqdm import tqdm

import cv2
import numpy as np
import sys

from learning.data_pre_process.triangle_detect import detect_circle_single
img_path = 'D:/Download/2022-12-19/2022-12-19/1-1/'
save_path = 'D:/Download/2022-12-19/2022-12-19/make/'
for img_name in tqdm(os.listdir(img_path)):

    img_ori = cv2.imread(os.path.join(img_path, img_name))
    img = cv2.bilateralFilter(img_ori, 9, 75, 75)
    h, w, _ = img.shape
    img_zero = np.zeros_like(img)
    # img_zero = img[]
    low_blue = np.array([94, 68, 88])
    high_blue = np.array([118, 255, 155])
    img_BGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, low_blue, high_blue)
    mask = cv2.bitwise_not(mask, mask)
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=35, minRadius=0, maxRadius=0)
    circles = circles[0, :, :]
    x, y, r = np.uint16(np.around(circles))[0]
    for i in range(h):
        for j in range(w):
            lx = abs(i - y)  # 到圆心距离的横坐标
            ly = abs(j - x)  # 到圆心距离的纵坐标
            l = math.sqrt(pow(lx, 2) + pow(ly, 2))  # 三角函数 半径
            if l > r - 25:
                mask[i, j] = 0
    # cv2.circle(mask, (x, y), r, (64, 58, 50), 5)
    # cv2.circle(mask, (x, y), 10, (64, 58, 50), 3)
    # mask = cv2.bitwise_and(img_ori, img_ori, mask=roi)# + cv2.bitwise_and(mask, mask, mask=~roi)
    n = random.randint(3, 8)
    m = random.randint(3, 8)
    t = random.choice([-1, 1])
    M = np.float32([[1, 0, n * t], [0, 1, m * t]])
    dst = cv2.warpAffine(mask, M, (w, h))
    dst[mask == 255] = 0
    # cv2.imshow('mask_', dst)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    dst = cv2.merge([dst, dst, dst * 10])
    img_add = cv2.addWeighted(img_ori, 0.9, dst, 0.1, 0)
    cv2.imwrite(os.path.join(save_path, img_name), img_add)
    # cv2.imshow('mask', mask)
    # cv2.imshow('mask_', dst)
    # cv2.imshow('mask_', img_add)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()


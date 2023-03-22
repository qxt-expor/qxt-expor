# -*- encoding: utf-8 -*-
import os
import json
import cv2
from pathlib import Path
import shutil
import math
from PIL import Image

import numpy as np

if __name__ == '__main__':
    #  文件夹目录
    # file_dir = r'D:\Download\yunlong\real_img\new'
    # output_dir = r'D:\Download\yunlong\real_img\resize'
    file_dir = r'D:\Download\yunlong\V_1.0.1_2\skewing-pin\long'
    output_dir = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\yunlong_backup\v3\test\skewing_pt'

    json_files = os.listdir(file_dir)
    json_dict = {}
    for json_file in json_files:

        #  只获取json文件
        if json_file[-3:] != 'bmp':
            continue
        jsonfile = file_dir + '/' + json_file
        outputfile = output_dir + '/' + json_file
        #outputfile = output_dir + '/25-' + json_file

        # 读取图像1
        img1 = cv2.imread(jsonfile, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(jsonfile)

        ret, dstImage = cv2.threshold(img1, 100, 255, cv2.THRESH_BINARY)
        dstImage = cv2.GaussianBlur(dstImage, (5, 5), 1.0)

        contours, hierarchy = cv2.findContours(dstImage, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = list(contours)
        contours.sort(key=lambda c: cv2.contourArea(c), reverse=True)
        rect = cv2.minAreaRect(contours[0])
        box = np.int0(cv2.boxPoints(rect))
        num = len(box)
        scal_data = []
        for i in range(num):
            x1 = box[(i) % num][0] - box[(i - 1) % num][0]
            y1 = box[(i) % num][1] - box[(i - 1) % num][1]
            x2 = box[(i + 1) % num][0] - box[(i) % num][0]
            y2 = box[(i + 1) % num][1] - box[(i) % num][1]

            d_A = (x1 ** 2 + y1 ** 2) ** 0.5
            d_B = (x2 ** 2 + y2 ** 2) ** 0.5

            Vec_Cross = (x1 * y2) - (x2 * y1)
            if (d_A * d_B == 0):
                continue
            sin_theta = Vec_Cross / (d_A * d_B)
            if (sin_theta == 0):
                continue
            dv = 200 / sin_theta

            v1_x = (dv / d_A) * x1
            v1_y = (dv / d_A) * y1

            v2_x = (dv / d_B) * x2
            v2_y = (dv / d_B) * y2

            PQ_x = v1_x - v2_x
            PQ_y = v1_y - v2_y

            Q_x = box[(i) % num][0] + PQ_x
            Q_y = box[(i) % num][1] + PQ_y
            scal_data.append([Q_x, Q_y])
        box = np.int0(scal_data)  # box

        orignal_H = 0
        orignal_W = 0
        pts1 = np.float32([box[0], box[1], box[2], box[3]])
        if (box[0][0] < box[2][0]):
            # 获取画框宽高(x=orignal_W,y=orignal_H)
            orignal_H = math.ceil(np.sqrt((box[3][1] - box[2][1]) ** 2 + (box[3][0] - box[2][0]) ** 2))
            orignal_W = math.ceil(np.sqrt((box[3][1] - box[0][1]) ** 2 + (box[3][0] - box[0][0]) ** 2))
            # 原图中的四个顶点,与变换矩阵
            pts1 = np.float32([box[0], box[1], box[2], box[3]])
        else:
            # 获取画框宽高(x=orignal_W,y=orignal_H)
            orignal_W = math.ceil(np.sqrt((box[3][1] - box[2][1]) ** 2 + (box[3][0] - box[2][0]) ** 2))
            orignal_H = math.ceil(np.sqrt((box[3][1] - box[0][1]) ** 2 + (box[3][0] - box[0][0]) ** 2))
            # 原图中的四个顶点,与变换矩阵
            pts1 = np.float32([box[1], box[2], box[3], box[0]])
        pts2 = np.float32([[0, int(orignal_H)], [0, 0], [int(orignal_W), 0], [int(orignal_W), int(orignal_H)]])

        # 生成透视变换矩阵；进行透视变换
        M = cv2.getPerspectiveTransform(pts1, pts2)
        result_img = cv2.warpPerspective(img2, M, (int(orignal_W + 3), int(orignal_H + 1)))
        if result_img.shape[1] < result_img.shape[0]:
            img = Image.fromarray(result_img)
            # img.show()
            img = img.rotate(-90, expand=1)
            img.resize((result_img.shape[0], result_img.shape[1]))
            # img.show()
            result_img = np.array(img)
        w = int(result_img.shape[1])
        h = int(result_img.shape[0])
        x = int((2448 - w) / 2)
        y = int((2048 - h) / 2)

        dstImage = cv2.copyMakeBorder(result_img, y, y, x, x, cv2.BORDER_CONSTANT, (0, 0, 0))
        transed_dstImage = cv2.resize(dstImage, (2448, 2048))

        cv2.imwrite(outputfile, transed_dstImage)


    cv2.waitKey(0)
    cv2.destroyAllWindows()
    print('OK!')

# coding=utf-8
import math
import pathlib
import time

import cv2
import numpy as np
import main


def detect_circle_single(source_file, target_file):
    """
    识别图像中的圆形并裁切出相应的矩形保存到目标文件中
    source_file:源文件
    target_file:生成后的文件
    """
    bias = 20
    img = cv2.imread(source_file)
    h, w, _ = img.shape
    # img = cv2.resize(img, (int(w / 2), int(h / 2)))
    # h, w, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 灰度图像
    gray = cv2.GaussianBlur(gray, (5, 5), 5)  # 模糊图像转低分辨率

    # cv2.imshow("fdga",gray)
    # cv2.waitKey()
    circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 5, param1=100, param2=100)
    try:  # 如果上一步没有检测到。执行try内容，就会报错。可以修改尝试看下。
        circles = circles1[0, :, :]  # 提取为二维
    except TypeError:
        print('未发现圆形物体！！', source_file)
    else:
        x, y, r = np.uint16(np.around(circles))[0]  # 四舍五入
        x0 = 0 if x < r + bias else x - r - bias
        y0 = 0 if y < r + bias else y - r - bias
        x1 = x + r + bias
        y1 = y + r + bias
        x1 = x1 if x1 < w else w
        y1 = y1 if y1 < h else h
        # img_t = np.ones_like(img)
        # for i in range(h):
        #     for j in range(w):
        #         if math.sqrt(math.pow(i - y, 2) + math.pow(j - x, 2)) < r:
        #             img_t[i, j] = img[i, j]
        img = img[y0:y1, x0:x1]
        # cv2.circle(img, (x, y), r, (0, 0, 255), 5)
        print(target_file)
    cv2.imwrite(target_file, img)


if __name__ == "__main__":
    # source_dir = r'D:\Download\2022-12-19\2022-12-19\1-1\1'
    source_dir = r'D:\Download\2022-12-19\trains'
    target_dir = 'D:/Download/2022-12-19/2022-12-19/new_make'
    # source_dir = r"img"
    # target_dir = r"img_circle"
    count = 0
    files_iter = pathlib.Path(source_dir).iterdir()
    a = time.time()
    for file in files_iter:
        # print(file)
        detect_circle_single(str(file), target_dir + "/" + file.name)
        count += 1
    # detect_circle_single(source_dir+"/test.jpg", target_dir + "/test.jpg")
    b = time.time()
    print("消耗时间：", b - a, "总数目：", count)
    # detect_circle_single()

"""
dp，用来检测圆心的累加器图像的分辨率于输入图像之比的倒数，且此参数允许创建一个比输入图像分辨率低的累加器。上述文字不好理解的话，来看例子吧。例如，如果dp= 1时，累加器和输入图像具有相同的分辨率。如果dp=2，累加器便有输入图像一半那么大的宽度和高度。
minDist，为霍夫变换检测到的圆的圆心之间的最小距离，即让我们的算法能明显区分的两个不同圆之间的最小距离。这个参数如果太小的话，多个相邻的圆可能被错误地检测成了一个重合的圆。反之，这个参数设置太大的话，某些圆就不能被检测出来了。
param1，有默认值100。它是method设置的检测方法的对应的参数。对当前唯一的方法霍夫梯度法，它表示传递给canny边缘检测算子的高阈值，而低阈值为高阈值的一半。
param2，也有默认值100。它是method设置的检测方法的对应的参数。对当前唯一的方法霍夫梯度法，它表示在检测阶段圆心的累加器阈值。它越小的话，就可以检测到更多根本不存在的圆，而它越大的话，能通过检测的圆就更加接近完美的圆形了。
minRadius，默认值0，表示圆半径的最小值。
maxRadius，也有默认值0，表示圆半径的最大值
"""

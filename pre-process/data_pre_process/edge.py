# Sobel边缘检测算子
import os
import cv2
img = cv2.imread('s-61CE7B72-0034-filek-img.jpg', 0)#转化为灰度图
x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
# cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
# 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
Scale_absX = cv2.convertScaleAbs(x)  # convert 转换  scale 缩放
Scale_absY = cv2.convertScaleAbs(y)
result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
cv2.namedWindow("result",0);#可调大小
cv2.namedWindow("1",0);#可调大小
cv2.imshow('1', img)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

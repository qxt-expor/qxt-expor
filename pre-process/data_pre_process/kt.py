import cv2
import numpy as np

img = cv2.imread('s-61CE7B72-0034-filek-img.jpg', cv2.IMREAD_GRAYSCALE)
img=cv2.GaussianBlur(img,(15,15),3)
dst = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 43, 0.15)
# 手动膨胀腐蚀
k = np.ones((6, 6), np.uint8)
pengzhang_source = cv2.dilate(dst, kernel=k)
fushi_pengzhang_source = cv2.erode(pengzhang_source, kernel=k)
# 调包
morph_open = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel=k)

cv2.imshow("image", img)
cv2.imshow('thresh_out', morph_open)
cv2.waitKey(0)
cv2.destroyAllWindows()

# x = cv2.Sobel(dst, cv2.CV_16S, 1, 0)
# y = cv2.Sobel(dst, cv2.CV_16S, 0, 1)
# # cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])
# # 可选参数alpha是伸缩系数，beta是加到结果上的一个值，结果返回uint类型的图像
# Scale_absX = cv2.convertScaleAbs(x)  # convert 转换  scale 缩放
# Scale_absY = cv2.convertScaleAbs(y)
# result = cv2.addWeighted(Scale_absX, 0.5, Scale_absY, 0.5, 0)
# cv2.namedWindow("result",0);#可调大小
# cv2.namedWindow("1",0);#可调大小
# cv2.imshow('1', img)
# cv2.imshow('result', result)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import math
# import numpy as np
#
#
# def caleGrayHist(image):
#     # 灰度图像的高、宽
#     rows, cols = image.shape
#     # 存储灰度直方图
#     grayHist = np.zeros([256], np.uint64)  # 图像的灰度级范围是0~255
#     for r in range(rows):
#         for c in range(cols):
#             grayHist[image[r][c]] += 1
#
#     return grayHist
#
#
# def threshEntropy(image):
#     rows, cols = image.shape
#     # 求灰度直方图
#     grayHist = caleGrayHist(image)
#     # 归一化灰度直方图，即概率直方图
#     normGrayHist = grayHist / float(rows * cols)
#
#     # 第一步：计算累加直方图，也成为零阶累矩阵
#     zeroCumuMoment = np.zeros([256], np.float32)
#     for k in range(256):
#         if k == 0:
#             zeroCumuMoment[k] = normGrayHist[k]
#         else:
#             zeroCumuMoment[k] = zeroCumuMoment[k - 1] + normGrayHist[k]
#     # 第二步：计算各个灰度级的熵
#     entropy = np.zeros([256], np.float32)
#     for k in range(256):
#         if k == 0:
#             if normGrayHist[k] == 0:
#                 entropy[k] = 0
#             else:
#                 entropy[k] = - normGrayHist[k] * math.log10(normGrayHist[k])
#         else:
#             if normGrayHist[k] == 0:
#                 entropy[k] = entropy[k - 1]
#             else:
#                 entropy[k] = entropy[k - 1] - normGrayHist[k] * math.log10(normGrayHist[k])
#     # 第三步：找阈值
#     fT = np.zeros([256], np.float32)
#     ft1, ft2 = 0.0, 0.0
#     totalEntropy = entropy[255]
#     for k in range(255):
#         # 找最大值
#         maxFront = np.max(normGrayHist[0:k + 1])
#         maxBack = np.max(normGrayHist[k + 1:256])
#         if maxFront == 0 or zeroCumuMoment[k] == 0 or maxFront == 1 or zeroCumuMoment[k] == 1 or totalEntropy == 0:
#             ft1 = 0
#         else:
#             ft1 = entropy[k] / totalEntropy * (math.log10(zeroCumuMoment[k]) / math.log10(maxFront))
#         if maxBack == 0 or 1 - zeroCumuMoment[k] == 0 or maxBack == 1 or 1 - zeroCumuMoment[k] == 1:
#             ft2 = 0
#         else:
#             if totalEntropy == 0:
#                 ft2 = (math.log10(1 - zeroCumuMoment[k]) / math.log10(maxBack))
#             else:
#                 ft2 = (1 - entropy[k] / totalEntropy) * (math.log10(1 - zeroCumuMoment[k]) / math.log10(maxBack))
#         fT[k] = ft1 + ft2
#
#     # 找到最大值索引
#     threshLoc = np.where(fT == np.max(fT))
#     thresh = threshLoc[0][0]
#     # 阈值处理
#     threshold = np.copy(image)
#     threshold[threshold > thresh] = 255
#     threshold[threshold <= thresh] = 0
#
#     return (thresh, threshold)
#
#
# img = cv2.imread('s-61CE7B72-0034-filek-img.jpg', cv2.IMREAD_GRAYSCALE)
# the, dst = threshEntropy(img)
# the1 = 0
# maxval = 150
# the1, dst1 = cv2.threshold(img, the1, maxval, cv2.THRESH_TRIANGLE + cv2.THRESH_BINARY)
# print('The thresh is :', the)
# print('The thresh1 is :', the1)
# cv2.imshow("image", img)
# cv2.imshow('thresh_out', dst)
# cv2.imshow('thresh_out1', dst1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



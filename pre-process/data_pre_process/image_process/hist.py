import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
calcHist-计算图像直方图
函数原型：calcHist(images,channels,mask,histSize,ranges,hist=None,accumulate=None)
images：图像矩阵，例如：[image]
channels：通道数，例如：0
mask：掩膜，一般为：None
histSize：直方图大小，一般等于灰度级数
ranges：横轴范围
'''

# 获取灰度图像
img = cv2.imread("2.bmp", 0)

# 灰度图像的直方图
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.figure()#新建一个图像
plt.title("Grayscale Histogram")
plt.xlabel("Bins")#X轴标签
plt.ylabel("# of Pixels")#Y轴标签
plt.plot(hist)
plt.xlim([0,256])#设置x坐标轴范围
plt.show()


'''
equalizeHist—直方图均衡化
函数原型： equalizeHist(src, dst=None)
src：图像矩阵(单通道图像)
dst：默认即可
'''
# 灰度图像直方图均衡化
# dst = cv2.equalizeHist(img)
clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(8, 8))
dst = clahe.apply(img)

# 直方图
hist = cv2.calcHist([dst],[0],None,[256],[0,256])

plt.figure()
plt.hist(dst.ravel(), 256)
plt.show()
cv2.imwrite('101hist.bmp',dst)

cv2.imshow("Histogram Equalization",np.hstack([img, dst]))
cv2.waitKey(0)

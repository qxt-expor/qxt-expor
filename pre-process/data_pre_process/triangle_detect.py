import os

import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm


# 定义形状检测函数
def ShapeDetection(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)  # 寻找轮廓点
    for obj in contours:
        area = cv2.contourArea(obj)  # 计算轮廓内区域的面积
        # cv2.drawContours(img, obj, -1, (255, 0, 0), 4)  # 绘制轮廓线
        perimeter = cv2.arcLength(obj, True)  # 计算轮廓周长
        approx = cv2.approxPolyDP(obj, 0.02 * perimeter, True)  # 获取轮廓角点坐标
        CornerNum = len(approx)  # 轮廓角点的数量
        x, y, w, h = cv2.boundingRect(approx)  # 获取坐标值和宽度、高度

        # 轮廓对象分类
        if CornerNum == 3:
            objType = "triangle"
        elif CornerNum == 4:
            if w == h:
                objType = "Square"
            else:
                objType = "Rectangle"
        elif CornerNum > 4:
            objType = "Circle"
        else:
            objType = "N"

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)  # 绘制边界框
        cv2.putText(img, objType, (x + (w // 2), y + (h // 2)), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 0),
                    1)  # 绘制文字


def Triangle_detect(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    tri = []  # 每个矩形以一个一维列表的形式存入tri列表中
    for c in contours:
        # 找到边界坐标
        min_list = []  # 保存单个轮廓的信息，x,y,w,h,area。 x,y 为起始点坐标
        x, y, w, h = cv2.boundingRect(c)  # 计算点集最外面的矩形边界
        min_list.append(x)
        min_list.append(y)
        min_list.append(w)
        min_list.append(h)
        min_list.append(w * h)  # 把轮廓面积也添加到 tri 中
        tri.append(min_list)

    # 找出最大矩形的 x,y,w,h,area
    max_area = tri[0][4]  # 把第一个矩形面积当作最大矩形面积
    for inlist in tri:
        area = inlist[4]
        if area >= max_area:
            x = inlist[0]
            y = inlist[1]
            w = inlist[2]
            h = inlist[3]
            max_area = area

    # 在原图上画出最大的矩形
    cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 1)
    return x, y, w, h


def detect_circle_demo(image):
    # dst = cv.bilateralFilter(image, 0, 150, 5)  #高斯双边模糊，不太好调节,霍夫噪声敏感，所以要先消除噪声
    # cv.imshow("1",dst)
    # dst = cv.pyrMeanShiftFiltering(image,5,100)  #均值迁移，EPT边缘保留滤波,霍夫噪声敏感，所以要先消除噪声
    # cv.imshow("2", dst)
    dst = cv2.GaussianBlur(image,(13,15),15) #使用高斯模糊，修改卷积核ksize也可以检测出来
    # cv.imshow("3", dst)
    gray = cv2.cvtColor(dst,cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles)) #around对数据四舍五入，为整数
    for i in circles[0,:]:
        cv2.circle(image,(i[0],i[1]),i[2],(0,0,255),2)
        cv2.circle(image,(i[0],i[1]),2,(255,0,0),2)   #圆心

    cv2.imshow("detect_circle_demo",image)
    cv2.waitKey()

def detect_circle_single(img):
    """
    识别图像中的圆形并裁切出相应的矩形保存到目标文件中
    source_file:源文件
    target_file:生成后的文件
    """
    bias = 20
    h, w, _ = img.shape
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 灰度图像
    gray = cv2.GaussianBlur(gray, (5, 5), 5)  # 模糊图像转低分辨率
    # cv2.imshow("fdga",gray)
    circles1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, param1=100, param2=100)
    try:  # 如果上一步没有检测到。执行try内容，就会报错。可以修改尝试看下。
        circles = circles1[0, :, :]  # 提取为二维
    except TypeError:
        print('未发现圆形物体！！', img)
    else:
        x, y, r = np.uint16(np.around(circles))[0]  # 四舍五入
        x0 = 0 if x < r + bias else x - r - bias
        y0 = 0 if y < r + bias else y - r - bias
        x1 = x + r + bias
        y1 = y + r + bias
        x1 = x1 if x1 < w else w
        y1 = y1 if y1 < h else h
        img = img[y0:y1, x0:x1]
        cv2.circle(img, (x, y), r, (0, 0, 255), 5)
        cv2.imshow('img',img)
        cv2.waitKey()
        # print(target_file)
    # cv2.imwrite(target_file, img)


if __name__ == '__main__':

    img_path = 'D:/Download/2022-12-19/2022-12-19/new/'
    # mask_path = 'D:/Download/mvtec_anomaly_detection.tar/mvtec_anomaly_detection/screw/ground_truth/empty-blister/'
    img_save_path = 'D:/Download/2022-12-19/2022-12-19/'
    # mask_save_path = 'D:/Download/yunlong/V_1.0.1_2/empty-blister/crop_mask/'

    for each in tqdm(os.listdir(img_path)):
        # each = each.split('_mask')[0] + '.bmp'
        img = cv2.imread(img_path + each)
        h_ori, w_ori, _ = img.shape
        scale_w = w_ori / 640
        scale_h = h_ori / 640
        img = cv2.resize(img, (640, 640))
        imgContour = img.copy()

        imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)  # 转灰度图
        imgBlur = cv2.GaussianBlur(imgGray, (35, 35), 1)  # 高斯模糊
        imgCanny = cv2.Canny(imgBlur, 200, 200)  # Canny算子边缘检测
        # imgBlur = cv2.medianBlur(imgCanny,5)
        # ShapeDetection(imgCanny)  # 形状检测
        detect_circle_single(img)
        # x, y, w, h = Triangle_detect(imgCanny)
        # result = Image.open(img_path + each).crop((int(x * scale_w * 0.8), int(y * scale_h * 0.8),
        #                                            int((x + w) * scale_w * 1.07), int((y + h) * scale_h * 1.07)))
        # mask = Image.open(mask_path + each.split('.')[0] + '_mask.bmp').resize((640, 640)).crop((x, y, x + w, y + h))
        # image1 = Image.new("RGB", (1714, 1434))
        # image1.paste(result, (int((image1.width-result.width)/2), int((image1.height-result.height)/2)))
        # result.save(img_save_path + each)
        # mask.save(mask_save_path + each.split('.')[0] + '_mask.bmp')

        # cv2.imshow("Original img", img)
        # cv2.imshow("closed", closed)
        # cv2.imshow("Blur", imgBlur)
        # cv2.imshow("imgCanny", imgCanny)
        # result.show()
        # cv2.imshow("shape Detection", result)
        # cv2.imshow("seg", Image.open(path).crop((x, y, x + w, y + h)))

        # cv2.waitKey(0)
        # cv2.destroyAllwinodows()

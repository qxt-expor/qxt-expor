import glob
import xml.dom.minidom
import cv2
from PIL import Image
import matplotlib.pyplot as plt
import os

class_name = ['black-pin', 'blister-fold', 'breakage', 'break-pin',
              'curved-pin', 'dirt', 'empty-blister', 'loss-packaging',
              'multi-pin', 'outplace-pin', 'poor-packaging',
              'skewing-pin']
for c in class_name:
    # 定义待批量裁剪图像的路径地址
    IMAGE_INPUT_PATH = r"D:\Download\yunlong\V_1.0.1\{}".format(c) + r"\bmp"
    XML_INPUT_PATH = r"D:\Download\yunlong\V_1.0.1\{}".format(c) + r"\xml"
    # 定义裁剪后的图像存放地址
    IMAGE_OUTPUT_PATH = r"D:\Download\yunlong\V_1.0.1\{}".format(c) + r"\resize"
    XML_OUTPUT_PATH = r"D:\Download\yunlong\V_1.0.1\{}".format(c) + r"\xml_resize"
    imglist = os.listdir(IMAGE_INPUT_PATH)
    xmllist = os.listdir(XML_INPUT_PATH)

    for i in range(len(imglist)):
        # 每个图像全路径
        image_input_fullname = IMAGE_INPUT_PATH + r'\{}'.format(imglist[i])
        xml_input_fullname = XML_INPUT_PATH + r'\{}'.format(xmllist[i])
        image_output_fullname = IMAGE_OUTPUT_PATH + r'\{}'.format(imglist[i])
        xml_output_fullname = XML_OUTPUT_PATH + r'\{}'.format(xmllist[i])

        img = cv2.imread(image_input_fullname)
        height, width = img.shape[:2]

        # 定义缩放信息 以等比例缩放到416为例
        scale = 640 / height
        height = 640
        width = int(width * scale)

        dom = xml.dom.minidom.parse(xml_input_fullname)
        root = dom.documentElement

        # 读取标注目标框
        objects = root.getElementsByTagName("bndbox")

        for object in objects:
            xmin = object.getElementsByTagName("xmin")
            xmin_data = int(float(xmin[0].firstChild.data))
            # xmin[0].firstChild.data =str(int(xmin1 * x))
            ymin = object.getElementsByTagName("ymin")
            ymin_data = int(float(ymin[0].firstChild.data))
            xmax = object.getElementsByTagName("xmax")
            xmax_data = int(float(xmax[0].firstChild.data))
            ymax = object.getElementsByTagName("ymax")
            ymax_data = int(float(ymax[0].firstChild.data))

            # 更新xml
            width_xml = root.getElementsByTagName("width")
            width_xml[0].firstChild.data = width
            height_xml = root.getElementsByTagName("height")
            height_xml[0].firstChild.data = height

            xmin[0].firstChild.data = int(xmin_data * scale)
            ymin[0].firstChild.data = int(ymin_data * scale)
            xmax[0].firstChild.data = int(xmax_data * scale)
            ymax[0].firstChild.data = int(ymax_data * scale)

            # 另存更新后的文件
            with open(xml_output_fullname, 'w') as f:
                dom.writexml(f, addindent='  ', encoding='utf-8')
            # 测试缩放效果
            img = cv2.resize(img, (width, height))
            '''
            # xmin, ymin, xmax, ymax分别为xml读取的坐标信息
            left_top = (int(xmin_data*scale), int(ymin_data*scale))
            right_down= (int(xmax_data*scale), int(ymax_data*scale))
            cv2.rectangle(img, left_top, right_down, (255, 0, 0), 1)
            '''

        cv2.imwrite(image_output_fullname, img)

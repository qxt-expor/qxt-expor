import os

import xml.dom.minidom
from PIL import Image
from tqdm import tqdm

# class_name = 'dirt'

# img_path = 'D:/Download/yunlong/V_1.0.1_2/{}'.format(class_name) + '/bmp/'
# xml_path = 'D:/Download/yunlong/V_1.0.1_2/{}'.format(class_name) + '/xml/'
# xml_output_path = 'D:/Download/yunlong/V_1.0.1_2/{}'.format(class_name) + '/crop_new_xml/'
# mask_path = 'D:/Download/mvtec_anomaly_detection.tar/mvtec_anomaly_detection/screw/ground_truth/empty-blister/'
# img_save_path = 'D:/Download/yunlong/V_1.0.1_2/{}'.format(class_name) + '/crop_new/'
# mask_save_path = 'D:/Download/yunlong/V_1.0.1_2/empty-blister/crop_mask/'
# img_path = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit-yunlong-v1/VOC2007/JPEGImages/'
img_path = 'D:/Download/2022-12-19/trains/1/'
img_save_path = 'D:/Download/2022-12-19/2022-12-19/new_make/1/'
# xml_path = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit-yunlong-v1/VOC2007/Annotations/'
# xml_output_path = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit-yunlong-v3/VOC2007/Annotations1/'

for each in tqdm(os.listdir(img_path)):
    img = Image.open(img_path + each)
    x = int((img.width / 2) * 0.2)
    y = int((img.height / 2) * 0.2)
    # x = int((img.width / 2) * 0.15)
    # y = int((img.height / 2) * 0.145)
    result = img.crop((x, y, img.width - x, img.height - y))
    if not os.path.exists(img_save_path):
        os.makedirs(img_save_path)
    # if not os.path.exists(xml_output_path):
    #     os.makedirs(xml_output_path)
    result.save(img_save_path + each)
    # xml_input_fullname = xml_path + each.split('.')[0] + '.xml'
    # xml_output_fullname = xml_output_path + each.split('.')[0] + '.xml'
    # dom = xml.dom.minidom.parse(xml_input_fullname)
    # root = dom.documentElement

    # 读取标注目标框
    # objects = root.getElementsByTagName("bndbox")
    #
    # for object in objects:
    #     xmin = object.getElementsByTagName("xmin")
    #     xmin_data = int(float(xmin[0].firstChild.data))
    #     # xmin[0].firstChild.data =str(int(xmin1 * x))
    #     ymin = object.getElementsByTagName("ymin")
    #     ymin_data = int(float(ymin[0].firstChild.data))
    #     xmax = object.getElementsByTagName("xmax")
    #     xmax_data = int(float(xmax[0].firstChild.data))
    #     ymax = object.getElementsByTagName("ymax")
    #     ymax_data = int(float(ymax[0].firstChild.data))
    #
    #     # 更新xml
    #     width_xml = root.getElementsByTagName("width")
    #     width_xml[0].firstChild.data = img.width - 2*x
    #     height_xml = root.getElementsByTagName("height")
    #     height_xml[0].firstChild.data = img.height - 2*y
    #
    #     xmin[0].firstChild.data = int(xmin_data - x)
    #     ymin[0].firstChild.data = int(ymin_data - y)
    #     xmax[0].firstChild.data = int(xmax_data - x)
    #     ymax[0].firstChild.data = int(ymax_data - y)
    #
    #     # 另存更新后的文件
    #     with open(xml_output_fullname, 'w') as f:
    #         dom.writexml(f, encoding='utf-8')
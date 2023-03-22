import os

import xml.dom.minidom

import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm

# img_path = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\yunlong_v0\test\empty'
# img_save_path = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\yunlong_v2\test\empty'
img_path = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\yunlong_backup\v3\test\good_enhance'
img_save_path = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\yunlong_backup\v3\test'
# xml_path = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit-yunlong-v1/VOC2007/Annotations/'
# xml_output_path = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit-yunlong-v3/VOC2007/Annotations1/'

clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8, 8))

for each in tqdm(os.listdir(img_path)):
    file_path = os.path.join(img_path, each)
    img = Image.open(file_path).convert('L')
    # good
    # x = int((img.width / 2) * 0.45)
    # y = int((img.height / 2) * 0.45)
    # x = int((img.width / 2) * 0.15)
    # y = int((img.height / 2) * 0.145)
    # result = img.crop((x, y, img.width - x, img.height - y))

    if not os.path.exists(img_save_path):
        os.makedirs(img_save_path)
    # result.save(os.path.join(img_save_path, 'good_crop', each))
    result = Image.fromarray(clahe.apply(np.array(img)))

    # if not os.path.exists(xml_output_path):
    #     os.makedirs(xml_output_path)
    result.save(os.path.join(img_save_path, 'good_enhance_clahe', each))
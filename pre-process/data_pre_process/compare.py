import os

xml_path = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit-yunlong-v1/VOC2007/Annotations/'
xml_output_path = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit-yunlong-v3/VOC2007/Annotations1/'


xml_1 = os.listdir(xml_path)
xml_2 = os.listdir(xml_output_path)
print(list(set(xml_1) - set(xml_2)))
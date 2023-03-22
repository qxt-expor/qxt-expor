import os
import xml.dom.minidom

import numpy as np

class_name_notnull = ['black-pin', 'blister-fold', 'breakage', 'break-pin',
                      'curved-pin', 'dirt', 'empty-blister', 'loss-packaging',
                      'multi-pin', 'outplace-pin', 'poor-packaging',
                      'skewing-pin',
                      'damaged-packaging', 'foreign', 'packaging-fold', 'plate-fold', 'unusual-pin']
class_name_null = ['damaged-packaging', 'foreign', 'packaging-fold', 'plate-fold', 'unusual-pin']
class_num = np.zeros(len(class_name_notnull))
object_num = {class_name: num for class_name, num in zip(class_name_notnull, class_num)}
null_object_num = {class_name: [] for class_name in class_name_null}
for c in class_name_notnull:
    XML_INPUT_PATH = r"D:\Download\yunlong\VOC2007\{}".format(c) + r"\xml"
    xmllist = os.listdir(XML_INPUT_PATH)
    for xml_name in xmllist:
        xml_input_fullname = XML_INPUT_PATH + r'\{}'.format(xml_name)
        dom = xml.dom.minidom.parse(xml_input_fullname)
        root = dom.documentElement

        # 读取标注目标框
        objects = root.getElementsByTagName("object")
        for object in objects:
            object_name = object.getElementsByTagName("name")
            # print(object_name[0].firstChild.data)
            if object_name[0].firstChild.data in class_name_null:
                null_object_num[object_name[0].firstChild.data].append(xml_input_fullname)
            object_num[object_name[0].firstChild.data] += 1

print(object_num)
print(null_object_num)


# {'black-pin': 9.0, 'blister-fold': 55.0, 'breakage': 70.0, 'break-pin': 23.0, 'curved-pin': 20.0, 'dirt': 148.0,
# 'empty-blister': 1418.0, 'loss-packaging': 139.0, 'multi-pin': 492.0, 'outplace-pin': 86.0, 'poor-packaging': 103.0,
# 'skewing-pin': 48.0,
# 'damaged-packaging': 11.0, 'foreign': 3.0, 'packaging-fold': 39.0, 'plate-fold': 7.0, 'unusual-pin': 7.0}
# {'damaged-packaging': ['D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\25-1396.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\940.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1552.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\poor-packaging\\xml\\25-218.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\poor-packaging\\xml\\40.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\poor-packaging\\xml\\41.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\poor-packaging\\xml\\42.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\poor-packaging\\xml\\43.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\poor-packaging\\xml\\55.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\skewing-pin\\xml\\16.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\skewing-pin\\xml\\858.xml'],
# 'foreign': ['D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\35.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1597.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\308.xml'],
# 'packaging-fold': ['D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\25-1397.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\25-1397.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\25-1397.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\25-1397.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\25-1398.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\25-1399.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\943.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\943.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\943.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\943.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\breakage\\xml\\943.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\18.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\22.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\33.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\33.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\34.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\34.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\34.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\5.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\51.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\53.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\56.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\6.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\7.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\7.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\7.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\8.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\8.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\8.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\8.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\dirt\\xml\\8.xml'],
# 'plate-fold': ['D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\224.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1756.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1757.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1758.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1759.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\459.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\outplace-pin\\xml\\826.xml'],
# 'unusual-pin': ['D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\222.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1403.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1505.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\empty-blister\\xml\\25-1591.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\outplace-pin\\xml\\796.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\outplace-pin\\xml\\803.xml',
# 'D:\\Download\\yunlong\\V_1.0.1_2\\outplace-pin\\xml\\845.xml']}
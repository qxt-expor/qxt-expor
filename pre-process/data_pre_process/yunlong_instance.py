import os
import xml.dom.minidom

import numpy as np

class_name_notnull = ['black-pin', 'blister-fold', 'breakage', 'break-pin',
                      'curved-pin', 'dirt', 'empty-blister', 'loss-packaging',
                      'multi-pin', 'outplace-pin', 'poor-packaging',
                      'skewing-pin',
                      'damaged-packaging', 'foreign', 'packaging-fold', 'plate-fold', 'unusual-pin', 'black-spot']
# class_name_notnull = ['dirty', 'unknown', 'skewing', 'empty','multi']

# class_name_notnull = ['spot_stain', 'bad_circle', 'streak_stain', 'no_cork', 'broken_cork', 'broken_ball', 'no_ball',
#                       'white_glue', 'logo', 'bottle_cap', 'white_stain', 'double_shadow']
# class_name_null = ['damaged-packaging', 'foreign', 'packaging-fold', 'plate-fold', 'unusual-pin']
class_num = np.zeros(len(class_name_notnull))
object_num_trainval = {class_name: num for class_name, num in zip(class_name_notnull, class_num)}
object_num_test = {class_name: num for class_name, num in zip(class_name_notnull, class_num)}
object_xml_path = {class_name: [] for class_name in class_name_notnull}
dataset_root_path = r"D:\Download\yunlong\train_1.1.7\com"
# dataset_root_path = r'D:\Download\yunlong\VOC2007'
XML_INPUT_PATH = os.path.join(dataset_root_path, 'Annotations')
trainval_path = os.path.join(dataset_root_path, 'ImageSets/Main/trainval.txt')
trainval_files = open(trainval_path, 'r').read().splitlines()
test_path = os.path.join(dataset_root_path, 'ImageSets/Main/test.txt')
test_files = open(test_path, 'r').read().splitlines()
# XML_INPUT_PATH = r'D:\Download\bottle\inside_wall\VOC2007\Annotations'
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
        # if object_num_trainval[object_name[0].firstChild.data] < 25:
        # if xml_name.split('.xml')[0] in test_files:# and xml_name not in object_xml_path[object_name[0].firstChild.data]:
        #     object_xml_path[object_name[0].firstChild.data].append(xml_name)

        if xml_name.split('.xml')[0] in trainval_files:
            object_num_trainval[object_name[0].firstChild.data] += 1
            object_xml_path[object_name[0].firstChild.data].append(xml_name)
        elif xml_name.split('.xml')[0] in test_files:
            object_num_test[object_name[0].firstChild.data] += 1
            object_xml_path[object_name[0].firstChild.data].append(xml_name)

print('trainval:{}'.format(object_num_trainval))
print('test:{}'.format(object_num_test))
print('the path of 25 instances at least')
for class_name in object_xml_path:
    print(class_name + ':{}'.format(object_xml_path[class_name]))

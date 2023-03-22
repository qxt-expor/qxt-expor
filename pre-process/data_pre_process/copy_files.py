# srcfile 需要复制、移动的文件
# dstpath 目的地址
import os
import shutil
from glob import glob


def mycopyfile(srcfile, dstpath):  # 复制函数
    srcfile = src_path + srcfile + '.bmp'
    # print(srcfile)
    if not os.path.isfile(srcfile):
        print("%s not exist!" % (srcfile))
    else:
        fpath, fname = os.path.split(srcfile)  # 分离文件名和路径
        if not os.path.exists(dstpath):
            os.makedirs(dstpath)  # 创建路径
        print(fpath, fname)
        shutil.copy(srcfile, dstpath + fname)  # 复制文件
        print("copy %s -> %s" % (srcfile, dstpath + fname))


# content_root = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit/VOC2007/'
content_root = 'D:/ProjectG/YOLOX-main/datasets/VOCdevkit-yunlong-v2/VOC2007/'

src_path = content_root + 'JPEGImages/'
src_dir = content_root + "ImageSets/Main/test.txt"
dst_dir = 'D:/ProjectG/YOLOX-main/assets/test_yunlong_v2/'  # 目的路径记得加斜杠
# src_file_list = glob(src_dir + '*')  # glob获得路径下所有文件，可根据需要修改

# src_files = os.listdir (src_dir)
src_files = open(src_dir, 'r').read().splitlines()
for srcfile in src_files:
    print(srcfile)
    mycopyfile(srcfile, dst_dir)  # 复制文件

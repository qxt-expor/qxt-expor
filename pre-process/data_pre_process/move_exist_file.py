# srcfile 需要复制、移动的文件
# dstpath 目的地址
import os
import shutil
from glob import glob


def mycopyfile(srcfile, dstpath):  # 复制函数
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


content_root = 'D:/Download/bottle/'

src_path = content_root + '内壁数据集2（未标注可能含缺陷）/Images/'
src_dir = content_root + "内壁数据集2（未标注可能含缺陷）/Annotations"
dst_dir = 'D:/Download/bottle/内壁数据集2（未标注可能含缺陷）/train/'  # 目的路径记得加斜杠
# src_file_list = glob(src_dir + '*')  # glob获得路径下所有文件，可根据需要修改

src_files = os.listdir(src_dir)
# src_files = open(src_dir, 'r').read().splitlines()
for srcfile in src_files:
    srcfile = srcfile.split('.xml')[0]
    srcfile = src_path + srcfile + '.jpg'
    mycopyfile(srcfile, dst_dir)  # 复制文件

##python批量更换后缀名

import os

# 列出当前目录下所有的文件

files = os.listdir('./')
# print('files',files)
for filename in files:
    if '_bmp' in filename:
        if filename.endswith('jpg'):
            newname = filename.split("_bmp")[0] + ".bmp"
        elif filename.endswith('xml'):
            newname = filename.split("_bmp")[0] + ".xml"
        print(newname)
        os.rename(filename, newname)

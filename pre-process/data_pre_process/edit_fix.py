import os
import re

# folder = r'./datasets/VOCdevkit/VOC2007/Annotations'
folder = r'D:\Download\中科煜宸\xml'

files = os.listdir(folder)
for item in files:
    if not item.endswith('xml'):
        continue
    path = os.path.join(folder, item)
    with open(path, 'r') as f:
        txt = f.read()
    reg = re.compile(r'<filename>(?P<name>.*?)</filename>', re.S)
    res = reg.search(txt)
    name = res.group('name')
    # txt = re.sub(r'<path>(?P<name>.*?)</path>','<path></path>',txt,re.S)
    newpath = name.split("(2)")[0] + '-dp.bmp'
    print(newpath)

    txt = re.sub(r'<path>(?P<name>.*?)</path>', '<path>' +  + '</path>', txt, re.S)
    txt = re.sub(r'<filename>(?P<name>.*?)</filename>', '<filename>' + newpath + '</filename>', txt, re.S)
    # print(txt)

    with open(path, 'w') as f:
        f.write(txt)
print('done')

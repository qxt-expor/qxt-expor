import os
import shutil

new_path = "../assets/0505test"
with open('D:/ProjectG/datasets/wuzhongyaoban24_voc/ImageSets/Main/test.txt', 'r') as f1:
    files = f1.readlines()
    for file in files:
        print(file)
        file = file.strip("\n")
        des_path = new_path + '/' + file
        file = file + ".bmp"
        filepath = "D:/ProjectG/datasets/wuzhongyaoban24_voc/JPEGImages" + '/' + file
        shutil.copy(filepath, des_path)
    f1.close()

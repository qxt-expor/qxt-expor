# from PIL import Image
#
# mask1 = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\grid\ground_truth\dirt\27_mask.bmp'
# mask1 = Image.open(mask1)
#
# mask2 = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\carpet\ground_truth\color\000_mask.png'
# mask2 = Image.open(mask2)
#
# print(mask1)
# print(mask2)

from PIL import Image

import os

input_dir = 'D:/Download/yunlong/anomaly_version_1/carpet/ground_truth/unknown/'

a = os.listdir(input_dir)

for i in a:
    print(i)

    I = Image.open(input_dir + i)

    L = I.convert('L')

    L.save(input_dir + i)

# 直方图正规化API
# 灰度级主要在0~150之间，造成图像对比度较低，可用直方图正规化将图像灰度级拉伸到0~255,使其更清晰
import os

import cv2
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt

# 灰度图像转化为ndarray类型
if __name__ == "__main__":
    image_path = 'D:/Download/yunlong/V_1.0.1_2/ok/crop/'
    save_path = 'D:/Download/yunlong/V_1.0.1_2/ok/crop_new/'
    for each in tqdm(os.listdir(image_path)):
        src = cv2.imread(image_path + each, cv2.IMREAD_ANYCOLOR)
        dst = np.zeros_like(src)
        cv2.normalize(src, dst, 0, 200, cv2.NORM_MINMAX, cv2.CV_8U)  # 公式
        cv2.imwrite(save_path + each, dst)
        # cv2.imshow("src", src)
        # cv2.imshow("dst", dst)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
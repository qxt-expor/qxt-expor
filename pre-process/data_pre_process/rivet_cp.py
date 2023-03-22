import os.path
import random

from PIL import Image
import math
import numpy as np
from tqdm import tqdm

paste_path = 'D:/Download/2022-12-19/2022-12-19/good/'

for file in tqdm(os.listdir(paste_path)):
    if random.randint(1, 9) > 5:
        continue
    cut_path = os.path.join('D:/Download/2022-12-19/2022-12-19/new/', str(random.randint(1, 3))+'.bmp')
    cut_img = Image.open(cut_path)
    rotation = random.randrange(20, 360)
    cut_img = cut_img.rotate(rotation)
    w, h = cut_img.size
    # r = 125 # 1
    r = 133  # 2
    # r = 149 # 3
    cut_img_np = np.array(cut_img)

    paste_img = Image.open(os.path.join(paste_path, file))
    paste_img = paste_img.resize((w, h))
    paste_img = paste_img.rotate(random.choice([90.0, 180.0, 270.0]))
    paste_img_np = np.array(paste_img)

    print(cut_img_np)
    for i in range(cut_img.width):
        for j in range(cut_img.height):
            if math.sqrt(math.pow(i - w / 2, 2) + math.pow(j - h / 2, 2)) < r:
                paste_img_np[i, j] = cut_img_np[i, j]

    save_img = Image.fromarray(paste_img_np)
    # save_img.show()
    save_img.save(os.path.join(os.path.dirname(paste_path),
                               file.split('.')[0] + '_bpaste{}.bmp'.format(
                                   os.path.basename(cut_path).split('.')[0])))

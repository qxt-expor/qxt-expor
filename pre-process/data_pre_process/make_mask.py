import json
import cv2
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os

img_path = 'D:/Download/mvtec_anomaly_detection.tar/mvtec_anomaly_detection/rivet/test/gap/'
json_path = 'D:/Download/mvtec_anomaly_detection.tar/mvtec_anomaly_detection/rivet/test/gap/json/'
save_path = 'D:/Download/mvtec_anomaly_detection.tar/mvtec_anomaly_detection/rivet/ground_truth/gap/'
tmp = {}
for each in tqdm(os.listdir(json_path)):

    with open(json_path + each, "r") as f:
        tmp = f.read()

    tmp = json.loads(tmp)
    img = cv2.imread(img_path + each.split('.json')[0] + '.bmp')
    # BGR->RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mask = np.zeros_like(img)
    for i in range(len(tmp['shapes'])):
        points = tmp["shapes"][i]["points"]
        points = np.array(points, np.int32)
        # points = np.insert(points, 1, [points[1][0], points[0][1]], axis=0)
        # points = np.insert(points, 3, [points[0][0], points[2][1]], axis=0)

        box = tmp["shapes"][i]["points"]
        box = np.array(box, np.int32)

        cv2.rectangle(img, (box[0][0], box[0][1]), (box[1][0], box[1][1]), (125, 125, 125), 2)

        # cv2.polylines(img, [points], 1, (0,0,255))
        cv2.fillPoly(mask, [points], (255, 255, 255))
    img_add = cv2.addWeighted(mask, 0.3, img, 0.7, 0)
    cv2.imwrite(save_path + each.split('.json')[0] + '_mask.bmp', mask)
    # plt.imshow(img_add)
    # plt.show()

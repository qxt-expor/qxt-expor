import os
import cv2

# dataset_path = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\grid'
# datav0_path = r'D:\Download\mvtec_anomaly_detection.tar\mvtec_anomaly_detection\grid_v0'
# clahe = cv2.createCLAHE(clipLimit=1.7, tileGridSize=(8, 8))
#
# for dir in os.listdir(datav0_path):
#     if dir == 'ground_truth':
#         continue
#     file_path = os.path.join(datav0_path, dir)
#     for sub_dir in os.listdir(file_path):
#         save_path = os.path.join(dataset_path, dir, sub_dir)
#         if not os.path.exists(save_path):
#             os.makedirs(save_path)
#         image_path = os.path.join(file_path, sub_dir)
#         for image_file in os.listdir(image_path):
#             img = cv2.imread(os.path.join(image_path, image_file), 0)
#             dst = clahe.apply(img)
#             cv2.imwrite(os.path.join(save_path, image_file), dst)


ori_img_path = r'D:\Download\yunlong\real_img\save'
dst_path = r'D:\Download\yunlong\real_img\cle'
clahe = cv2.createCLAHE(clipLimit=3, tileGridSize=(8, 8))

for img_file in os.listdir(ori_img_path):
    file_path = os.path.join(ori_img_path, img_file)
    img = cv2.imread(file_path, 0)
    dst = clahe.apply(img)
    print(dst)
    # cv2.imwrite(os.path.join(dst_path, img_file), dst)

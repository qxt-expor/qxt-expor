import numpy as np
import cv2
from PIL import Image, ImageEnhance
import random
import matplotlib.pyplot as plt


# 随机改变亮暗、对比度和颜色等
def random_distort(img):
    # 随机改变亮度
    def random_brightness(img, lower=0.5, upper=3):
        e = np.random.uniform(lower, upper)
        return ImageEnhance.Brightness(img).enhance(e)

    # 随机改变对比度
    def random_contrast(img, lower=0.5, upper=3):
        e = np.random.uniform(lower, upper)
        return ImageEnhance.Contrast(img).enhance(e)

    # 随机改变颜色
    def random_color(img, lower=0.5, upper=3):
        e = np.random.uniform(lower, upper)
        return ImageEnhance.Color(img).enhance(e)

    ops = [random_brightness, random_contrast, random_color]
    np.random.shuffle(ops)

    img = Image.fromarray(img)
    img = ops[0](img)
    img = ops[1](img)
    img = ops[2](img)
    img = np.asarray(img)

    return img


# 定义可视化函数，用于对比原图和图像增强的效果


def visualize(srcimg, img_enhance):
    # 图像可视化
    plt.figure(num=2, figsize=(6, 12))
    plt.subplot(1, 2, 1)
    plt.title('Src Image', color='#0000FF')
    plt.axis('off')  # 不显示坐标轴
    plt.imshow(srcimg)  # 显示原图片

    # 对原图做 随机改变亮暗、对比度和颜色等 数据增强
    # srcimg_gtbox = records[0]['gt_bbox']
    # srcimg_label = records[0]['gt_class']

    plt.subplot(1, 2, 2)
    plt.title('Enhance Image', color='#0000FF')
    plt.axis('off')  # 不显示坐标轴
    plt.imshow(img_enhance)
    plt.show()


image_path = 'C:/Users/19505/Desktop/images/977081.jpg'
# image_path = records[0]['im_file']
print("read image from file {}".format(image_path))
srcimg = Image.open(image_path)
# 将PIL读取的图像转换成array类型
srcimg = np.array(srcimg)

# 对原图做 随机改变亮暗、对比度和颜色等 数据增强
img_enhance = random_distort(srcimg)
visualize(srcimg, img_enhance)


# 随机填充
def random_expand(img,
                  # gtboxes,
                  max_ratio=4.,
                  fill=None,
                  keep_ratio=True,
                  thresh=0.5):
    if random.random() > thresh:
        return img  # , gtboxes

    if max_ratio < 1.0:
        return img  # , gtboxes

    h, w, c = img.shape
    ratio_x = random.uniform(1, max_ratio)
    if keep_ratio:
        ratio_y = ratio_x
    else:
        ratio_y = random.uniform(1, max_ratio)
    oh = int(h * ratio_y)
    ow = int(w * ratio_x)
    off_x = random.randint(0, ow - w)
    off_y = random.randint(0, oh - h)

    out_img = np.zeros((oh, ow, c))
    if fill and len(fill) == c:
        for i in range(c):
            out_img[:, :, i] = fill[i] * 255.0

    out_img[off_y:off_y + h, off_x:off_x + w, :] = img
    print(img.shape,out_img.shape)
    # gtboxes[:, 0] = ((gtboxes[:, 0] * w) + off_x) / float(ow)
    # gtboxes[:, 1] = ((gtboxes[:, 1] * h) + off_y) / float(oh)
    # gtboxes[:, 2] = gtboxes[:, 2] / ratio_x
    # gtboxes[:, 3] = gtboxes[:, 3] / ratio_y

    return out_img.astype('uint8')  # , gtboxes


# 对原图做 随机改变亮暗、对比度和颜色等 数据增强
# srcimg_gtbox = records[0]['gt_bbox']
# img_enhance, new_gtbox = random_expand(srcimg, srcimg_gtbox)
img_enhance = random_expand(srcimg)
visualize(srcimg, img_enhance)


# 随机缩放
def random_interp(img, size, interp=None):
    interp_method = [
        cv2.INTER_NEAREST,
        cv2.INTER_LINEAR,
        cv2.INTER_AREA,
        cv2.INTER_CUBIC,
        cv2.INTER_LANCZOS4,
    ]
    if not interp or interp not in interp_method:
        interp = interp_method[random.randint(0, len(interp_method) - 1)]
    h, w, _ = img.shape
    im_scale_x = size / float(w)
    im_scale_y = size / float(h)
    img = cv2.resize(
        img, None, None, fx=im_scale_x, fy=im_scale_y, interpolation=interp)
    return img


img_enhance = random_interp(srcimg, 640)
visualize(srcimg, img_enhance)

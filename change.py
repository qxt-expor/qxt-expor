import os
import json

json_dir = 'E:/qxt/train-back/'  # json文件路径
out_dir = 'E:/qxt/outputDir/'  # 输出的 txt 文件路径


def get_json(json_file, filename):
    # 读取 json 文件数据
    with open(json_file, 'r') as load_f:
        content = json.load(load_f)

    # # 循环处理
    tmp = filename
    filename_txt = out_dir + tmp + '.txt'
    # 创建txt文件
    fp = open(filename_txt, mode="w", encoding="utf-8")
    # 将数据写入文件
    str_tmp = ""  # 存储字符串内容
    # 1.获取version、flags数据
    version = content["version"]
    flags = content["flags"]
    # 暂存内容
    str_tmp = str(version) + "\n" + str(flags) + "\n"

    # 2. 获取shapes数组中的数据
    # 循环读取 shapes中的每一组数据，json文件中有2组数据，循环则是2个 [0,1]
    for i in range(2):
        label = (content["shapes"][i])["label"]
        line_color = (content["shapes"][i])["line_color"]
        fill_color = (content["shapes"][i])["fill_color"]
        str_tmp += str(label) + "\n" + str(line_color) + "\n" + str(fill_color) + "\n"  ##暂存内容
        # 读取points中的数据，有6组数据
        points_size = len((content["shapes"][i])["points"])
        for j in range(points_size):
            x = (content["shapes"][i])["points"][j][0]
            y = (content["shapes"][i])["points"][j][1]
            str_tmp += str(x) + "        " + str(y) + "\n"  ##暂存内容
        # 读取shape_type,flags
        shape_type = (content["shapes"][i])["shape_type"]
        flags = (content["shapes"][i])["flags"]
        str_tmp += str(shape_type) + "        " + str(flags) + "\n"  ##暂存内容
    # 3. 获取lineColor、fillColor、imagePath、imageData
    line_Color = content["lineColor"]
    fill_Color = content["fillColor"]
    imagePath = content["imagePath"]
    imageData = content["imageData"]

    # lineColor是数组，获取并存储lineColor
    for i in range(len(line_Color)):
        str_tmp += str(line_Color[i]) + "   "
    str_tmp += "\n"  # 换行效果
    # fillColor与lineColor一样，也为数组，获取并存储fillColor
    for i in range(len(fill_Color)):
        str_tmp += str(fill_Color[i]) + "   "
    str_tmp += "\n"  # 换行效果
    str_tmp += str(imagePath) + "        " + str(imageData) + "\n"  ##暂存内容
    fp = open(filename_txt, mode="r+", encoding="utf-8")
    file_str = str_tmp
    line_data = fp.readlines()

    if len(line_data) != 0:
        fp.write('\n' + file_str)
    else:
        fp.write(file_str)
    fp.close()


def main():
    files = os.listdir(json_dir)  # 得到文件夹下的所有文件名称
    s = []
    for file in files:  # 遍历文件夹
        filename = file.split('.')[0]
        # print(tmp)
        get_json(json_dir + file, filename)


if __name__ == '__main__':
    main()


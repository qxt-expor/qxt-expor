import os
from glob import glob
from sklearn.model_selection import train_test_split

saved_path = r'D:\Download\yunlong\train_1.1.7\com'  # 保存路径
saved_path = saved_path.replace('\\', '/')
# 2.创建要求文件夹
if not os.path.exists(saved_path + "/ImageSets/Main/"):
    os.makedirs(saved_path + "/ImageSets/Main/")

# 3.split files for txt
txtsavepath = saved_path + "/ImageSets/Main/"
# ftrainval = open(txtsavepath + '/trainval.txt', 'w')
ftrainval = open(txtsavepath + 'trainval.txt', 'w')
ftest = open(txtsavepath + 'test.txt', 'w')
ftrain = open(txtsavepath + 'train.txt', 'w')
fval = open(txtsavepath + 'val.txt', 'w')

total_files = glob(saved_path + "/Annotations/*.xml")

total_files = [i.split("\\")[-1].split(".xml")[0] for i in total_files]
print(total_files)
# for file in total_files:
#     ftrainval.write(file + "\n")

# split
trainval_files, test_files = train_test_split(total_files, test_size=0.3, random_state=39)
train_files, val_files = train_test_split(trainval_files, test_size=0.25, random_state=39)

# trainval
for file in trainval_files:
    ftrainval.write(file + "\n")
print("trainval num:{}".format(len(trainval_files)))
# test
for file in test_files:
    ftest.write(file + "\n")
print("test num:{}".format(len(test_files)))
# train
for file in train_files:
    ftrain.write(file + "\n")
print("train num:{}".format(len(train_files)))
# val
for file in val_files:
    fval.write(file + "\n")
print("val num:{}".format(len(val_files)))

print("total num:{}".format(len(trainval_files)+len(test_files)))

ftrainval.close()
ftest.close()
ftrain.close()
fval.close()

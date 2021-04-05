# 将这些放在每个笔记本的顶部，以实现自动重新加载和内联打印
%reload_ext autoreload
%autoreload 2
%matplotlib inline

# 导入必要的包
import pandas as pd
import numpy
import os
import shutil
# 对原始文件进行相对于的重命名，例如 male.100.jpg
# os.makedirs('./data',exist_ok=True)


# df_train = pd.read_csv('train.csv')
# df_test = pd.read_csv('test.csv')

# train_dir = './data/train'
# test_dir = './data/test'

# train_list = os.listdir(train_dir)
# train_list.sort(key=lambda x:int(x.split('.')[0]))

# for i in range(len(train_list)):
#     l = df_train.loc[i].label
#     if l==1:
#         sex = 'female'
#     else:
#         sex = 'male'
#     oldname = train_dir + '/' + train_list[i]
#     newname = train_dir + '/' + sex + '.'+train_list[i]
#     print(oldname,'=====>',newname)
#     os.rename(oldname,newname)
#     # print(sex,df_train.loc[i].id)

# 该文件包含我们将使用的所有主要外部库
from fastai.imports import *

from fastai.vision.all import *
import zipfile

# kaggle上文件存储位置需要更换，否则无法进行写入
PATH = '../input/face-pic/data/'
TMP_PATH = "./data/"
# MODEL_PATH = "/tmp/model/"
sz=224

from fastai import *
from fastai.vision import *
print(torch.cuda.is_available(), torch.backends.cudnn.enabled)

print(torch.backends.cudnn.enabled)

# 将./input/face-pic/data 下的文件写入到 ./data下
def cover_files(source_dir, target_ir):
    for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file)

        if os.path.isfile(source_file):
            shutil.copy(source_file, target_ir)

os.makedirs('./data',exist_ok=True)

os.makedirs('./data/train',exist_ok=True)
os.makedirs('./data/test',exist_ok=True)
cover_files('../input/face-pic/data/train','./data/train')

# 检查文件是否正确
train_path = './data/train'
print(os.listdir(train_path)[:5])

# 使用numpy库 将训练的数据集变成数组形式
# fnames = np.array([f'train/{f}' for f in sorted(os.listdir(f'{TMP_PATH}train'))])
# labels = np.array([(1 if 'female' in fname else 0) for fname in fnames])
# fnames,labels

# 通过文件名 建立对应标签数据
train_set = sorted(os.listdir('../input/face-pic/data/train'))
fnames = np.array([f'train/{i}' for i in train_set])

labels = np.array([(1 if 'female' in fname else 0) for fname in fnames])
fnames,labels


# 打印图片验证数组的正确性
img = plt.imread(f'{TMP_PATH}{fnames[10000]}')
plt.imshow(img)

files = get_image_files(TMP_PATH+"train")

test_files = get_image_files(PATH+"test")

str(test_files[1]).split('.')[-2].split('/')[-1]

# test_dir = '../input/face-pic/data/test'
# test_list = os.listdir(test_dir)
test_files.sort(key=lambda x:int(str(x).split('.')[-2].split('/')[-1]))

files[0].name #可以获得数据的名字

# 通过正则表达式提取类型标签
pat = r'^(.*)\.\d+.jpg'

dls = ImageDataLoaders.from_name_re(TMP_PATH, files, pat, item_tfms=Resize(224))

dls.show_batch()

#进行数据增强
dls2 = ImageDataLoaders.from_name_re(TMP_PATH,files,pat,item_tfms = Resize(460),batch_tfms = aug_transforms(size=224))

dls2.show_batch()

timg = TensorImage(array(img)).permute(2,0,1).float()/255.
def _batch_ex(bs): return TensorImage(timg[None].expand(bs, *timg.shape).clone())
tfms = aug_transforms(pad_mode='zeros', mult=2, min_scale=0.5)
y = _batch_ex(9)
for t in tfms: y = t(y, split_idx=0)
_,axs = plt.subplots(1,3, figsize=(12,3))
for i,ax in enumerate(axs.flatten()): show_image(y[i], ctx=ax)

tfms = aug_transforms(pad_mode='zeros', mult=2, batch=True)
y = _batch_ex(9)
for t in tfms: y = t(y, split_idx=0)
_,axs = plt.subplots(1,3, figsize=(12,3))
for i,ax in enumerate(axs.flatten()): show_image(y[i], ctx=ax)

learn = cnn_learner(dls2,resnet50,metrics = error_rate)


learn.fine_tune(40, 1e-3)


res = []
num = []
for i in range(0,5708):
    num.append(i+18001)
    img = open_image(test_files[i])
    sex = learner.predict(img)[0]
    if str(sex)=='female': res.append(1)
    else: res.append(0)

xxx = {'id':num,'label':res}
result = pd.DataFrame(xxx)
result.to_csv('../working/fastai1.0.61-1.csv',index=False)

learn.save('fastaiV2.0')
path = './'
path2 = './data/models'
def copy_allfiles(src,dest):
#src:原文件夹；dest:目标文件夹
  src_files = os.listdir(src)
  for file_name in src_files:
    full_file_name = os.path.join(src, file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest)

copy_allfiles(path2,path)
learn.export()






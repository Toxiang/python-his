# 放在开头实现内联打印
# %reload_ext autoreload
# %autoreload 2
# %matplotlib inline

import pandas as pd
import numpy
import os
import shutil
from fastai import *
from fastai.vision import *
# import fastai
import zipfile

PATH = '../input/face-pic/data/'
TMP_PATH = "./data/"
MODEL_PATH = "/tmp/model/"
sz=224

def cover_files(source_dir, target_ir):
    for file in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file)

        if os.path.isfile(source_file):
            shutil.copy(source_file, target_ir)

os.makedirs('./data',exist_ok=True)

os.makedirs('./data/train',exist_ok=True)
os.makedirs('./data/test',exist_ok=True)

cover_files('../input/face-pic/data/train','./data/train')

os.listdir(TMP_PATH)
# 检查文件是否正确
train_path = './data/train'
os.listdir(train_path)[:5]

fnames = np.array([f'train/{f}' for f in sorted(os.listdir(f'{TMP_PATH}train'))])
labels = np.array([(1 if 'female' in fname else 0) for fname in fnames])

img = plt.imread(f'{TMP_PATH}{fnames[1000]}')
plt.imshow(img)

files = get_image_files(TMP_PATH+"train")
test_files = get_image_files(PATH+"test")

pat = r'/.*/(.*)\.\d+\.jpg$'

s = re.compile(r'/.*/(.*)\.\d+\.jpg$')

# s.split(str(files[0]))[1]

data = ImageDataBunch.from_name_re(path = TMP_PATH ,fnames=files , pat=pat,size=224,bs=16)


learner = cnn_learner(data, models.resnet34, metrics=[accuracy])

learner.fit_one_cycle(20,1e-3)

interp = ClassificationInterpretation.from_learner(learner)
interp.plot_top_losses(20, figsize=(20,20))

# files[2904]
interp.top_losses(100)

test_files.sort(key=lambda x:int(str(x).split('.')[-2].split('/')[-1]))

res = []
num = []
for i in range(0,5708):
    num.append(i+18001)
    img = open_image(test_files[i])
    sex = learner.predict(img)[0]
    if str(sex)=='female': res.append(1)
    else: res.append(0)

learner.save('model-1-0-61')
learner.export()
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
xxx = {'id':num,'label':res}
result = pd.DataFrame(xxx)
result.to_csv('../working/fastai1.0.61-1.csv',index=False)
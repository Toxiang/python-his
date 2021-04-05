import pandas as pd
import numpy
import os

os.makedirs('./data',exist_ok=True)


df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

train_dir = './data/train'
test_dir = './data/test'

train_list = os.listdir(train_dir)
train_list.sort(key=lambda x:int(x.split('.')[0]))

for i in range(len(train_list)):
    l = df_train.loc[i].label
    if l==1:
        sex = 'female'
    else:
        sex = 'male'
    oldname = train_dir + '/' + train_list[i]
    newname = train_dir + '/' + sex + '.'+train_list[i]
    print(oldname,'=====>',newname)
    os.rename(oldname,newname)
    # print(sex,df_train.loc[i].id)



# print(os.listdir(train_dir)[:5])
# import glob
#
# train_list = glob.glob(os.path.join(train_dir,'*.jpg'))
# test_list = glob.glob(os.path.join(test_dir, '*.jpg'))

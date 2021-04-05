# 能够手动创建DataFrame或Series非常方便。但是，在大多数情况下，
# 我们实际上不会手动创建我们自己的数据。相反，我们将使用已经存在的数据。
# 数据可以以多种不同形式和格式中的任何一种存储。到目前为止，
# 其中最基本的是不起眼的CSV文件。当您打开CSV文件时，您会看到如下所示的内容：

# import pandas as pd
# pd.set_option('display.max_columns', 1000)
# pd.set_option('display.width', 1000)
# pd.set_option('display.max_colwidth', 1000)
# data = pd.read_csv('D:\\PyCharm 2018.3.7\\深度学习\\kaggle\\Titanic\\train.csv')
#
# print(data.shape)
# (891, 12)

# print(data.head())
#    PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0            1         0       3  ...   7.2500   NaN         S
# 1            2         1       1  ...  71.2833   C85         C
# 2            3         1       3  ...   7.9250   NaN         S
# 3            4         1       1  ...  53.1000  C123         S
# 4            5         0       3  ...   8.0500   NaN         S
# [5 rows x 12 columns]
#    PassengerId  Survived  Pclass                                                 Name     Sex   Age  SibSp  Parch            Ticket     Fare Cabin Embarked
# 0            1         0       3                              Braund, Mr. Owen Harris    male  22.0      1      0         A/5 21171   7.2500   NaN        S
# 1            2         1       1  Cumings, Mrs. John Bradley (Florence Briggs Thayer)  female  38.0      1      0          PC 17599  71.2833   C85        C
# 2            3         1       3                               Heikkinen, Miss. Laina  female  26.0      0      0  STON/O2. 3101282   7.9250   NaN        S
# 3            4         1       1         Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1      0            113803  53.1000  C123        S
# 4            5         0       3                             Allen, Mr. William Henry    male  35.0      0      0            373450   8.0500   NaN        S

import os, cv2, random
import numpy as np
import pandas as pd
import zipfile

import matplotlib.pyplot as plt
from matplotlib import ticker
import seaborn as sns
# %matplotlib inline

from keras.models import Sequential
from keras.layers import Input, Dropout, Flatten, Convolution2D, MaxPooling2D, Dense, Activation
from keras.optimizers import RMSprop
from keras.callbacks import ModelCheckpoint, Callback, EarlyStopping
from keras.utils import np_utils




# model = catdog()
# 数据分析用的库
import pandas as pd
import math
import numpy as np
import random
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# 可视化用的库
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline


# 机器学习用的库
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC,LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier

def concat_df(df_train,df_test):
    return pd.concat([df_train,df_test],sort=True).reset_index(drop=True)


df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')
combine = [df_train,df_test]
df_all = concat_df(df_train,df_test)
# concat和直接[]链接区别 concat将两个数据表直接合并成一个 []还是两个表


# df_train.describe()

df_train[['Pclass','Survived']].groupby(['Pclass'],as_index=False).mean().sort_values(by='Pclass',ascending=False)
# 对于聚合输出，返回以组标签作为索引的对象。仅与DataFrame输入相关。AS_INDEX=FALSE实际上是“SQL风格”的分组输出。

df_train[['Sex','Survived']].groupby(['Sex'],as_index=False).mean().sort_values(by='Sex',ascending=True)

df_train[['SibSp','Survived']].groupby(['SibSp'],as_index=False).mean().sort_values(by='SibSp',ascending=True)

df_train[['Parch','Survived']].groupby(['Parch'],as_index=False).mean().sort_values(by='Parch',ascending=True)

grid_age = sns.FacetGrid(df_train,col='Survived')
grid_age.map(plt.hist,'Age',bins=20)
# plt.show()

grid_pclass = sns.FacetGrid(df_train,col='Survived',row='Pclass',height=2.2,aspect=1.6)
grid_pclass.map(plt.hist,'Age',alpha=.5,bins=20)
grid_pclass.add_legend()

# plt.show()

grid_embarked = sns.FacetGrid(df_train,row='Embarked',size=2.2,aspect=1.6)
grid_embarked.map(sns.pointplot,'Pclass','Survived','Sex',palatte='deep')
grid_embarked.add_legend()

# a = np.array([[1,0,1],[0,1,0],[1,2,1]])
# b = np.array([[math.sqrt(3)/2,1/2,0],[-1/2,math.sqrt(3)/2,0],[0,0,1]])

grid_fare = sns.FacetGrid(df_train,row='Embarked',col='Survived',size=2.2,aspect=1.6)
grid_fare.map(sns.barplot,'Sex','Fare',alpha=.5,ci=None)
grid_fare.add_legend()

# plt.show()
print(combine[0].shape)

# 对不用的属性进行剔除
df_train = df_train.drop(['Ticket','Cabin'],axis=1)
df_test = df_test.drop(['Ticket','Cabin'],axis=1)
combine = [df_train,df_test]

for dataset in combine:
    dataset['Title'] = dataset.Name.str.extract(' ([A-Za-z]+)\.', expand=False)#匹配姓氏开头 以.为结束

pd.crosstab(df_train['Title'],df_train['Sex'])

for dataset in combine:
    dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

df_train[['Title','Survived']].groupby(['Title'],as_index=False).mean()

Title_Mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Rare": 5}

for dataset in combine:
    dataset['Title'] = dataset['Title'].map(Title_Mapping)
    dataset['Title'] = dataset['Title'].fillna(0)

df_train = df_train.drop(['Name','PassengerId'],axis=1)
df_test = df_test.drop(['Name'],axis=1)
combine = [df_train,df_test]

# for dataset in combine:
#     dataset = dataset.drop(['Name','PassengerId'],axis=1)


# combine[0] = combine[0].drop(['Name','PassengerId'],axis=1)
# combine[1] = combine[1].drop(['Name'],axis=1)


for datase in combine:
    datase['Sex'] = datase['Sex'].map({'female':1,'male':0})
    # datase=datase.drop(['Sex'],axis=1)

grid_pclass_sex = sns.FacetGrid(df_train,row='Pclass',col='Sex',height=2.2,aspect=1.6)
grid_pclass_sex.map(plt.hist,'Age',alpha=.5,bins=20)
grid_pclass_sex.add_legend()

guess_ages = np.zeros((2,3))


for dataset in combine:
    for i in range(0,2):
        for j in range(0,3):
            guess_df = dataset[(dataset['Sex'] == i)&(dataset['Pclass'] == j+1)]['Age'].dropna()
            guess_age = guess_df.median()
            guess_ages[i, j] = int(guess_age / 0.5 + 0.5) * 0.5

    for i in range(0,2):
        for j in range(0,3):
            dataset.loc[(dataset.Age.isnull())&(dataset.Sex == i)&(dataset.Pclass == j+1),'Age'] = guess_ages[i, j]
    dataset['Age'] = dataset['Age'].astype(int)

df_train['AgeBand'] = pd.cut(df_train['Age'],5)
print(df_train[['AgeBand','Survived']].groupby(['AgeBand'],as_index=False).mean().sort_values(by='AgeBand',ascending=True))


for dataset in combine:
    dataset.loc[dataset['Age']<16,'Age'] =0
    dataset.loc[(dataset['Age'] > 16) & (dataset['Age'] <= 32), 'Age'] = 1
    dataset.loc[(dataset['Age'] > 32) & (dataset['Age'] <= 48), 'Age'] = 2
    dataset.loc[(dataset['Age'] > 48) & (dataset['Age'] <= 64), 'Age'] = 3
    dataset.loc[dataset['Age'] > 64, 'Age'] = 4

df_train = df_train.drop(['AgeBand'],axis=1)

df_train['FamilySize'] = df_train['Parch'] + df_train['SibSp'] + 1
df_test['FamilySize'] = df_test ['Parch'] + df_test['SibSp'] + 1


df_train[['FamilySize','Survived']].groupby(['FamilySize'],as_index=False).mean().sort_values(by='Survived',ascending=False)

# for dataset in combine:
#     dataset['IsAlone'] = 0
#     dataset.loc[dataset['FamilySize'] == 1,'IsAlone'] = 1
df_train ['IsAlone'],df_test['IsAlone'] = 0,0
df_train.loc[df_train['FamilySize'] == 1,'IsAlone'] = 1
df_test.loc[df_test['FamilySize'] == 1,'IsAlone'] = 1


#
df_train[['IsAlone','Survived']].groupby(['IsAlone'],as_index=False).mean()

df_train = df_train.drop(['Parch','SibSp','FamilySize'],axis=1)
df_test = df_test.drop(['Parch','SibSp','FamilySize'],axis=1)
combine = [df_train,df_test]

for dataset in combine:
    dataset['Age*Class'] = dataset.Age * dataset.Pclass


fill_port = df_train.Embarked.dropna().mode()[0] #mode函数 统计出现频率最高的

for dataset in combine:
    dataset['Embarked'] = dataset['Embarked'].fillna(fill_port)
    dataset['Embarked'] = dataset['Embarked'].map({'S':0,'C':1,'Q':2}).astype(int)

df_train[['Embarked','Survived']].groupby(['Embarked'],as_index=False).mean().sort_values(by='Survived',ascending=False)

df_test['Fare'].fillna(df_test['Fare'].dropna().median(),inplace=True)

df_train['FareBand'] = pd.qcut(df_train['Fare'], 4)
df_train[['FareBand', 'Survived']].groupby(['FareBand'], as_index=False).mean().sort_values(by='FareBand', ascending=True)

for dataset in combine:
    dataset.loc[dataset['Fare'] <= 7.91, 'Fare'] = 0
    dataset.loc[(dataset['Fare'] > 7.91) & (dataset['Fare'] <= 14.454), 'Fare'] = 1
    dataset.loc[(dataset['Fare'] > 14.454) & (dataset['Fare'] <= 31), 'Fare'] = 2
    dataset.loc[dataset['Fare'] > 31, 'Fare'] = 3
    dataset['Fare'] = dataset['Fare'].astype(int)

df_train = df_train.drop(['FareBand'], axis=1)
combine = [df_train, df_test]

# train_df.head(10)
#  逻辑回归
X_train = df_train.drop('Survived',axis=1)
Y_train = df_train['Survived']
X_test = df_test.drop('PassengerId',axis=1)

logReg = LogisticRegression()
logReg.fit(X_train,Y_train)
Y_predicted = logReg.predict(X_test)
logReg.score(X_train,Y_train)






















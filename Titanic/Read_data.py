import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from matplotlib import style
#We will use the popular scikit-learn library to develop our machine learning algorithms

# Model Helpers
from sklearn.preprocessing import OneHotEncoder,LabelEncoder,StandardScaler
from sklearn.metrics import roc_auc_score,auc

# Models
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron,SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC,LinearSVC
from sklearn.naive_bayes import GaussianNB

import string
import warnings
# warnings.warn("cdc")

# 使用pandas模块读取数据
df_train = pd.read_csv("train.csv")
df_test = pd.read_csv("test.csv")

# concat连接函数，
def concat_df(train_data,test_data):
    return pd.concat([train_data,test_data],sort=True).reset_index(drop=True)

def divide_df(all_data):
    return all_data.loc[:890],all_data.loc[:891:].drop(['Survived'],axis=1)

df_all = concat_df(df_train,df_test)

# print(df_all)
df_train.name = 'Train Set'
df_test.name = 'Test Set'
df_all.name = 'All Set'

dfs = [df_train,df_test]
# Pls note:- df_all and dfs is not same (df_all is a Dataframe and dfs is a list)
df_all.sample(10)

# df_train.info()
# df_train.head() #默认为5
# df_train.tail() #默认为5
# df_train.sample(10)
# df_train.discribe()

# 画图 关于生存人数的比例图
# f1,ax = plt.subplots(1,2,figsize=(18,8))
# df_train['Survived'].value_counts().plot.pie(explode=[0,0.1],autopct='%1.1f%%',ax=ax[0],shadow=True)
#
# ax[0].set_title('Survived')
# ax[0].set_ylabel('')
#
# sns.countplot('Survived',data=df_train,ax=ax[1])
# ax[1].set_title('Survived')

# plt.show()

# 计算丢失属性值的属性个数
total_missing_train = df_train.isnull().sum().sort_values(ascending=False)

percent_1 = df_train.isnull().sum()/df_train.isnull().count()*100
percent_2 = (round(percent_1,1)).sort_values(ascending=False)

train_missing_data = pd.concat([total_missing_train,percent_2],axis=1,keys=['total','%'])

# print(total_missing_train)
# print('_'*25)
# print(train_missing_data.head(5))

total_missing_test = df_test.isnull().sum().sort_values(ascending=False)

percent_3 = df_test.isnull().sum()/df_test.isnull().count()*100
percent_4 = (round(percent_3,1)).sort_values(ascending=False)

test_missing_data = pd.concat([total_missing_test,percent_4],axis=1,keys=['total','%'])

# print(total_missing_test)
# print('_'*25)
# print(test_missing_data.head(5))

#
# f,ax = plt.subplot(figsize=(18,8))
# 画图关于存活人数与Pclass和Age之间的关系
# f2,ax=plt.subplots(figsize=(18,8))
# sns.violinplot("Pclass","Age",hue="Survived",data=df_train,split=True,ax=ax)
# ax.set_title('Pclass and Age vs Survived')
# ax.set_yticks(range(0,110,10))
# plt.show()

# link --> https://www.geeksforgeeks.org/python-pandas-dataframe-corr/
df_all_corr = df_all.corr().abs().unstack().sort_values(kind="quicksort", ascending=False).reset_index()

df_all_corr.rename(columns={"level_0": "Feature 1", "level_1": "Feature 2", 0: 'Correlation Coefficient'}, inplace=True)

co = df_all_corr[df_all_corr['Feature 1'] == 'Pclass']

#  找到年龄和性别与存活率=之间的关系

# f,ax = plt.subplots(figsize=(18,8))

# link --> http://alanpryorjr.com/visualizations/seaborn/violinplot/violinplot/
# sns.violinplot("Sex","Age",hue="Survived" ,data=df_train,split=True,ax=ax)
# ax.set_title('Sex and Age VS Survived')
# ax.set_yticks(range(0,110,10))

# plt.show()

# link ---> https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/
age_by_pclass_sex = df_all.groupby(['Sex','Pclass']).median()['Age']

# for pclass in range(1,4):
#     for sex in ['female','male']:
#         print('median age of pclass {} {}s: {}'.format(pclass,sex ,age_by_pclass_sex[sex][pclass].astype(int)))

# filling the missing values
df_all['Age'] = df_all.groupby(['Sex','Pclass'])['Age'].apply(lambda x:x.fillna(x.median()))

# 存活率与EMbark的关系
# https://www.w3schools.com/python/python_lambda.asp

# sns.factorplot('Embarked','Survived',data=df_train)
# fig = plt.gcf() # pyplot.gcf() 用来获得当前的图片
# fig.set_size_inches(5,3)
# plt.show()

# df_all[df_all['Embarked'].isnull()]

df_all['Embarked'] = df_all['Embarked'].fillna('S')

# 接下来讨论Embarked与存活率之间的关系

# https://www.kaggle.com/residentmario/faceting-with-seaborn
# FacetGrid = sns.FacetGrid(df_train,row='Embarked',height = 4.5,aspect = 1.6)
# https://www.geeksforgeeks.org/python-seaborn-pointplot-method/
# FacetGrid.map(sns.pointplot,'Pclass','Survived','Sex')
# 绘制图例，也许将其放置在轴外并调整图的大小。
# FacetGrid.add_legend() #
# plt.show()

# fare 与 Survived  之间的关系

# df_all['Fare'].isnull().sum()
# There is only one passenger with missing Fare value.
# We can assume that Fare is related to family size (Parch and SibSp)
# and Pclass features. Median Fare value of a male with a third class
# ticket and no family is a logical choice to fill the missing value.

med_fare = df_all.groupby(['Pclass','Parch','SibSp'])['Fare'].median()[3][0][0]
df_all['Fare'] = df_all['Fare'].fillna(med_fare)

# Pclass
# link --> https://www.geeksforgeeks.org/seaborn-barplot-method-in-python/
# sns.barplot(x='Pclass',y='Survived',hue='Sex',data=df_train)
# plt.show()

# grid = sns.FacetGrid(df_train,col='Survived',row='Pclass',height=2.2,aspect=1.6)
# grid.map(plt.hist,'Age',alpha=.5,bins=20)
# grid.add_legend()
# plt.show()

# SibSp and Parch

data1 = df_train.copy()
data1['Family_size'] = data1['SibSp']+data1['Parch']

# axex = sns.factorplot('Family_size','Survived',data = data1,aspect = 2.5,)
# plt.show()

# Cabin

df_all['Deck'] = df_all['Cabin'].apply(lambda s:s[0] if pd.notnull(s) else 'M')
df_all_deck = df_all.groupby(['Deck','Pclass']).count().drop(columns=['Survived','Sex','Age','SibSp','Parch','Fare','Embarked','Cabin','PassengerId','Ticket'])\
    .rename(columns={'Name':'Count'})

df_all_deck = df_all_deck.transpose()

def get_pclass_dist(df_all_deck):
    # 为每一个乘客类型创建一个字典
    deck_counts = {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'G': {}, 'M': {}, 'T': {}}
    decks = df_all_deck.columns.levels[0]
    # print(deck)
    # 如果为空，则仅在各自的Pclass中创建一个df_all_decks的副本，副本为0
    for deck in decks:
        for pclass in range(1,4):
            try:
                count = df_all_deck[deck][pclass][0]
                deck_counts[deck][pclass] = count
            except  KeyError:
                deck_counts[deck][pclass] = 0
    # print(deck_counts)
    df_decks = pd.DataFrame(deck_counts)

    deck_percentages = {}
    for col in df_decks.columns:
        deck_percentages[col] = [(count / df_decks[col].sum()) * 100 for count in df_decks[col]]
    return deck_counts,deck_percentages,df_decks
all_deck_counts,all_deck_percentage,all_decks = get_pclass_dist(df_all_deck)


def display_pclass_dist(all_deck_percentage):
    # 将字典转换为数据框，然后转置
    df_percentage = pd.DataFrame(all_deck_percentage).transpose()
    decks_name = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'M', 'T')
    bar_count = np.arange(len(decks_name))
    bar_width = 0.85

    pclass1 = df_percentage[0]
    pclass2 = df_percentage[1]
    pclass3 = df_percentage[2]

    plt.figure(figsize=(20,10))
    # link --> https://www.tutorialspoint.com/matplotlib/matplotlib_bar_plot.htm
    plt.bar(bar_count, pclass1, width=bar_width, edgecolor='white', label='Passenger Class 1')
    plt.bar(bar_count, pclass2, bottom=pclass1, color='#f9bc86', edgecolor='white', width=bar_width,
            label='Passenger Class 2')
    plt.bar(bar_count, pclass3, bottom=pclass1 + pclass2, color='#a3acff', edgecolor='white', width=bar_width,
            label='Passenger Class 3')

    plt.xlabel('Deck', size=15, labelpad=20)
    plt.ylabel('Passenger Class Percentage', size=15, labelpad=20)
    plt.xticks(bar_count, decks_name)
    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=15)

    plt.legend(loc='best', bbox_to_anchor=(1, 1), prop={'size': 15})
    plt.title('Passenger Class Distribution in Decks', size=18, y=1.05)

    plt.show()
# display_pclass_dist(all_deck_percentage)

# 将原本为T的deck值变为A ？？？
idx = df_all[df_all['Deck'] == 'T'].index
df_all.loc[idx,'Deck'] ='A'

df_all_decks_survived = df_all.groupby(['Deck', 'Survived']).count().drop(
    columns=['Sex', 'Age', 'SibSp', 'Parch', 'Fare',
             'Embarked', 'Pclass', 'Cabin', 'PassengerId', 'Ticket']).rename(columns={'Name': 'Count'}).transpose()


def get_survived_dist(df):
    # Creating a dictionary for every survival count in every deck
    surv_counts = {'A': {}, 'B': {}, 'C': {}, 'D': {}, 'E': {}, 'F': {}, 'G': {}, 'M': {}}
    decks = df.columns.levels[0]

    for deck in decks:
        for survive in range(0, 2):
            surv_counts[deck][survive] = df[deck][survive][0]

    df_surv = pd.DataFrame(surv_counts)
    surv_percentages = {}

    for col in df_surv.columns:
        surv_percentages[col] = [(count / df_surv[col].sum()) * 100 for count in df_surv[col]]

    return surv_counts, surv_percentages


def display_surv_dist(percentages):
    df_survived_percentages = pd.DataFrame(percentages).transpose()
    deck_names = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'M')
    bar_count = np.arange(len(deck_names))
    bar_width = 0.85

    not_survived = df_survived_percentages[0]
    survived = df_survived_percentages[1]

    plt.figure(figsize=(20, 10))
    plt.bar(bar_count, not_survived, color='#b5ffb9', edgecolor='white', width=bar_width, label="Not Survived")
    plt.bar(bar_count, survived, bottom=not_survived, color='#f9bc86', edgecolor='white', width=bar_width,
            label="Survived")

    plt.xlabel('Deck', size=15, labelpad=20)
    plt.ylabel('Survival Percentage', size=15, labelpad=20)
    plt.xticks(bar_count, deck_names)
    plt.tick_params(axis='x', labelsize=15)
    plt.tick_params(axis='y', labelsize=15)

    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), prop={'size': 15})
    plt.title('Survival Percentage in Decks', size=18, y=1.05)

    plt.show()


# all_surv_count, all_surv_per = get_survived_dist(df_all_decks_survived)
# display_surv_dist(all_surv_per)

df_all['Deck'] = df_all['Deck'].replace(['A','B','C'],'ABC')
df_all['Deck'] = df_all['Deck'].replace(['D','E'],'DE')
df_all['Deck'] = df_all['Deck'].replace(['F','G'],'FG')


# After filling the missing values in Age, Embarked, Fare and Deck features,
# there is no missing value left in both training and test set. Cabin is dropped because Deck feature is used instead of it.

# drop Cabin

df_all.drop(['Cabin'],axis=1,inplace=True) #axis=1 删除列 =0 删除行 inplace=1 表示将原数组直接替代

df_train,df_test = divide_df(df_all)

dfs2 = [df_train,df_test]

# for df in dfs2:
#     print(df.isnull().sum())
#     print('-'*20)

# cont_features = ['Age', 'Fare']
# surv = df_train['Survived'] == 1
#
# fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(20, 20))
# plt.subplots_adjust(right=1.5)
#
# for i, feature in enumerate(cont_features):  # link --> https://www.geeksforgeeks.org/enumerate-in-python/
#     # Distribution of survival in feature
#     sns.distplot(df_train[~surv][feature], label='Not Survived', hist=True, color='#e74c3c', ax=axs[0][i])
#     # [-surv] means "Not Survived"
#     sns.distplot(df_train[surv][feature], label='Survived', hist=True, color='#2ecc71', ax=axs[0][i])
#
#     # Distribution of feature in dataset
#     sns.distplot(df_train[feature], label='Training Set', hist=False, color='#e74c3c', ax=axs[1][i])
#     sns.distplot(df_test[feature], label='Test Set', hist=False, color='#2ecc71', ax=axs[1][i])
#
#     axs[0][i].set_xlabel('')
#     axs[1][i].set_xlabel('')
#
#     # just providing the ticks for x & y axis in respective plots
#     for j in range(2):
#         axs[i][j].tick_params(axis='x', labelsize=20)
#         axs[i][j].tick_params(axis='y', labelsize=20)
#
#     axs[0][i].legend(loc='upper right', prop={'size': 20})
#     axs[1][i].legend(loc='upper right', prop={'size': 20})
#     axs[0][i].set_title('Distribution of Survival in {}'.format(feature), size=20, y=1.05)
#
# axs[1][0].set_title('Distribution of {} Feature'.format('Age'), size=20, y=1.05)
# axs[1][1].set_title('Distribution of {} Feature'.format('Fare'), size=20, y=1.05)
#
# plt.show()

# Distribution of Age feature clearly shows that children younger than 15 has a higher survival rate than any of the other age groups
# In distribution of Fare feature, the survival rate is higher on distribution tails. The distribution also has positive skew because
# of the extremely large outliers

# cat_features = ['Embarked','Parch','Pclass','Sex','SibSp','Deck']
#
# fig,axs = plt.subplots(ncols=2,nrows=3,figsize=(20,20))
# plt.subplots_adjust(right=1.5,top=1.25)
#
# for i,feature in enumerate(cat_features,1):
#     plt.subplot(2,3,i)
#     sns.countplot(x=feature,hue='Survived',data = df_train)
#
#     plt.xlabel('{}'.format(feature),size = 20,labelpad=15)
#     plt.ylabel('Passenger Count',size = 20,labelpad=15)
#     plt.tick_params(axis='x',labelsize=20)
#     plt.tick_params(axis='y',labelsize=20)
#
#     plt.legend(['Not Survived','Survived'],loc = 'upper center',prop = {'size':18})
#     plt.title('Count of Survived in {} Feature'.format(feature),size = 20 ,y=1.05)
#
# plt.show()


# 每个分类特征都有至少一个具有高死亡率的类别。 这些课程对于预测乘客是幸存者还是受害者很有帮助。
# 最好的分类特征是Pclass和Sex，因为它们具有最均匀的分布。
#
# 与其他港口相比，从南安普敦登上的乘客的生存率较低。 从瑟堡登机的乘客中有一半以上幸存下来。 该观察结果可能与Pclass功能有关
# Parch和SibSp的功能表明只有一个家庭成员的乘客的生存率更高

# 大多数功能是相互关联的。 此关系可用于通过要素转换和要素交互来创建新要素。 由于与Survived功能的高度相关性，目标编码也可能非常有用。
# 在连续要素中可见分裂点和尖峰。 使用决策树模型可以轻松捕获它们，但是线性模型可能无法发现它们。
# 分类特征具有非常不同的分布，具有不同的生存率。 这些功能可以进行一键编码。 这些功能中的某些功能可能会相互组合以形成新功能。
# 在“探索性数据分析”部分创建了一个称为“甲板”的新功能，并删除了机舱功能。

df_all = concat_df(df_train,df_test)

# Correlation Between The Features
#  https://likegeeks.com/seaborn-heatmap-tutorial/
# sns.heatmap(df_all.corr(),annot=True,cmap='RdYlGn',linewidths=0.2)
# fig = plt.gcf()
# fig.set_size_inches(10,8)
# plt.show()

# 6. Feature Engineering
df_all['Fare'] = pd.qcut(df_all['Fare'], 13) # visit the link above
# fig, axs = plt.subplots(figsize=(22, 9))
# sns.countplot(x='Fare', hue='Survived', data=df_all)
#
# plt.xlabel('Fare', size=15, labelpad=20)
# plt.ylabel('Passenger Count', size=15, labelpad=20)
# plt.tick_params(axis='x', labelsize=10)
# plt.tick_params(axis='y', labelsize=15)
#
# plt.legend(['Not Survived', 'Survived'], loc='upper right', prop={'size': 15})
# plt.title('Count of Survival in {} Feature'.format('Fare'), size=15, y=1.05)
#
# plt.show()

# 年龄特征具有正态分布，带有一些尖峰和颠簸，并且将10个基于分位数的垃圾箱用于年龄。
# 第一个容器的生存率最高，第四个容器的生存率最低。 这些是分布中的最大峰值。
# 在此过程中还捕获了一个不寻常的群体（34.0，40.0），它们具有很高的生存率。

# df_all['Age'] = pd.qcut(df_all['Age'],10)
#
# fig,axs = plt.subplots(figsize=(22,9))
# sns.countplot(x='Age',hue='Survived',data=df_all)
#
# plt.xlabel('Age',size=15,labelpad=20)
# plt.ylabel('Passenger counts',size=15,labelpad=20)
# plt.tick_params(axis='x',labelsize=15)
# plt.tick_params(axis='y',labelsize=15)
#
# plt.legend(['Not Survived','Survived'],loc='upper right',prop= {'size':15})
# plt.title('Survival counts in {} feature '.format('Age'),size=15,y=1.05)
#
# plt.show()

# Family_Size是通过添加SibSp，Parch和1来创建的。SibSp是兄弟姐妹和配偶的计数，而Parch是父母和孩子的计数。
# 添加这些列是为了找到家庭的总人数。 最后乘以1是当前乘客。 图形清楚地表明，家庭人数是生存的预测指标，因为不同的值具有不同的生存率。
# 带1的家庭人数标记为“单独”
# 2、3和4的家庭人数标记为“小”
# 5和6的家庭人数标记为中
# 7、8和11的家庭人数标记为大

# df_all['Family_Size'] = df_all['SibSp'] + df_all['Parch'] + 1
#
# fig, axs = plt.subplots(figsize=(20, 20), ncols=2, nrows=2)
# plt.subplots_adjust(right=1.5)
#
# sns.barplot(x=df_all['Family_Size'].value_counts().index, y=df_all['Family_Size'].value_counts().values, ax=axs[0][0])
# sns.countplot(x='Family_Size', hue='Survived', data=df_all, ax=axs[0][1])
#
# axs[0][0].set_title('Family Size Feature Value Counts', size=20, y=1.05)
# axs[0][1].set_title('Survival Counts in Family Size ', size=20, y=1.05)
#
# # Mapping Family Size
# family_map = {1: 'Alone', 2: 'Small', 3: 'Small', 4: 'Small', 5: 'Medium', 6: 'Medium', 7: 'Large', 8: 'Large', 11: 'Large'}
# df_all['Family_Size_Grouped'] = df_all['Family_Size'].map(family_map)
#
# sns.barplot(x=df_all['Family_Size_Grouped'].value_counts().index, y=df_all['Family_Size_Grouped'].value_counts().values, ax=axs[1][0])
# sns.countplot(x='Family_Size_Grouped', hue='Survived', data=df_all, ax=axs[1][1])
#
# axs[1][0].set_title('Family Size Feature Value Counts After Grouping', size=20, y=1.05)
# axs[1][1].set_title('Survival Counts in Family Size After Grouping', size=20, y=1.05)
#
#
# for i in range(2):
#     axs[i][1].legend(['Not Survived', 'Survived'], loc='upper right', prop={'size': 20})
#     for j in range(2):
#         axs[i][j].tick_params(axis='x', labelsize=20)
#         axs[i][j].tick_params(axis='y', labelsize=20)
#         axs[i][j].set_xlabel('')
#         axs[i][j].set_ylabel('')
#
# plt.show()

# 要分析的唯一票证值太多，因此按频率将它们分组可以使事情变得更容易。
# 此功能与Family_Size有何不同？许多乘客与团体同行。这些团体由朋友，保姆，女佣等组成。虽然不算家庭，但他们使用的票相同。
# 为什么不按票证的前缀对票证进行分组？如果票证功能中的前缀具有任何含义，则它们已在Pclass或Embarked功能中捕获，
# 因为这可能是可以从票证功能派生的唯一逻辑信息。
# 根据下图，具有2,3和4个成员的组的生存率更高。独自旅行的乘客存活率最低。经过4个小组成员，生存率急剧下降。此模式与Family_Size功能非常相似，
# 但有细微差别。 Ticket_Frequency值没有像Family_Size那样分组，因为这基本上可以创建具有完美相关性的相同功能。这种功能不会提供任何其他信息。

# df_all['Ticket_Frequency'] = df_all.groupby('Ticket')['Ticket'].transform('count')
#
# fig,axs = plt.subplots(figsize=(12,9))
# sns.countplot(x='Ticket_Frequency',hue='Survived',data=df_all)
#
# plt.xlabel('Ticket_Frequcy',size=15,labelpad=20)
# plt.ylabel('Passneger Count',size=15,labelpad=20)
# plt.tick_params(axis='x',labelsize=15)
# plt.tick_params(axis='y',labelsize=15)
#
# plt.legend(['Not Survived','Survived'],loc='upper right',prop={'size':15})
# plt.title('Count of Survived in {} feature'.format('Ticket_Frequency'),size=15 ,y=1.05)
#
# plt.show()


# 通过提取名称功能之前的前缀来创建标题。 根据下图，出现很多标题的次数很少。 其中一些标题似乎不正确，需要替换。
# 小姐，夫人，女士，夫人，夫人，女士，伯爵夫人，多娜的头衔被小姐/夫人/女士取代，因为他们都是女性。
# 诸如Mlle，Mme和Dona之类的值实际上是乘客的姓名，但由于名称功能由逗号分隔，因此它们被归类为标题。
# Dr，Col，Major，Jonkheer，Capt，Sir，Don和Rev职称被Dr / Military / Noble / Clergy取代，
# 因为这些乘客具有相似的特征。 大师是唯一的头衔。 它适用于26岁以下的男性乘客。在所有男性中，他们的生存率最高。

# Is_Married是基于Mrs标题的二进制功能。 夫人头衔在其他女性头衔中具有最高的成活率。 此标题必须是一项功能，因为所有女性标题都相互分组。




# 7.Building Machine Learning Models






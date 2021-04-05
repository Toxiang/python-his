import pandas as pd
import os
import zipfile
import matplotlib.pyplot as plt


# DataFrame
# DataFrame是一个表。它包含单个条目的数组，每个条目都有一个特定值。每个条目对应于一行(或记录)和一列。
pd.DataFrame({'one':[1,2],'Two':[3,4]})
# Out[3]:
#    one  Two
# 0    1    3
# 1    2    4

# 我们使用pd.DataFrame()构造函数来生成这些DataFrame对象。
# 声明新条目的语法是一个字典，它的键是列名(在本例中是AB和CD)，
# 值是一个条目列表。这是构造新DataFrame的标准方法，也是您最有可能遇到的方法
pd.DataFrame({'one':['aaa','bbb'],'Two':['ccc','ddd']},index=['AB','CD'])
# Out[4]:
#     one  Two
# AB  aaa  ccc
# CD  bbb  ddd

# Series

# 相比之下，序列是数据值的序列。如果DataFrame是一个表，那么Series就是一个列表。
# 事实上，您可以创建一个列表，而不只是一个列表：

pd.Series([1,2,3,4,5])
# Out[5]:
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

pd.Series([1,2,3],index=['one','two','three'],name='A')
# Out[6]:
# one      1
# two      2
# three    3
# Name: A, dtype: int64


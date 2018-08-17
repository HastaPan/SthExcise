
# coding: utf-8

# In[1]:


# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import geohash2 as gh
# 保证生成的图片在浏览器内显示
#get_ipython().run_line_magic('matplotlib', 'inline')
# 保证能正常显示中文(Mac)
plt.rcParams['font.family'] = ['Arial Unicode MS']


# In[2]:


data_test = pd.read_csv('E:\\data\\MOBIKE_CUP_2017\\test.csv')
print('This is the test data******************** ')
print(data_test)
print('*************************')
data_train = pd.read_csv('E:\\data\\MOBIKE_CUP_2017\\train.csv')
print('This is the train data************')
print(data_train)
print('********************')
data_sample = pd.read_csv('E:\\data\\MOBIKE_CUP_2017\\mobike_sample_submission.csv')
print('This is the mobike_sample_submission************')
print(data_sample)
print('********************')


# In[3]:


#于此无关，只是看一下摩拜大赛的结果
data_submission = pd.read_csv('E:\\data\\MOBIKE_CUP_2017\\submission.csv')
print('This is the mobike_submission************')
print(data_submission)
print('********************')


# In[4]:


#查看数据的头部
data_test_head = data_test.head()
print('This is the test data head******************** ')
print(data_test_head)
print('*************************')
data_test_tail=data_test.tail()
print('This is the test data tail******************** ')
print(data_test_tail)
print('*************************')


# In[5]:


#数据初步统计
data_test_describe = data_test.describe()
print(data_test_describe)


# In[6]:


#数据类型查看
print(data_test.dtypes)


# In[7]:


#删除存在缺失值的样本
data_test_dropna=data_test.dropna()
print(data_test_dropna)


# In[8]:


#数据进行排序
data_test_sort_orderid = data_test.sort_values(by = 'orderid')
print(data_test_sort_orderid)


# In[9]:


#将日期列拆分
data_test['start_year'] = pd.DatetimeIndex(data_test['starttime']).year
data_test['start_month'] = pd.DatetimeIndex(data_test['starttime']).month
data_test['start_weekday'] = pd.DatetimeIndex(data_test['starttime']).weekday
print('This is the test data******************** ')
print(data_test)
print('*************************')


# In[10]:


#统计一些数据
data_test_group_biketype = data_test.groupby(['biketype']).count()
print(data_test_group_biketype)


# In[11]:


#计算 biketype 
data_test_biketype_counter=Counter(data_test['biketype'])
print(data_test_biketype_counter)


# In[12]:


#计算周几骑车人多
data_test_start_weekday_counter=Counter(data_test['start_weekday'])
print(data_test_start_weekday_counter)


# In[13]:


#计算几月骑车人多
data_test_start_month_counter=Counter(data_test['start_month'])
print(data_test_start_month_counter)


# In[14]:


#计算哪年骑车人多
data_test_start_year_counter=Counter(data_test['start_year'])
print(data_test_start_year_counter)


# In[15]:


#计算深度用户
data_test_userid_counter=Counter(data_test['userid']).most_common(100)
print(data_test_userid_counter)


# In[16]:


#计算被用的多的车
data_test_bikeid_counter=Counter(data_test['bikeid']).most_common(100)
print(data_test_bikeid_counter)


# In[17]:


#计算繁忙的点
data_test_start_loc_counter_all=Counter(data_test['geohashed_start_loc'])
data_test_start_loc_counter=Counter(data_test['geohashed_start_loc']).most_common(100)
print(data_test_start_loc_counter)


# In[19]:


#print(list(data_test_start_loc_counter))

#print(data_test_start_loc_counter_all.items())
data_test_start_loc_counter_all_dit = dict(data_test_start_loc_counter_all)
print(data_test_start_loc_counter_all_dit)



# In[21]:


#data_test['ll_start_loc'] = pd.loc(data_test['geohashed_start_loc'])
data_test_hashed_start_loc = data_test['geohashed_start_loc']
print(data_test_hashed_start_loc)
data_test_ll_start_loc = gh.decode(data_test_hashed_start_loc)
print(data_test_ll_start_loc)


# In[18]:


print(data_test_start_loc_counter_all.elem())


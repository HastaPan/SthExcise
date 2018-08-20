
# coding: utf-8

# In[65]:


# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator
from collections import Counter
#import geohash2 as gh
# 保证生成的图片在浏览器内显示
get_ipython().run_line_magic('matplotlib', 'inline')
# 保证能正常显示中文(Mac)
plt.rcParams['font.family'] = ['Arial Unicode MS']


# In[66]:


#path = 'E:\\data\\MOBIKE_CUP_2017\\test.csv'
#data_train = pd.read_csv('E:\\data\\MOBIKE_CUP_2017\\train.csv')
#data_sample = pd.read_csv('E:\\data\\MOBIKE_CUP_2017\\mobike_sample_submission.csv')
#Mobike 大赛结果
#E:\\data\\MOBIKE_CUP_2017\\submission.csv'


# In[67]:


#def Read_Data(path,dataname):
    #data_test = pd.read_csv(path)
    #print('This is the '+dataname+'******************** ')
   #print(data_test)
    #print('*************************')


# In[68]:


def Read_Data(path,dataname):
    data = pd.read_csv(path)
    return data
    PrintSth(dataname,data)


# In[69]:


def PrintSth(dataname,data):
    print('This is the '+dataname+'******************** ')
    print(data)
    print('*************************')


# In[70]:


def Data_Process(data):
    Data_Head_Out(data)
    Data_Tail_Out(data)
    Data_Describe_Out(data)
    Data_Dtypes_Out(data)
    Data_Dropna_Out(data)


# In[71]:


def Data_Head_Out(data):
    data_head = data.head()
    PrintSth('data head',data_head)


# In[72]:


def Data_Tail_Out(data):
    data_tail = data.tail()
    PrintSth('data tail',data_tail)


# In[73]:


#数据描述
def Data_Describe_Out(data):
    data_describe= data.describe()
    PrintSth('data describe',data_describe)


# In[74]:


#数据类型查看
def Data_Dtypes_Out(data):
    data_dtypes= data.dtypes
    PrintSth('data type',data_dtypes)


# In[75]:


#删除存在缺失值的样本
def Data_Dropna_Out(data):
    data_dropna= data.dropna()
    PrintSth('data dropna',data_dropna)


# In[76]:


#统计各类型数据的数量
def Group(data,dataname，typename):
    dataname = data.groupby([typename]).count()
    print(dataname)


# In[77]:


data_test=Read_Data('E:\\data\\MOBIKE_CUP_2017\\test.csv','data_test')


# In[78]:


#Data_Head_Out(data_test)
Data_Process(data_test)


# In[79]:


#将日期列拆分
data_test['start_year'] = pd.DatetimeIndex(data_test['starttime']).year
data_test['start_month'] = pd.DatetimeIndex(data_test['starttime']).month
data_test['start_weekday'] = pd.DatetimeIndex(data_test['starttime']).weekday
print('This is the test data******************** ')
print(data_test)
print('*************************')


# In[80]:


#统计不同类型数据,并排序
#第三个参数确定是否要排序,如果要排序，istime=1，如果不需要排序istime =0
def Counter_Data(data, typename,istime):
    data_counter=Counter(data[typename])
    #这是周，月，年数据需要排序，其他类型数据不需要排序
    #加一个参数，如果是日，周，月，年等时间数据进行排序，否则不排序
    if istime:
        data_counter_sorted=sorted(data_counter.items(),key=operator.itemgetter(0))
    else:
        data_counter_sorted = sorted(data_counter.items(),key=operator.itemgetter(1),reverse=True)
    
    return data_counter_sorted


# In[57]:


data_counter_sorted = Counter_Data(data_test,'biketype',0)   
    
x=[]
y=[]
for i ,val in enumerate(data_counter_sorted):
    x.append(val[0])
    y.append(val[1])
x=x[0:20]
y=y[0:20]
print(x)
print(y)


# In[58]:


#设置画图值得类
#这种方式对每个参数单独初始化
class Picture_Part_Setting():
    def __init__(self,color='kkkk'):
        self.xlab = ''
        self.ylab = ''
        self.color=color
        self.title = ''
        self.osd =''
        self.figsize = (15,8)
        self.dpi = 100
        self.width = 0.3
        self.loc = 'best'     
a= Picture_Part_Setting('xze')
a.xlab="hello"

print(a.xlab)
print(a.osd)
print(a.color)


# In[82]:


#设置画图值得类
#这种方式对参数一体化初始化
class Picture_Part_Setting():
    def __init__(self,xlab,ylab,title,label,unit,picture_name,width=0.3,color='#509839',loc='best',figsize=(15,8),dpi=100):
        self.xlab =xlab
        self.ylab = ylab
        self.title = title
        self.label = label
        self.unit = unit
        self.picture_name = picture_name
        self.width = width
        self.color = color
        self.loc = loc
        self.figsize = figsize
        self.dpi = dpi 
    
    
    def Print_Chart_Figure(self,data_counter_sorted):
        
            #处理数据，为X轴和Y轴填充数据
        x=[]
        y=[]
        for i ,val in enumerate(data_counter_sorted):
            x.append(val[0])
            y.append(val[1])

    # 设置画板属性
        plt.figure(self.figsize, self.dpi)
    
    # width以x为基准,向右为正,向左为负(如果多了,就需要为基准x加减相应的数值)
    #color="#509839  c03035")
        plt.bar(x, y, self.width, self.label, self.color)
    
    #这块固定了，需要处理成动态变化的
    #x轴画图
        x_ = x
        x_desc = ["{}".format(x_desc) for x_desc in data_counter_sorted]
        x_desc.insert(100, "")

        #y轴画图
        y_ = y
        y_desc = ["{}"+self.unit.format(y_desc) for y_desc in range(0, 35000)][::500]
        # x轴的数值和描述
        plt.xticks(x_, x_desc)
        plt.yticks(y_, y_desc)

        plt.xlabel(self.xlab)
        plt.ylabel(self.ylab)
        plt.title(self.title)
        plt.legend(self.loc)
        plt.savefig("./{}.png".format(self.picture.name))
        plt.show()           


# In[83]:


a= Picture_Part_Setting('车型','数量','各类自行车数量','数量','辆','SUIYI')
data_test_type=Counter_Data(data_test,'biketype',1)
a.Print_Chart_Figure(data_test_type)


# In[ ]:


def Print_Chart_Figure(data_counter_sorted):
    #处理数据，为X轴和Y轴填充数据
    x=[]
    y=[]
    for i ,val in enumerate(data_counter_sorted):
        x.append(val[0])
        y.append(val[1])

    # 设置画板属性
    plt.figure(figsize = (15, 8), dpi = 100)
    
    # width以x为基准,向右为正,向左为负(如果多了,就需要为基准x加减相应的数值)
    #color="#509839  c03035")
    plt.bar(x, y, width= 0.5, label="数量", color="#509839")
    
    #这块固定了，需要处理成动态变化的
    #x轴画图
    x_ = x
    x_desc = ["{}".format(x_desc) for x_desc in data_counter_sorted]
    x_desc.insert(100, "")
    
    #y轴画图
    y_ = y
    y_desc = ["{}辆".format(y_desc) for y_desc in range(0, 35000)][::500]
    # x轴的数值和描述
    plt.xticks(x_, x_desc)
    plt.yticks(y_, y_desc)
    
    plt.xlabel("车型")
    plt.ylabel("数量")
    plt.title("各类行车的数量")
    plt.legend(loc="best")
    plt.savefig("./bikeweek9.png")
    plt.show()


# In[ ]:


def Print_Chart_Figure(data_counter_sorted):
    #处理数据，为X轴和Y轴填充数据
    x=[]
    y=[]
    for i ,val in enumerate(data_counter_sorted):
        x.append(val[0])
        y.append(val[1])

    # 设置画板属性
    plt.figure(figsize = (15, 8), dpi = 100)
    
    # width以x为基准,向右为正,向左为负(如果多了,就需要为基准x加减响应的数值)
    #plt.bar(x, y, width= -0.3, label="现实年龄", color="#509839  c03035")
    plt.bar(x, y, width= 0.5, label="数量", color="#509839")
    
    #这块固定了，需要处理成动态变化的
    #x轴画图
    x_ = x
    x_desc = ["{}".format(x_desc) for x_desc in data_counter_sorted]
    x_desc.insert(100, "")
    
    #y轴画图
    y_ = y
    y_desc = ["{}辆".format(y_desc) for y_desc in range(0, 35000)][::500]
    # x轴的数值和描述
    plt.xticks(x_, x_desc)
    plt.yticks(y_, y_desc)
    
    plt.xlabel("车型")
    plt.ylabel("数量")
    plt.title("各类行车的数量")
    plt.legend(loc="best")
    plt.savefig("./bikeweek9.png")
    plt.show()


# In[ ]:


print(Counter_Data(data_test,'biketype',1))


# In[ ]:


data_test_type=(Counter_Data(data_test,'biketype',1))
Print_Chart_Figure(data_test_type)


# In[12]:


#计算周几骑车人多
data_test_start_weekday_counter=Counter(data_test['start_weekday'])
data_test_start_weekday_counter_sorted = sorted(data_test_start_weekday_counter.items(),key=operator.itemgetter(0))
print(data_test_start_weekday_counter_sorted)


# In[57]:


x=[]
y=[]
for i ,val in enumerate(data_test_start_weekday_counter_sorted):
    x.append(val[0])
    y.append(val[1])
print(x)
print(y)


# In[65]:


#条形图

# 条形图绘制名侦探柯南主要角色年龄
#role_list =data_test_start_weekday_counter_sorted.keys()
#role_age = data_test_start_weekday_counter_sorted.values()
# 实际年龄
x=[]
y=[]
for i ,val in enumerate(data_test_start_weekday_counter_sorted):
    x.append(val[0])
    y.append(val[1])
print(x)
print(y)
#x = [data_test_start_weekday_counter_sorted[i] for i in range(1, len(data_test_start_weekday_counter_sorted)+1)][0]

#y = [data_test_start_weekday_counter_sorted[i] for i in range(1, len(data_test_start_weekday_counter_sorted)+1)][1]
#x= [0,1,2,3,4,5,6]
#y=[230542,231381,289707,324215,335853,342868,248430]

# 设置画板属性
plt.figure(figsize = (15, 8), dpi = 100)

# width以x为基准,向右为正,向左为负(如果多了,就需要为基准x加减响应的数值)
#plt.bar(x, y, width= -0.3, label="现实年龄", color="#509839  c03035")
plt.bar(x, y, width= 0.5, label="数量", color="#509839")


x_ = x
x_desc = ["{}".format(x_desc) for x_desc in data_test_start_weekday_counter_sorted]
x_desc.insert(100, "")

y_ = y
y_desc = ["{}辆".format(y_desc) for y_desc in range(0, 35000)][::500]

# x轴的数值和描述
plt.xticks(x_, x_desc)
plt.yticks(y_, y_desc)

plt.xlabel("车型")
plt.ylabel("数量")
plt.title("各类行车的数量")
plt.legend(loc="best")
plt.savefig("./bikeweek2.png")
plt.show()


# In[17]:


#计算几月骑车人多
data_test_start_month_counter=Counter(data_test['start_month'])
print(data_test_start_month_counter)


# In[ ]:


#计算哪年骑车人多
data_test_start_year_counter=Counter(data_test['start_year'])
print(data_test_start_year_counter)


# In[ ]:


#计算深度用户
data_test_userid_counter=Counter(data_test['userid']).most_common(100)
print(data_test_userid_counter)


# In[ ]:


#计算被用的多的车
data_test_bikeid_counter=Counter(data_test['bikeid'])
#print(data_test_bikeid_counter)
data_test_bikeid_counter_keys=data_test_bikeid_counter.keys()
data_test_bikeid_counter_values=data_test_bikeid_counter.values()
print(data_test_bikeid_counter_keys)
print(data_test_bikeid_counter_values)


# In[ ]:


#计算繁忙的点
data_test_start_loc_counter_all=Counter(data_test['geohashed_start_loc'])
data_test_start_loc_counter=Counter(data_test['geohashed_start_loc']).most_common(100)
print(data_test_start_loc_counter)


# In[ ]:


#print(list(data_test_start_loc_counter))

#print(data_test_start_loc_counter_all.items())
data_test_start_loc_counter_all_dit = dict(data_test_start_loc_counter_all)
print(data_test_start_loc_counter_all_dit)



# In[ ]:


#data_test['ll_start_loc'] = pd.loc(data_test['geohashed_start_loc'])
data_test_hashed_start_loc = data_test['geohashed_start_loc']
print(data_test_hashed_start_loc)
data_test_ll_start_loc = gh.decode(data_test_hashed_start_loc)
print(data_test_ll_start_loc)


# In[ ]:


print(data_test_start_loc_counter_all.elem())


# In[ ]:


#统计不同类型数据,并排序
#第三个参数确定是否要排序,如果要排序，istime=1，如果不需要排序istime =0
def Counter_Data(data, typename,istime):
    data_counter=Counter(data[typename])
    #这是周，月，年数据需要排序，其他类型数据不需要排序
    #加一个参数，如果是日，周，月，年等时间数据进行排序，否则不排序
    if istime:
        data_counter_sorted=sorted(data_counter.items(),key=operator.itemgetter(0))
    else:
        data_counter_sorted = data_counter
        
    #这块在判断一下数据的长度
    
    return data_counter_sorted


# In[141]:


#数据进行排序
data_test_sort_orderid = data_test.sort_values(by = 'userid')
print(data_test_sort_orderid)


# In[140]:


#统计一些数据
data_test_group_biketype = data_test.groupby(['biketype']).count()
print(data_test_group_biketype)


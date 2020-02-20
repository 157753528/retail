import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data_1=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_2=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',encoding='utf8')

data_1_1=pd.DataFrame(data_1['kh'])
data_2_1=data_2[['kh','djh']]

data_VIP=pd.merge(data_1_1,data_2_1,on='kh',how='inner')     #得到会员的消费信息
list=[]                                                     #创建一个空列表
for i in data_VIP['djh']:
    list.append(i)
list2=[]
for i in data_2_1['djh']:
    list2.append(i)
VIP_djs=len(list)               #用len（）得出数据的数量，当时傻了，其实直接len(data_2_1['djh'])就OK了。
normal_djs=len(list2)-VIP_djs      #分别是VIP的单据数和普通的单据数
y=[VIP_djs,normal_djs]
x=['VIP','Normal']
plt.bar(x,y)

for x,y in zip(x,y):                         #for循环用于显示条形统计图的每个部分的最大值
    plt.text(x,y+1,'%.2f'%y,horizontalalignment='center')

plt.show()


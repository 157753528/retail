import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data_1=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_2=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',encoding='utf8')
data_1_1=data_1[['kh','xb']]
data_2_1=data_2[['kh','dtime','djh']]

VIP=pd.merge(data_1_1,data_2_1,how='inner',on='kh')
VIP['dtime']=pd.to_datetime(VIP['dtime'],errors='coerce',format='%Y/%m/%d %H:%M:%S.%f')
VIP_1=VIP.copy()
VIP_1['hour']=VIP_1['dtime'].dt.hour            #上同。求时间。
sj_lc=VIP_1[(0<=VIP_1.hour) & (VIP_1.hour<6)]
sj_zs=VIP_1[(6<=VIP_1.hour) & (VIP_1.hour<10)]
sj_zw=VIP_1[(10<=VIP_1.hour) & (VIP_1.hour<14)]
sj_xw=VIP_1[(14<=VIP_1.hour) & (VIP_1.hour<18)]
sj_ws=VIP_1[(18<=VIP_1.hour) & (VIP_1.hour<23)]
# print(sj_lc.head())
# print(sj_zs.head())
# print(sj_zw.head())
# print(sj_xw.head())
# print(sj_ws.head())
num_lc=len(sj_lc.groupby(['djh','kh']).sum())     #将一天划分为凌晨，早上，中午，下午，晚上。len（）函数求长度
num_zs=len(sj_zs.groupby(['djh','kh']).sum())

num_zw=len(sj_zw.groupby(['djh','kh']).sum())
num_ws=len(sj_ws.groupby(['djh','kh']).sum())
num_xw=len(sj_xw.groupby(['djh','kh']).sum())


print(num_lc,num_ws,num_xw,num_zs,num_zw)
x=['lc','zs','zw','xw','ws']
y=[num_lc,num_zs,num_zw,num_xw,num_ws]
plt.bar(x,y)
plt.xlabel('sjd')                #sjd为时间段。。
plt.ylabel('number')
for x,y in zip(x,y):                         #for循环用于显示条形统计图的每个部分的最大值
    plt.text(x,y+1,'%.2f'%y,horizontalalignment='center')
plt.show()

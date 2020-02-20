import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data_1=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_2=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',encoding='utf8')
data_1_1=data_1[['kh','xb']]
data_2_1=data_2[['kh','dtime','je']]

VIP=pd.merge(data_1_1,data_2_1,how='inner',on='kh')
VIP['dtime']=pd.to_datetime(VIP['dtime'],errors='coerce',format='%Y/%m/%d %H:%M:%S.%f')
VIP_1=VIP.copy()
VIP_1['year']=VIP_1['dtime'].dt.year    #新建列，值为VIP['dtime’]的年份，下同，为月份
VIP_1['month']=VIP_1['dtime'].dt.month
a=VIP_1.groupby(['year','month']).sum()           #按年，月进行分组求和
je=a['je']                                         #每年每月的营业额

#因为2015年只有9个月在营业。所以是je_2015=je[:9]，下同
je_2015=je[:9]
je_2016=je[9:20]
je_2017=je[20:32]
je_2018=je[32:33]
x1=[1,2,3,4,5,6,7,8,12]
x2=[1,3,4,5,6,7,8,9,10,11,12]
x3=[1,2,3,4,5,6,7,8,9,10,11,12]
x4=[1]
# print(je_2015,je_2016,je_2017,je_2018)
x=[i for i in range(13)]
plt.subplot(221)     #画几幅图。（xyz）,画x*y副图，第z张图
plt.xticks(x)
plt.title(2015)
plt.bar(np.array(x1),je_2015,label='2015')
# for a,b in zip(x1,je_2015):                         #for循环用于显示条形统计图的每个部分的最大值
#     plt.text(a,b+1,'%.2f'%b,horizontalalignment='center')

plt.subplot(222)
plt.xticks(np.array(x))
plt.title(2016)
plt.bar(np.array(x2),je_2016,label='2016')
# for a,b in zip(x2,je_2016):                         #for循环用于显示条形统计图的每个部分的最大值
#     plt.text(a,b+1,'%.2f'%b,horizontalalignment='center')

plt.subplot(223)
plt.xticks(x)
plt.title(2017)
plt.bar(np.array(x3),je_2017,label='2017')
# for a,b in zip(x3,je_2017):                         #for循环用于显示条形统计图的每个部分的最大值
#     plt.text(a,b+1,'%.2f'%b,horizontalalignment='center')

plt.subplot(224)
plt.xticks(x)
plt.title(2018)
plt.bar(np.array(x4),je_2018,label='2018')
# for a,b in zip(x4,je_2018):                         #for循环用于显示条形统计图的每个部分的最大值
#     plt.text(a,b+1,'%.2f'%b,horizontalalignment='center')


plt.xticks(x)

plt.show()
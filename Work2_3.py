import pandas as pd
from matplotlib import pyplot as plt

data_1=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_2=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',encoding='utf8')
data_1_1=data_1[['kh','xb']]
data_2_1=data_2[['kh','dtime','je']]

VIP=pd.merge(data_1_1,data_2_1,how='inner',on='kh')
VIP['dtime']=pd.to_datetime(VIP['dtime'],errors='coerce',format='%Y/%m/%d %H:%M:%S.%f')
#将object类型的时间转化为datatime类型，分别操作。errors=‘coerce’为强制转化，format为格式

VIP_1=VIP.copy()
#拷贝元数据，下面的操作无法在原数据上进行

VIP_1['dtime']=VIP['dtime'].dt.year    #将复杂的年月日重赋值，值为VIP['dtime‘]的年
a=VIP_1.groupby('dtime').sum()         #按年分组。
je=a['je']
year=[2015,2016,2017,2018]

plt.bar(year,je)
plt.xlabel('year')
plt.ylabel('money')
for x,y in zip(year,je):                         #for循环用于显示条形统计图的每个部分的最大值
    plt.text(x,y+1,'%.2f'%y,horizontalalignment='center')
plt.show()

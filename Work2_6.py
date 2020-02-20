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
VIP_1['year']=VIP_1['dtime'].dt.year
VIP_1['month']=VIP_1['dtime'].dt.month
x=['spring','summer','autumn','winter']
sj_2015=VIP_1[VIP_1.year==2015]
sj_2015_spring=sj_2015[(sj_2015.month>=3)&(sj_2015.month<=5)]
sj_2015_summer=sj_2015[(sj_2015.month>=6)&(sj_2015.month<=8)]
sj_2015_autumn=sj_2015[(sj_2015.month>=9)&(sj_2015.month<=11)]
sj_2015_winter=sj_2015[(sj_2015.month==12)|(sj_2015.month<=2)]
y1_2015=len(sj_2015_spring.groupby(['kh','djh']))
y2_2015=len(sj_2015_summer.groupby(['kh','djh']))
y3_2015=len(sj_2015_autumn.groupby(['kh','djh']))
y4_2015=len(sj_2015_winter.groupby(['kh','djh']))
y1=[y1_2015,y2_2015,y3_2015,y4_2015]
plt.subplot(221)
plt.title(2015)

plt.bar(x,y1)
for x,y in zip(x,y1):
    plt.text(x,y+1,'%.2f'%y,horizontalalignment='center')


sj_2016=VIP_1[VIP_1.year==2016]
sj_2016_spring=sj_2016[(sj_2016.month>=3)&(sj_2016.month<=5)]
sj_2016_summer=sj_2016[(sj_2016.month>=6)&(sj_2016.month<=8)]
sj_2016_autumn=sj_2016[(sj_2016.month>=9)&(sj_2016.month<=11)]
sj_2016_winter=sj_2016[(sj_2016.month==12)|(sj_2016.month<=2)]
y1_2016=len(sj_2016_spring.groupby(['kh','djh']))
y2_2016=len(sj_2016_summer.groupby(['kh','djh']))
y3_2016=len(sj_2016_autumn.groupby(['kh','djh']))
y4_2016=len(sj_2016_winter.groupby(['kh','djh']))
y2=[y1_2016,y2_2016,y3_2016,y4_2016]
plt.subplot(222)
plt.title(2016)
x1=['spring','summer','autumn','winter']
plt.bar(x1,y2)
for x,y in zip(x1,y2):
    plt.text(x,y+1,'%.2f'%y,horizontalalignment='center')


sj_2017=VIP_1[VIP_1.year==2017]
sj_2017_spring=sj_2017[(sj_2017.month>=3)&(sj_2017.month<=5)]
sj_2017_summer=sj_2017[(sj_2017.month>=6)&(sj_2017.month<=8)]
sj_2017_autumn=sj_2017[(sj_2017.month>=9)&(sj_2017.month<=11)]
sj_2017_winter=sj_2017[(sj_2017.month==12)|(sj_2017.month<=2)]
y1_2017=len(sj_2017_spring.groupby(['kh','djh']))
y2_2017=len(sj_2017_summer.groupby(['kh','djh']))
y3_2017=len(sj_2017_autumn.groupby(['kh','djh']))
y4_2017=len(sj_2017_winter.groupby(['kh','djh']))
y3=[y1_2017,y2_2017,y3_2017,y4_2017]
plt.subplot(223)
plt.title(2017)
x2=['spring','summer','autumn','winter']

plt.bar(x2,y3)

for x,y in zip(x2,y3):
    plt.text(x,y+1,'%.2f'%y,horizontalalignment='center')


sj_2018=VIP_1[VIP_1.year==2018]
sj_2018_winter=sj_2018[(sj_2018.month==12)|(sj_2018.month<=2)]
y1_2018=len(sj_2018_winter.groupby(['kh','djh']))
y4=[y1_2018,0,0,0]
plt.subplot(224)
plt.title(2018)
x3=['spring','summer','autumn','winter']

plt.bar(x3,y4)

for x,y in zip(x3,y4):
    plt.text(x,y+1,'%.2f'%y,horizontalalignment='center')
plt.show()


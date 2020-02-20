import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_1=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',encoding='utf8')

data_2=data.dropna(axis=0,subset=['csrq'])
csrq=data_2[['csrq','kh']]

jj=csrq.copy()
jj['csrq']=pd.to_datetime(csrq['csrq'],format='%Y/%m/%d %H:%M:%S.%f',errors='coerce')
jj['csrq']=jj['csrq'].dt.year
jj['old']=2020-jj['csrq']
# print(jj.head())

data_3=data_1.dropna(axis=0,subset=['kh'])
data_4=data_3[['kh','je']]
a=data_4.groupby('kh').sum()
b=pd.merge(a,jj,on='kh')
# print(b.info())
c=b[(15<b['old'])&(b['old']<90)]

d=c.groupby('old').sum()
# print(d)
je=[]
for i in d['je']:
    je.append(i)
old=[i for i in range(18,88)]
plt.bar(old,je)
plt.plot()
plt.xlabel('old')
plt.xticks(old)
plt.ylabel('je')
plt.show()


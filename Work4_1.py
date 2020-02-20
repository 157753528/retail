import pandas as pd
import numpy as np
import matplotlib.font_manager as fm
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
data_1=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_2=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',
                   encoding='utf8').dropna(axis=0,subset=['dtime'])

data_1_1=data_1[['kh','djsj']].dropna(axis=0,subset=['djsj'])
data_2_1=data_2[['kh','je','djh']]
data=pd.merge(data_1_1,data_2_1,on='kh')
data_cp=data.copy()
data_cp.loc[:,'djsj']=pd.to_datetime(data['djsj'],format='%Y/%m/%d %H:%M:%S.%f',errors='coerce')
data_cp['djsj']=data_cp['djsj'].dt.year
data_cp['入会时间']=2020-data_cp['djsj']
L=data_cp[['kh','入会时间']]
# print(data_cp.head())

F=data_cp[['kh','djh']].groupby('kh').count().reset_index()
F_1=F[['kh','djh']]                #获取消费次数

M=data_cp[['kh','je']].groupby('kh').sum().reset_index()
M_1=M[['kh','je']]                      #获取消费金额

data_a=pd.merge(L,F,on='kh',how='inner')
data_b=pd.merge(data_a,M,on='kh',how='inner')
data_b=data_b.rename(columns={'kh':'卡号','djh':'消费次数','je':'消费金额'})
# print(data_b.info())

data_future=data_b[['入会时间','消费次数','消费金额']]
data_b_SC=StandardScaler().fit_transform(data_future)
KMeans_model=KMeans(n_clusters=5)
fit_model=KMeans_model.fit(data_b_SC)        #训练聚类模型
# print(KMeans_model.cluster_centers_)
myfont=fm.FontProperties(fname='C:/WindowsFonts/AdobeSongStd-Light.otf')
angles=np.linspace(0,2*np.pi,3,endpoint=False)     #将园根据标签的个数等比分
angles=np.concatenate((angles,[angles[0]]))        #闭合
centers=KMeans_model.cluster_centers_             #获取聚类中心数据
plt_data=np.concatenate((centers,centers[:,[0]]),axis=1)
label=['L','F','M']
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111,polar=True)
for i in range(len(plt_data)):
    ax.plot(angles,plt_data[i],'o-',label=(i+1))
ax.set_thetagrids(angles*180/np.pi,label)
plt.legend(bbox_to_anchor=(0.8,1.15),ncol=3)

plt.show()
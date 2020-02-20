import pandas as pd
from matplotlib import pyplot as plt

data_1=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_2=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',encoding='utf8')

data_1_1=data_1[['kh','xb']]      #取data_1的‘kh’列和‘xb’列
data_2_1=data_2[['kh','je']]

data=pd.merge(data_1_1,data_2_1,on='kh')          #将两表按‘kh’相同的合并在一起。取交集
data_dropna=data.dropna(axis=0,subset=['xb'])        #将‘xb’为空的行删除

data_people=data_dropna.groupby(['xb','kh']).sum()        #求男。女人数
data_je=data_dropna.groupby('xb').sum()          #求男性和女性的消费金额


df=pd.DataFrame(data_people)           #将得到的DataframeGroupBy数据类型转化为Dataframe
finish=df.reset_index()               #重置索引
sex_0=finish[finish.xb==0]      #性别为男的数据
sex_1=finish[finish.xb==1]
x=[len(sex_0),len(sex_1)]          #len（）函数求出长度，即人数
plt.pie(x,labels=['man','wuman'],autopct='%1.2f%%')
plt.title('people')



# plt.pie(data_je['je'],labels=['man','wuman'],autopct='%1.2f%%')
# plt.title('je')

plt.show()

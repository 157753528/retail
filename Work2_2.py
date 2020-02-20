import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data_1=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_2=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',encoding='utf8')

data_1_1=pd.DataFrame(data_1['kh'])
data_2_1=data_2[['kh','je']]

VIP_list=pd.merge(data_1_1,data_2_1,how='inner',on='kh')
VIP=VIP_list['je'].sum()                  #会员消费金额
Normal=data_2_1['je'].sum()-VIP        #所有人的消费金额-会员消费金额=非会员消费金额
# print(int(VIP))
# print(int(Normal))

x=['VIP','Normal']
y=[VIP,Normal]
plt.bar(x,y)
for x,y in zip(x,y):                         #for循环用于显示条形统计图的每个部分的最大值
    plt.text(x,y+1,'%.2f'%y,horizontalalignment='center')
plt.show()
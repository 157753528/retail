import pandas as pd
from matplotlib import pyplot as plt
import wordcloud


data_1=pd.read_excel("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c1.xlsx")
data_2=pd.read_csv("C:/Users/Ntisok/Desktop/实训材料/data/cumcm2018c2.csv",engine='python',encoding='utf8').dropna(axis=0,subset=['dtime'])




data_1_1=data_1.dropna(axis=0,subset=['csrq','djsj','xb','djsj'])
data_2_1=data_2[['kh','dtime','je','gzmc','jf']]
data=pd.merge(data_1_1,data_2_1,on='kh',how='inner')
# print(data.info())

#卡号和性别
bq_1=data_1_1[['kh','xb']]
bq_1_cp=bq_1.copy()
data_cp=data.copy()

#年龄
data_cp.loc[:,'csrq']=pd.to_datetime(data['csrq'],format='%Y/%m/%d %H:%M:%S.%f',errors='coerce')
data_cp.loc[:,'csrq']=data_cp['csrq'].dt.year
bq_1_cp['old']=2020-data_cp['csrq']


#入会时间
data_cp.loc[:,'djsj']=pd.to_datetime(data['djsj'],format='%Y/%m/%d %H:%M:%S.%f',errors='coerce')
data_cp.loc[:,'djsj']=data_cp['djsj'].dt.year
bq_1_cp['rhsj']=2020-data_cp['djsj']


#消费水平
je_a=data_cp['je']
je_b=[]
for i in je_a:
    if 0<i<=100:
        je_b.append("低消费水平")
    elif 100<=i<300:
        je_b.append('中等消费水平')
    elif 300<=i:
        je_b.append("高消费水平")
    else:
        je_b.append('Nan')

je_c={'kh':data_cp['kh'],'xfsp':je_b}
je_d=pd.DataFrame(je_c)           #最后与bq_1_cp合并
data1=pd.merge(bq_1_cp,je_d,on='kh',how='outer')
del je_d,je_b,je_c,je_a
# print(data1.info())
# #消费季节
data_cp.loc[:,'dtime']=pd.to_datetime(data['dtime'],format='%Y/%m/%d %H:%M:%S.%f',errors='coerce')
data_cp['month']=data_cp['dtime'].dt.month
month_a=data_cp['month']
month_b=[]
for i in month_a:
    if 3<=i<=5:
        month_b.append('春季集中消费')
    elif 6<=i<=8:
        month_b.append('夏季集中消费')
    elif 9<=i<=11:
        month_b.append("秋季集中消费")
    elif i==12 | i<=2:
        month_b.append("冬季集中消费")
    else:
        month_b.append("Nan")

month_c={'kh':data_cp['kh'],'集中消费季节':month_b}
month_d=pd.DataFrame(month_c)
data2=pd.merge(data1,month_d,on='kh',how='outer')
del month_a,month_b,month_c,month_d,data1


#柜台
gzmc_a=data_cp['gzmc']
gzmc_1=['好孩子','小天才''jeep童装']
gzmc_2=['雅诗兰黛ESTEE LAUDER','兰芝柜','科颜氏柜','迪奥柜','佰草集','圣罗兰柜','雅芳婷柜','Marisfrolg','碧欧泉(BIOTHERM)','Dior','CHANEL','迪奥']
gzmc_3=[ 'ARMANI COLLEZIONI','阿玛尼GIORGIO ARMANI','施华洛世奇柜']
gzmc_4=['']
gzmc_b=[]
for i in gzmc_a:
    if i in gzmc_1:
        gzmc_b.append('有孩子')
    elif i in gzmc_2:
        gzmc_b.append('精致')
    elif i in gzmc_3:
        gzmc_b.append('奢侈品')
    else:
        gzmc_b.append("促销狂热者")
gzmc_c={'kh':data_cp['kh'],'标签':gzmc_b}
gzmc_d=pd.DataFrame(gzmc_c)
data3=pd.merge(data2,gzmc_d,on='kh',how='outer')
del data2

mid_je=data3.groupby('标签')['je'].sum()
dic={x[0]:x[1] for x in mid_je.loc[:,:].values}
wc=wordcloud.WordCloud(scale=16,background_color='white',max_words=100,colormap='coolwarm',
                    font_path='C:/WindowsFonts/AdobeSongStd-Light.otf')
X=wc.generate_from_frequencies(dic)
plt.axis('off')
plt.imshow(X)
plt.show()
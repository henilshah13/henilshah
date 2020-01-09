import pandas as pd
df=pd.read_csv('dbdump.csv')
print(df['ip'])
df2=df['id'].describe()
print(df2)
line='-'*40
print(line)

df3=df['ip'].describe()
print(df3)
print(line)

df4=df.describe()
print(df4)
print(line)

df5=df['id'].mean()
print(df5)
print(line)

df6=df.head(5)
df7=df.tail(5)
print(df6)
print(line)
print(df7)


df8=df['pics'].value_counts()
print(df8)
print(line)

import matplotlib.pyplot as plt
df8.plot()
#plt.show()

df8.plot.bar()
plt.savefig('mygraph.png',bbox_inches='tight')

writer=pd.ExcelWriter('Report.xlsx',engine='xlsxwriter')
df8.to_excel(writer,sheet_name='data')
wb=writer.book
ws=wb.add_worksheet('graph')
ws.insert_image('B2','mygraph.png')
writer.close()

#df9=df[df['id']>10]
#print(df9)

#df10=df[df['pics'].str.endswith('jpg')]
#print(df10)

#df11=df.groupby(['pics']).count()
#print(df11)


df12=df.iloc[1,1]
df13=df.iloc[1]
df14=df.iloc[:,1]
df15=df.iloc[1:10:2]
df16=df.iloc[:,0:5:2]
df17=df.iloc[5:10,1:4]
df18=df.iloc[[1,4,7]]
df19=df.iloc[[1,4,7],[1,3]]
print(df12)
print(df13)
print(df14)
print(df15)
print(df16)
print(df17)
print(df18)
print(df19)

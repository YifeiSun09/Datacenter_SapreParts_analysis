import pandas as pd 
import re

df = pd.read_csv("location of file , and file name", encoding='utf-8')
rows=df["Item Name"]#只选需要分离的一列

df_new = df['Item Name'].str.extract('(?P<length>(\d+(?:\.\d+)?))\s*(?P<unit>(KM|M|meter|FT))', flags=re.IGNORECASE)
#正则YYDS，并且重新明明新的列

df_new=df_new["length"]+df_new["unit"]
df_new
#新的dataframe（这么做是因为不知道为什么变成了4列，所以就只提取需要的两列）

df["length"]=df_new
df
#把分离出来的添加到以前的dataframe里

df.to_csv("C:/Users/yifeisun/Desktop/TYO22DPLY.csv", encoding='utf-8')
#导出
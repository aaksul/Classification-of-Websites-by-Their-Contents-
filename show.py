import pandas as pd
import numpy as np
modelname="all"
df=pd.DataFrame()
df=pd.read_csv('CsvForTrain/'+modelname+'.csv',encoding='utf-8')
df = df.sample(frac=1).reset_index(drop=True)#shuffle
print(df.head(10))

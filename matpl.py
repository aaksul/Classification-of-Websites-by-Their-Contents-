import pandas as pd
import numpy as np
import pickle
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
#import matplotlib.pyplot as plt

df=pd.DataFrame()
df=pd.read_csv('Dataset/CsvForTrain/AdultvsNews.csv',encoding='utf-8')
df = df.sample(frac=1).reset_index(drop=True)#shuffle
#print(df.head(10))

#X_train= df.loc[:1499,'content'].values
#Y_train=df.loc[:1499,'label'].values
#X_test= df.loc[1300:1800,'content'].values
#Y_test=df.loc[1300:1800,'label'].values
total_reviews=df.loc[:1840,'content']
tokenizer_obj=Tokenizer()
tokenizer_obj.fit_on_texts(total_reviews)
print(tokenizer_obj.word_index)
max_length=max([len(s.split()) for s in total_reviews])
with open('Model/tokenizerForAdultvsNews.pickle', 'wb') as handle:
    pickle.dump(tokenizer_obj, handle, protocol=pickle.HIGHEST_PROTOCOL)
#print(max_length)
vocab_size= len(tokenizer_obj.word_index) + 1
print(vocab_size)
reviews_tokens=tokenizer_obj.texts_to_sequences(total_reviews)
#X_test_tokens= tokenizer_obj.texts_to_sequences(X_test)
review_pad=pad_sequences(reviews_tokens,maxlen=max_length,padding='post')
#X_test_pad=pad_sequences(X_test_tokens,maxlen=max_length,padding='post')

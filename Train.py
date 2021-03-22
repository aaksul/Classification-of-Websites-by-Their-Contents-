import pandas as pd
import numpy as np
import pickle
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense,Embedding,LSTM,GRU
from keras.layers.embeddings import Embedding
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import classification_report,confusion_matrix


df_train=pd.DataFrame()
df_train=pd.read_csv('CsvForTrain/train2.csv',encoding='utf-8')
#df_train = df_train.sample(frac=2).reset_index(drop=True)#shuffle

df_valid=pd.DataFrame()
df_valid=pd.read_csv('CsvForTrain/valid2.csv',encoding='utf-8')
#df_valid = df_valid.sample(frac=2).reset_index(drop=True)#shuffle

df_all=pd.DataFrame()
df_all=pd.read_csv('CsvForTrain/all2.csv',encoding='utf-8')
#df_all =df_all.sample(frac=1).reset_index(drop=True)#shuffle


X_train= df_train.loc[:2451,'content'].values
Y_train=df_train.loc[:2451,'label'].values

X_valid= df_valid.loc[:571,'content'].values
Y_valid=df_valid.loc[:571,'label'].values

total_reviews=df_all.loc[:3021,'content']
tokenizer_obj=Tokenizer()
tokenizer_obj.fit_on_texts(total_reviews)
max_length=max([len(s.split()) for s in total_reviews])
with open('Tokenizers/tokenizerFormodel1.pickle', 'wb') as handle:
    pickle.dump(tokenizer_obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

vocab_size= len(tokenizer_obj.word_index) + 1
print(vocab_size)
Y_train=Y_train.reshape(-1,1)
Y_valid=Y_valid.reshape(-1,1)
onehot_encoder = OneHotEncoder(sparse=False)
Y_train = onehot_encoder.fit_transform(Y_train)
Y_valid  = onehot_encoder.fit_transform(Y_valid)
print(Y_valid)
X_train_tokens= tokenizer_obj.texts_to_sequences(X_train)
X_valid_tokens= tokenizer_obj.texts_to_sequences(X_valid)
X_train_pad=pad_sequences(X_train_tokens,maxlen=max_length,padding='post')
X_valid_pad=pad_sequences(X_valid_tokens,maxlen=max_length,padding='post')


print("Build Model...")
EMBEDDING_DIM=100
model=Sequential()
model.add(Embedding(vocab_size,EMBEDDING_DIM,input_length=max_length))
model.add(GRU(units=32,dropout=0.2,recurrent_dropout=0.2))
model.add(Dense(2,activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
#print(model.summary())
print("Train...")
history=model.fit(X_train_pad,Y_train,batch_size=128,epochs=38,validation_data=(X_valid_pad,Y_valid),verbose=2)
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('model1'+' accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'valid'], loc='upper left')
plt.show()

df_test=pd.DataFrame()
df_test=pd.read_csv('CsvForTrain/test2.csv',encoding='utf-8')

X_test= df_test.loc[:401,'content'].values
Y_test=df_test.loc[:401,'label'].values

test_sample_tokens=tokenizer_obj.texts_to_sequences(X_test)
test_sample_tokens_pad=pad_sequences(test_sample_tokens,maxlen=max_length)
y_pred=model.predict(x=test_sample_tokens_pad)
y_pred_bool = np.argmax(y_pred, axis=1)
print(y_pred_bool)
print(Y_test)
#target_names = ['class 0', 'class 1']
print(classification_report(Y_test, y_pred_bool))

category_list = ["Yetişkin", "Haber+Oyun+Eğitim"]
#labels=[0,1]
data=confusion_matrix(Y_test,y_pred_bool)


row_format ="{:>15}" * (len(category_list) + 1)
print(row_format.format("", *category_list))
for category, row in zip(category_list, data):
    print(row_format.format(category, *row))

model.save('Models/model1.h5')


#tokenizer_obj.fit_on_texts(total_reviews)

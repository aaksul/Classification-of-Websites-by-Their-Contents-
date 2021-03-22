from keras import models
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
import pickle
import collections
import Stemming

def SetToText(set):
    text=""
    print(set)
    for word in set:
        text+=str(word)+" "
    return text

def PredictContent(domain,language='english'):
    Category=["Adult","News","Games","Science"]
    Text=""
    domain=domain
    content=Stemming.GetContentSetOfDomain(domain)
    print(content)
    if(content!=None):
        Text=SetToText(content)
    else:
        print("gecerli domain giriniz")

    index=TestWithCat(Text,language='english')
    print(Category[index])
    return Category[index]

def TestWithCat(Text,language='english'):
    test_sample=[]
    test_sample.append(Text)
    TokenizerPath='Tokenizers/tokenizerForall.pickle'
    ModelPath='Models/all.h5'
    with open(TokenizerPath, 'rb') as handle:#Verilen Contentin tokenize yani vectore cevrilmesi icin gerekli dosya
        tokenizer_obj = pickle.load(handle)
    new_model=models.load_model(ModelPath)
    test_sample_tokens=tokenizer_obj.texts_to_sequences(test_sample)
    test_sample_tokens_pad=pad_sequences(test_sample_tokens,maxlen=10)
    predicts=list(new_model.predict(x=test_sample_tokens_pad)[0])
    print("Tahmin degerleri:")
    print(predicts)
    handle.close()
    CategoryIndex=predicts.index(max(predicts))
    return CategoryIndex
PredictContent("https://fanatik.com.tr")

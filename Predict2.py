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
    Text=""
    domain=domain
    content=Stemming.GetContentSetOfDomain(domain)
    print(content)
    if(content!=None):
        Text=SetToText(content)
    else:
        print("gecerli domain giriniz")

    value=TestWithCat(Text,language='english',cat1="Adult",cat2="News")

    if(value<0.5):
        category="Adult"
    else:
        category="News"

    value=TestWithCat(Text,language='english',cat1=category,cat2="Games")

    if(value<0.5):
        return category
    else:
        category="Games"
        return category

def TestWithCat(Text,language='english',cat1="",cat2=""):
    test_sample=[]
    test_sample.append(Text)
    Modelname=str(cat1)+"vs"+str(cat2)
    print(Modelname)
    TokenizerPath='Tokenizers/tokenizerFor'+Modelname+'.pickle'
    ModelPath='Models/'+Modelname+'.h5'
    with open(TokenizerPath, 'rb') as handle:#Verilen Contentin tokenize yani vectore cevrilmesi icin gerekli dosya
        tokenizer_obj = pickle.load(handle)
    new_model=models.load_model(ModelPath)
    test_sample_tokens=tokenizer_obj.texts_to_sequences(test_sample)
    test_sample_tokens_pad=pad_sequences(test_sample_tokens,maxlen=10)
    #print(Modelname)
    print(float(new_model.predict(x=test_sample_tokens_pad)[0]))
    value=float(new_model.predict(x=test_sample_tokens_pad)[0])
    handle.close()
    return value

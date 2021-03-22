#-*- coding: utf-8 -*-
import string
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import requests
import csv
from TurkishStemmer import TurkishStemmer
def RemovePunctuation(Str1):
    for punc in string.punctuation:
        Str1=Str1.replace(punc,"")

    return Str1

def StemingOfString(Str1):
    translationTable = str.maketrans("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
    stopword = stopwords.words('english')
    words=word_tokenize(Str1)
    Str2=""
    for word in words:
        word=word.translate(translationTable)
        word=word.lower()
        word=re.sub(r'[^a-zA-Z]','',word)
        try:
            if word not in  stopword:
                Str2+=word
                Str2+=" "
        except UnicodeWarning :
            print("!!!!! "+word)

    return Str2


def Stem(Str1):
    Str1=RemovePunctuation(Str1)
    Str1=StemingOfString(Str1)
    return Str1

def GetContentSetOfDomain(Domain):
    try:
        title=""
        keywords=""
        description=""
        Content=""
        Domain=Domain.lower()
        r=requests.get(Domain)
        soup=BeautifulSoup(r.content,features="lxml")
        try:
            title=soup.title.string
        except AttributeError:
            pass
        for i in soup.find_all(attrs={'name':'keywords'}):
            keywords=i['content']
        for i in soup.find_all(attrs={'name':'description'}):
            description=i['content']
        Content=(title+" "+keywords+" "+description)
        Content=Stem(Content)
        Words=word_tokenize(Content)
        Content2=set()
        for word in Words:
            Content2.add(word)
        return Content2

    except:
        pass

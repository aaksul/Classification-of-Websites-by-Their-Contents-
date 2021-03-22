import Steeming
from bs4 import BeautifulSoup
import requests
import re
for i in range(20):
    F=open("AlexaPages//Science//"+str(i)+".html")
    soup=BeautifulSoup(F.read(),features='lxml')
    for elem in soup.find_all("p",{"a":""}):
        p=re.search('(<a href=\".+\">)(.+)(<\/a>)',str(elem))
        try:
            print(p.group(2))
        except:
            pass


    F.close()

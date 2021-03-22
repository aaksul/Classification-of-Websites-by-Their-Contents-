import csv
import string
import Stemming
import re
#Get Content From Domain list(txt) and Write To Csv with (domain,content) format

FileRead=open("/home/alp/Araproje/Domain/TurkOyunlarDomain.txt","r")
csv_fileToWrite=open("/home/alp/Araproje/Dataset/TurkishCsvGameDataset.csv","w")

fieldnames = ['domain','content','category']
csv_writer=csv.DictWriter(csv_fileToWrite,fieldnames=fieldnames)
csv_writer.writeheader()
for domain in FileRead.readlines():
    domain=re.sub('\n','',domain)
    words=Stemming.GetContentSetOfTurkishDomain(domain)
    print(domain)
    print(words)
    Content=""
    if(words!=None):
        for word in words:
            Content+=word+" "
        print("Content: "+Content)
    rowdict={'domain':domain,'content':Content,'category':'Game'}
    csv_writer.writerow(rowdict)

csv_fileToWrite.close()
FileRead.close()

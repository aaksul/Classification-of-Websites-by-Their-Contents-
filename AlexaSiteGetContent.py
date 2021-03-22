import Steeming
import csv

f=open("Domain//ScienceSite.txt")
csvfile=open("ScienceSiteDataset.csv",'w',newline='')
line=f.readline()
fieldnames=['Domain','Content']
writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
writer.writeheader()
while line:
    Domain="http://www."+line.lower()[:-1]
    print(Domain)
    WordSet=Steeming.GetContentSetOfDomain(Domain)
    Content=""
    if(WordSet!=None):
        for word in WordSet:
            Content+=word+" "
        print("Content: "+Content)
        writer.writerow({'Domain':Domain,'Content':Content})
    line=f.readline()
csvfile.close()
f.close()

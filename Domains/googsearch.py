try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
import re
import string
# to search
file=open("/home/alp/Araproje/Domain/TurkOyunGoogleDom.txt","w")

query="haber"
for line in search(query, tld="co.in", num=1000000, stop=None, pause=2):
    print(line)
    domain=re.search('^(https|http)://(www\.)*(?P<domain>[^/]+)',str(line))
    #file.write(domain.group(1)+"://www."+domain.group("domain")+"\n")
    file.write(line+"\n")
file.close()

import urllib.request, urllib.parse,urllib.error
from bs4 import BeautifulSoup
import ssl


#Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#raw input from stdin
url=input('Enter -')
#open the url as file handle
html=urllib.request.urlopen(url, context=ctx).read()
#Parse the HTML using Beautifulsoap
soup=BeautifulSoup(html,'html.parser')

#Retreve all the span tags
tags=soup('span')
print(tags)
count=0
for tag in tags:
    count=count+int(tag.contents[0])
print(count)
    

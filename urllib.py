#using urllib than socket

import urllib
html='http://py4inf.com/code/romeo.txt'
fhand=urllib.urlopen(html)
print type(fhand)
for line in fhand:
    print line.strip()

count=dict()
for line in fhand:
    words=line.split()
    for word in words:
        count[word]=count.get(word,0)+1
print count
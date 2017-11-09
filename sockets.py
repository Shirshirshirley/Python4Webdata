import socket

#creat endpoint
#creat an IP-based socket 
#request a stream-oriented socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#Establish connection between endpoint and host using port 80
mysock.connect(('www.py4inf.com',80))
#Send request
mysock.send('GET http://www.py4inf.com/code/intro-short.txt HTTP/1.0\n\n')
#Loop to read
while True:
    #call the receive
    #read chunks of up to 512 bytes
    data=mysock.recv(512)
    if len(data)<1:
        break
    print data
mysock.close()

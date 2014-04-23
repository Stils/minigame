from database import db_session as d
import models 
import socket
import sys
from thread import *
 
HOST = ''  
PORT = 8889 
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
s.listen(10)
print 'Socket now listening'
 
def regster(username,password):
    u = models.User(username,password)
    d.add(u)
    d.commit()

def clientthread(conn):
    conn.send('Welcome to the server. Register by register|name|passowrd\n')
     
    while True:
         
        #Receiving from client
        data = conn.recv(1024)
        a = data.split("|")
        if a[0]=="register":
            register(a[1],a[2])
        reply = 'OK...' + data
        if not data:
            break
     
        conn.sendall(reply)
     
    conn.close()
 
while 1:
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    
    start_new_thread(clientthread ,(conn,))
 
s.close()


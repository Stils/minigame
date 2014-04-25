from database import db_session as d
from models import *
import socket
import sys
from thread import *
import time
 
HOST = ''  
PORT = 8886
connections = []
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
 
def register(username,password):
    print "dupka"
    u = User(username,password)
    d.add(u)
    d.commit()

def login(username,password):
    u = User.query.filter(User.name==username ,User.password==password).first()
    if u != None:
        print "Succes login "+username+"!"
        return u
    else:
        return False

def move(direction,user):

    if user == False:
        return False

    if direction == "n":
        user.y -= 1
    elif direction == "s":
        user.y += 1
    elif direction == "w":
        user.x -= 1
    elif direction == "e":
        user.x += 1
    
    print user.x,user.y
    d.commit()

def parsemap():
    users = []
    for i in User.query.all():
        user = "-".join([i.name,str(i.x),str(i.y)])
        users.append(user)
    users = "|".join(users)
    # print users
    return users

def sendmap(x):
    while 1:
        for i in connections:
            i.sendall(parsemap())
        time.sleep(0.1)

def clientthread(conn):
    conn.send('Welcome to the server. Register by register|name|password\n')
    user = False
    while True:
         
        #Receiving from client
        data = ""

        try:
            data = conn.recv(1024).strip()
        except socket.error:
            pass

        print data
        a = data.split("|")
        try:
            if a[0]=="register":
                register(a[1],a[2])
            if a[0]=="login":
                user = login(a[1],a[2])
            if a[0]=="move":
                move(a[1],user)

        except:
            pass

        if not data:
            break
     
    conn.close()
    
start_new_thread(sendmap,(None,))
while 1:
    conn, addr = s.accept()
    connections.append(conn)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    
    start_new_thread(clientthread ,(conn,))
 
s.close()


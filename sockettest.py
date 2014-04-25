import socket
import sys
import curses
from thread import *
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",8886))
s.send("login|mat|abc")
win = curses.initscr()
curses.noecho()

def drawmap(connection):
	while 1:
		users = []
		data = connection.recv(1024)
		win.addstr(1,1,data)
		win.refresh()

		user = data.split("|")
		for i in user:
			users.append(i.split("-"))

		win.clear()
		win.border('|', '|', '-', '-', '+', '+', '+', '+')

		print users
		for i in users:
			win.addstr(int(i[2]),int(i[1]),i[0])
		win.refresh()

start_new_thread(drawmap,(s,))

while True:
	data = s.recv(1024)
	inputt = win.getch()
	win.refresh()
	if inputt==ord("d"):
		s.sendall("move|e")

	elif inputt==ord("a"):
		s.sendall("move|w")

	elif inputt==ord("w"):
		s.sendall("move|n")

	elif inputt==ord("s"):
		s.sendall("move|s")

	elif inputt==27:
		break


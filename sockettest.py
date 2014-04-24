import socket
import sys
import curses

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",8889))
s.send("login|mat|abc")
win = curses.initscr()

while True:
	print s.recv(1024)
		inputt = win.getch()
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

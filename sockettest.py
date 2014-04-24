import socket
import sys
import curses

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",8888))

win = curses.initscr()

while True:
		inputt = win.getch()
		if inputt==ord("d"):
			s.sendall("d")

		elif inputt==ord("a"):
			s.sendall("a")

		elif inputt==ord("w"):
			s.sendall("w")

		elif inputt==ord("s"):
			s.sendall("s")

		elif inputt==27:
			break

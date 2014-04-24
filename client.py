#!/usr/bin/env python
import curses

def login(stdscr):
# Clear screen
	stdscr.clear()
 
	begin_x = 0; begin_y = 0
	height = 7; width = 30
	win = curses.newwin(height, width, begin_y, begin_x)
	win.border('|', '|', '-', '-', '+', '+', '+', '+')
	win.addstr(1,1,'Hello! Please log in!',curses.A_BOLD)
	win.addstr(2,1,"----------------------------")
	win.addstr(3,1,"User: ")
	win.addstr(4,1,"----------------------------")
	win.addstr(5,1,"Pass: ")
	win.addstr(6,1,"----------------------------")

	curses.echo()
	log = win.getstr(3,7,20)
	win.addstr(3,1,"User: "+log)
	password = win.getstr(5,7,20)
	win.addstr(5,1,"Pass: "+password)
	curses.noecho()

	stdscr.refresh()

	if log != "":
		stdscr.clear()
		begin_x = 0; begin_y = 0
		height = 3; width = 25
		win = curses.newwin(height, width, begin_y, begin_x)
		win.border('|', '|', '-', '-', '+', '+', '+', '+')
		win.addstr(1,1,'Welcome %s!'% log.upper(),curses.A_BOLD)

		stdscr.refresh()
		win.refresh()


	stdscr.getch()
	stdscr.clear()
 	
	begin_x = 0; begin_y = 0
	height = 20; width = 40
	win = curses.newwin(height, width, begin_y, begin_x)
	win.border('|', '|', '-', '-', '+', '+', '+', '+')
	win.addstr(10,20,log)

	x=10
	y=20

	while True:
		inputt = win.getch() # zrobic tak zeby kasowalo caly login!
		if inputt==100:
			win.addstr(x,y," ")
			win.addstr(x,y+1,log)
			y+=1
			win.refresh()

		elif inputt==97:
			win.addstr(x,y," ")
			win.addstr(x,y-1,log)
			y-=1
			win.refresh()

		elif inputt==119:
			win.addstr(x,y," ")
			win.addstr(x-1,y,log)
			x-=1
			win.refresh()

		elif inputt==115:
			win.addstr(x,y," ")
			win.addstr(x+1,y,log)
			x+=1
			win.refresh()
		elif inputt==27:
			break
	 
	# This raises ZeroDivisionError when i == 10.
	# for i in range(0, 11):
	# v = i-10
	# stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
	 
	
	stdscr.getch()
	
curses.wrapper(login)

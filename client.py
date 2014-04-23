#!/usr/bin/env python
import curses
import curses.textpad

def main(stdscr):
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

	login = win.getstr(3,7,20)
	win.addstr(3,1,"User: "+login)
	password = win.getstr(5,7,20)
	win.addstr(5,1,"Pass: "+password)

	stdscr.refresh()

	if login != "":
		stdscr.clear()
		begin_x = 0; begin_y = 0
		height = 4; width = 25
		win = curses.newwin(height, width, begin_y, begin_x)
		win.border('|', '|', '-', '-', '+', '+', '+', '+')
		win.addstr(1,1,'Welcome %s!'% login,curses.A_BOLD)
		win.addstr(2,1,'8===D (.)(.)')

	stdscr.refresh()
	win.refresh()
	 
	 
	 
	# This raises ZeroDivisionError when i == 10.
	# for i in range(0, 11):
	# v = i-10
	# stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))
	 
	 
	stdscr.getch()
 
curses.wrapper(main)

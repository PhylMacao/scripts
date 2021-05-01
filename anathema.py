#!/usr/bin/env python3

# This is my first curses script ever

import sys,os,time
import curses

def typewriter(stdscr, message, delay=0.1):
    for c in message:
        stdscr.addch(c)
        time.sleep(delay)
        stdscr.refresh()

def draw_menu(stdscr):
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Show Hello World screen
    message = "Hello, World!\nPress a key..."
    typewriter(stdscr, message)
    k = stdscr.getch()

    stdscr.clear()
    stdscr.refresh()

    x = 0
    y = 0

    while (k != ord('q')):
        stdscr.clear()
        h, w = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            y = y + 1
        elif k == curses.KEY_UP:
            y = y - 1
        elif k == curses.KEY_RIGHT:
            x = x + 1
        elif k == curses.KEY_LEFT:
            x = x - 1

        x = max(0, x)
        x = min(w-1, x)

        y = max(0, y)
        y = min(h-1, y)

        # declarations
        wh = "Width: {}, Heigth: {}".format(w, h)
        statusbarstr = "Press 'q' to exit | STATUS BAR | Pos: {}, {}".format(x, y)

        # calculations

        # render text
        stdscr.addstr(0, 0, wh)

        stdscr.attron(curses.color_pair(3))
        stdscr.addstr(h-1, 0, statusbarstr)
        stdscr.addstr(h-1, len(statusbarstr), " " * (w - len(statusbarstr) - 1))
        stdscr.attroff(curses.color_pair(3))

        stdscr.move(y, x)

        #wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
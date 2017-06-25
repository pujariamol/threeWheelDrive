import curses

stdscr = curses.initscr();
curses.noecho();
curses.cbreak();
stdscr.keypad(1);

def initScreen():
  stdscr.addstr(0,7,"UP",curses.A_BOLD);
  stdscr.addstr(1,7,"DOWN",curses.A_BOLD);
  stdscr.addstr(1,0,"LEFT",curses.A_BOLD);
  stdscr.addstr(1,14,"RIGHT",curses.A_BOLD);

def quit():
  stdscr.addstr("Exiting...")
  curses.nocbreak();
  stdscr.keypad(0);
  curses.echo();
  curses.endwin();
  exit()

def up():
  print "UP key pressed"

def down():
  print "DOWN key pressed"

def left():
  print "LEFT key pressed"

def right():
  print "RIGHT key pressed"

def listenToKeyStrokes(args):
  initScreen();
  try:
    while 1:
      c = stdscr.getch()
      if c == curses.KEY_UP:
        stdscr.addstr(0,7,"UP",curses.A_BOLD);
        up()
      if c == curses.KEY_DOWN:
        stdscr.addstr(1,7,"DOWN",curses.A_BOLD);
        down()
      if c == curses.KEY_LEFT:
        stdscr.addstr(1,0,"LEFT",curses.A_BOLD);
        left()
      if c == curses.KEY_RIGHT:
        stdscr.addstr(1,14,"RIGHT",curses.A_BOLD);
        right()
      if c == ord('q'):
        quit()
  except KeyboardInterrupt:
    print "Keyboard interrupt"


try:
  curses.wrapper(listenToKeyStrokes) 
except KeyboardInterrupt: 
  print "Got Keyboard Interrupt exception. Exiting..." 
  exit() 

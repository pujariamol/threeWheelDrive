import curses

stdscr = curses.initscr();
curses.noecho();
curses.cbreak();
stdscr.keypad(1);

class UserInterface(object):

  def cursesWrapper(self,methodName):
    try:
      curses.wrapper(methodName)
    except KeyboardInterrupt:
      print "Got Keyboard Interrupt exception. Exiting..."
      exit()


  def initScreen(self):
    stdscr.addstr(0,7,"UP",curses.A_BOLD);
    stdscr.addstr(1,7,"DOWN",curses.A_BOLD);
    stdscr.addstr(1,0,"LEFT",curses.A_BOLD);
    stdscr.addstr(1,14,"RIGHT",curses.A_BOLD);

  def quit(self):
    stdscr.addstr("Exiting...")
    curses.nocbreak();
    stdscr.keypad(0);
    curses.echo();
    curses.endwin();

  def listenToKeyStrokes(self, up,down,left,right):
    self.initScreen();
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
          self.quit()
          break;
    except KeyboardInterrupt:
      print "Keyboard interrupt"


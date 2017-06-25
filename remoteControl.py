import threeWheelDriveV2 as DRIVER
import ui as UI

def UI.up():
  print "This is remote control printing the msg"

def main():
  UI.listenToKeyStrokes()

if __name__ == '__main__':
   main()

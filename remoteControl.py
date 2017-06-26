from ThreeWheelDrive import ThreeWheelDrive
from UserInterface import UserInterface

class RemoteControl(UserInterface):
  twd=ThreeWheelDrive()

  def upFunc(self):
    self.twd.forward()

  def downFunc(self):
    self.twd.backward()

  def leftFunc(self):
    self.twd.turnLeft()

  def rightFunc(self):
    self.twd.turnRight()

  def main(self,args):
    self.listenToKeyStrokes(self.upFunc, self.downFunc, self.leftFunc, self.rightFunc)
    self.twd.cleanup()

if __name__ == "__main__":
  rc=RemoteControl()
  rc.twd.init()
  rc.main('')
  rc.cursesWrapper(rc.main)
  

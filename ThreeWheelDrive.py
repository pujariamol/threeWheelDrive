import RPi.GPIO as GPIO 
from time import sleep

class ThreeWheelDrive(object):
  
  motorResponseTime=0.04

  def cleanup(self):
    GPIO.cleanup()

  def init(self):
    GPIO.setmode(GPIO.BOARD)

    global Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E
    Motor1A = 16
    Motor1B = 18
    Motor1E = 22
 
    Motor2A = 19
    Motor2B = 21
    Motor2E = 23
    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)
    GPIO.setup(Motor1E,GPIO.OUT)
	
    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)
    GPIO.setup(Motor2E,GPIO.OUT)
 
  def forward(self):
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)

    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)

    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor2A,GPIO.HIGH)
    sleep(self.motorResponseTime)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW) 

  def backward(self):
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)

    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.HIGH)

    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.LOW)
    sleep(self.motorResponseTime)
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)

  def turnLeft(self):
    GPIO.output(Motor1E,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1A,GPIO.HIGH)
    sleep(self.motorResponseTime)
    GPIO.output(Motor1E,GPIO.LOW)

  def turnRight(self):
    GPIO.output(Motor2E,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2A,GPIO.HIGH)
    sleep(self.motorResponseTime)
    GPIO.output(Motor2E,GPIO.LOW)

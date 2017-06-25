
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)



def init():
  #Initializing Motors
  global Motor1A, Motor1B, Motor1E, Motor2A, Motor2B, Motor2E
  Motor1A = 16
  Motor1B = 18
  Motor1E = 22

  Motor2A = 23
  Motor2B = 21
  Motor2E = 19
  GPIO.setup(Motor1A,GPIO.OUT)
  GPIO.setup(Motor1B,GPIO.OUT)
  GPIO.setup(Motor1E,GPIO.OUT)

  GPIO.setup(Motor2A,GPIO.OUT)
  GPIO.setup(Motor2B,GPIO.OUT)
  GPIO.setup(Motor2E,GPIO.OUT)

init()
GPIO.cleanup()


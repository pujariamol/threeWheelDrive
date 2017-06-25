import RPi.GPIO as GPIO 
import threading
from threading import Thread
from time import sleep

GPIO.setmode(GPIO.BOARD)

def cleanup():
  GPIO.cleanup()

def init():
  #Initializing Motors
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
 
def forward():
  GPIO.output(Motor1E,GPIO.HIGH)
  GPIO.output(Motor2E,GPIO.HIGH)

  GPIO.output(Motor1B,GPIO.LOW)
  GPIO.output(Motor2B,GPIO.LOW)

  GPIO.output(Motor1A,GPIO.HIGH)
  GPIO.output(Motor2A,GPIO.HIGH)
  sleep(0.5)
  GPIO.output(Motor1E,GPIO.LOW)
  GPIO.output(Motor2E,GPIO.LOW) 

def backward():
  GPIO.output(Motor1E,GPIO.HIGH)
  GPIO.output(Motor2E,GPIO.HIGH)

  GPIO.output(Motor1B,GPIO.HIGH)
  GPIO.output(Motor2B,GPIO.HIGH)

  GPIO.output(Motor1A,GPIO.LOW)
  GPIO.output(Motor2A,GPIO.LOW)
  sleep(0.5)
  GPIO.output(Motor1E,GPIO.LOW)
  GPIO.output(Motor2E,GPIO.LOW)

def turnLeft():
  GPIO.output(Motor1E,GPIO.HIGH)
  GPIO.output(Motor1B,GPIO.LOW)
  GPIO.output(Motor1A,GPIO.HIGH)
  sleep(0.5)
  GPIO.output(Motor1E,GPIO.LOW)

def turnRight():
  GPIO.output(Motor2E,GPIO.HIGH)
  GPIO.output(Motor2B,GPIO.LOW)
  GPIO.output(Motor2A,GPIO.HIGH)
  sleep(0.5)
  GPIO.output(Motor2E,GPIO.LOW)

def main():
  init()
  forward()
  turnLeft()
  turnRight()
  backward()

  cleanup()
	 
if __name__ == '__main__':
   main()

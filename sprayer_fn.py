import RPi.GPIO as GPIO
from time import sleep

def sprayer_run():
    GPIO.setmode(GPIO.BOARD)
 
    Motor3A = 36
    Motor3B = 38
    Motor3E = 40

    GPIO.setup(Motor3A,GPIO.OUT)
    GPIO.setup(Motor3B,GPIO.OUT)
    GPIO.setup(Motor3E,GPIO.OUT)
 
    print "SPRAYING THE HERBICIDE ON WEEDS"
    GPIO.output(Motor3A,GPIO.HIGH)
    GPIO.output(Motor3B,GPIO.LOW)
    GPIO.output(Motor3E,GPIO.HIGH)
    sleep(4)
 
    print "STOP SPRAYING"
    GPIO.output(Motor3E,GPIO.LOW)

    GPIO.cleanup()
    return




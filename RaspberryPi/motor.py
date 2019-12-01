#source code: https://gist.github.com/keithweaver/61fd7cec7b161a4f500ac05d257c7b72
import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BOARD)
 
MotorTopL = 16
MotorTopR = 17
MotorMidL = 18
MotorMidR = 19
MotorBotL = 20
MotorBotR = 21
 
GPIO.setup(MotorTopL,GPIO.OUT)
GPIO.setup(MotorTopR,GPIO.OUT)
GPIO.setup(MotorMidL,GPIO.OUT)
GPIO.setup(MotorMidR,GPIO.OUT)
GPIO.setup(MotorBotL,GPIO.OUT)
GPIO.setup(MotorBotR,GPIO.OUT)

i = 0
refresh = False
arr = [[0,1],[1,1],[0,0]]

while (i < 1000):
    if refresh == False: 
        reset()
    else:
        emboss(arr)
        sleep(5)
    
    i += 1
    


#raise dots according to input arr
def emboss(arr):
    if arr[0][0] == 1:
        GPIO.output(MotorTopL,GPIO.HIGH)
    elif arr[0][1] == 1:
        GPIO.output(MotorTopR,GPIO.HIGH)
    elif arr[1][0] == 1:
        GPIO.output(MotorMidL,GPIO.HIGH)
    elif arr[1][1] == 1:
        GPIO.output(MotorMidR,GPIO.HIGH)
    elif arr[2][1] == 1:
        GPIO.output(MotorBotL,GPIO.HIGH)
    elif arr[2][2] == 1:
        GPIO.output(MotorBotR,GPIO.HIGH)

sleep(5)

#reset all dots
def reset():
    GPIO.output(MotorTopL,GPIO.LOW)
    GPIO.output(MotorTopR,GPIO.LOW)
    GPIO.output(MotorMidL,GPIO.LOW)
    GPIO.output(MotorMidR,GPIO.LOW)
    GPIO.output(MotorBotL,GPIO.LOW)
    GPIO.output(MotorBotR,GPIO.LOW)
 
GPIO.cleanup()
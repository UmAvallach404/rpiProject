GPIO.output(enb,GPIO.HIGH) 

def sag():
    print("Motorlar sola gidiyor")
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(ena,GPIO.HIGH)

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ena = 11
in2 = 31
in1 = 29
in3 = 7
in4 = 37
enb = 24

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.output(in4, GPIO.LOW)
def dur():
    print("Motorlar durdu.")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)
    GPIO.output(ena,GPIO.LOW)
    GPIO.output(enb,GPIO.LOW)

try:
    while True:
        ileri()
        time.sleep(5)
        dur()
        time.sleep(7)

        sol()
        time.sleep(5)
        dur()
        time.sleep(7)

        sag()
        time.sleep(5)
        dur()
        time.sleep(7)


except:
    GPIO.cleanup()
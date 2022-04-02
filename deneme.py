import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ena = 11
input1 = 15
input2 = 13
input3 = 16
input4 = 18
enb =22

# Input Setup for Motor1
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)

# Input Setup for Motor2
GPIO.setup(input3, GPIO.OUT)
GPIO.setup(input4, GPIO.OUT)

# Motor Activation
GPIO.setup(ena, GPIO.OUT)
GPIO.setup(enb, GPIO.OUT)

command = input()

def forward():
    print("Motors running for forward movement.")
    GPIO.output(input1, GPIO.HIGH)
    GPIO.output(input2, GPIO.LOW)
    GPIO.setup(ena, GPIO.HIGH)

    GPIO.output(input3, GPIO.HIGH)
    GPIO.output(input4, GPIO.LOW)
    GPIO.setup(enb, GPIO.HIGH)

def backward():
    print("Motors running for backward movement.")
    GPIO.output(input2, GPIO.HIGH)
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(ena, GPIO.HIGH)

    GPIO.output(input4, GPIO.HIGH)
    GPIO.output(input3, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)

def right():
    print("Motors running for right movement.")
    GPIO.output(input1, GPIO.HIGH)
    GPIO.output(input2, GPIO.LOW)
    GPIO.output(ena, GPIO.HIGH)

    GPIO.output(input4, GPIO.HIGH)
    GPIO.output(input3, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)

def left():
    print("Motors running for left movement.")
    GPIO.output(input2, GPIO.HIGH)
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(ena, GPIO.HIGH)

    GPIO.output(input3, GPIO.HIGH)
    GPIO.output(input4, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)

def stop():
    print("Motors stopped.")
    GPIO.output(ena, GPIO.LOW)
    GPIO.output(enb, GPIO.LOW)




if command == 'r':
    forward()
    time.sleep(3)
    stop()
    time.sleep(5)
    backward()
    time.sleep(3)
    stop()
    time.sleep(5)
    right()
    time.sleep(3)
    stop()
    time.sleep(5)
    left()
    time.sleep(3)
    stop()
    time.sleep(5)

if command == 's':
    GPIO.cleanup()



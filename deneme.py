import RPi.GPIO as GPIO
import time

enable = 11
input1 = 15
input2 = 13
input3 = 16
input4 = 18
disable =22

# Input Setup for Motor1
GPIO.setup(input1, GPIO.OUT)
GPIO.setup(input2, GPIO.OUT)

# Input Setup for Motor2
GPIO.setup(input3, GPIO.OUT)
GPIO.setup(input4, GPIO.OUT)

# Motor Activation
GPIO.setup(enable, GPIO.OUT)
GPIO.setup(disable, GPIO.OUT)


def forward():
    print("Motors running for forward movement.")
    GPIO.output(input1, GPIO.HIGH)
    GPIO.output(input2, GPIO.LOW)
    GPIO.setup(enable, GPIO.HIGH)

    GPIO.output(input3, GPIO.HIGH)
    GPIO.output(input4, GPIO.LOW)
    GPIO.setup(disable, GPIO.HIGH)

def backward():
    print("Motors running for backward movement.")
    GPIO.output(input2, GPIO.HIGH)
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(enable, GPIO.HIGH)

    GPIO.output(input4, GPIO.HIGH)
    GPIO.output(input3, GPIO.LOW)
    GPIO.output(disable, GPIO.HIGH)

def right():
    print("Motors running for right movement.")
    GPIO.output(input1, GPIO.HIGH)
    GPIO.output(input2, GPIO.LOW)
    GPIO.output(enable, GPIO.HIGH)

    GPIO.output(input4, GPIO.HIGH)
    GPIO.output(input3, GPIO.LOW)
    GPIO.output(disable, GPIO.HIGH)

def left():
    print("Motors running for left movement.")
    GPIO.output(input2, GPIO.HIGH)
    GPIO.output(input1, GPIO.LOW)
    GPIO.output(enable, GPIO.HIGH)

    GPIO.output(input3, GPIO.HIGH)
    GPIO.output(input4, GPIO.LOW)
    GPIO.output(disable, GPIO.HIGH)

def stop():
    print("Motors stopped.")
    GPIO.output(enable, GPIO.LOW)
    GPIO.output(disable, GPIO.LOW)


try:
    while True:
        forward()
        time.sleep(3)
        stop()
        time.sleep(2)

        backward()
        time.sleep(3)
        stop()
        time.sleep(2)

        right()
        time.sleep(3)
        stop()
        time.sleep(2)

        left()
        time.sleep(3)
        stop()
        time.sleep(2)

except:
    GPIO.cleanup()

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


def ileri():
    print("Motorlar ileri gidiyor")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(ena, GPIO.HIGH)

    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)


def geri():
    print("Motorlar geri gidiyor")
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(ena, GPIO.HIGH)

    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)


def sol():
    print("Motorlar saga gidiyor")
    GPIO.output(in2, GPIO.HIGH)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(ena, GPIO.HIGH)

    GPIO.output(in3, GPIO.HIGH)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)


def sag():
    print("Motorlar sola gidiyor")
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(ena, GPIO.HIGH)

    GPIO.output(in4, GPIO.HIGH)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(enb, GPIO.HIGH)


def dur():
    print("Motorlar durdu.")
    GPIO.output(ena, GPIO.LOW)
    GPIO.output(enb, GPIO.LOW)


while(1):
    x = input()

    if x == 'i':
        ileri()
    elif x == 'g':
        geri()
    elif x == 'r':
        sag()
    elif x == 'l':
        sol()
    elif x == 'k':
        dur()
        GPIO.cleanup()
        break
    else:
        print("Yanlış girdin dalyarak")





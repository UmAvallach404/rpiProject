import serial, time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()


while True:
    ser.write(b"forward\n")
    time.sleep(10)
    print("forward")
    ser.write(b"backward\n")
    time.sleep(10)
    print("bakcward")
    ser.write(b"right\n")
    time.sleep(10)
    print("right")
    ser.write(b"left\n")
    time.sleep(10)
    print("left")
    ser.write(b"stop\n")
    time.sleep(10)
    print("stop")

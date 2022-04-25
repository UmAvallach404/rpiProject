import serial, time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()

while True:
    command = input()
    info = ser.readline().decode('utf-8').rstrip()
    print(info)
    x = int(command)
    if x == 5:
        print(info)
        ser.write(b"forward\n")

    elif x == 2:
        print(info)
        ser.write(b"backward\n")

    elif x == 3:
        print(info)
        ser.write(b"right\n")

    elif x == 1:
        print(info)
        ser.write(b"left\n")


    elif x == 0:
        print(info)
        ser.write(b"stop\n")

    elif x ==4:
        ser.write(b"deactivate\n")
    elif x ==6:
        ser.write(b"activate\n")



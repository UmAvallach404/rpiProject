import serial, time

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.flush()

command = input()

while True:
    if command==5:
        ser.write()
    elif command==2:
        ser.write(b"backward\n")
    elif command==3:
        ser.write(b"right\n")
    elif command==1:
        ser.write(b"left\n")
    elif command==0:
        ser.write(b"stop\n")

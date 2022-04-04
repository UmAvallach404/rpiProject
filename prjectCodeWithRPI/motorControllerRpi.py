import serial

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()

inputCommand = ser.readline();
print("Read input " + inputCommand.decode("utf-8").strip() + "from Arduino")

x = input()
while True:
    print("Choosen direction is "+ x + "to Arduino for Motors")
    ser.write(x.encode('utf-8'))


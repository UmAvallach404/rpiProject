import serial

x= input()
if __name__ == '_main_':
 ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
 ser.flush()
 while True:
  line = ser.readline().decode('utf-8').rstrip()
  print(line)
  if (x == "forward"):
   ser.write(b"forward/n")
  elif(x=="right"):
   ser.write(b"right/n")
  elif (x == "stop"):
   ser.write(b"stop/n")
  elif (x == "left"):
   ser.write(b"left/n")
  elif (x == "stop"):
   ser.write(b"stop/n")
  else:
   ser.write(b"stop/n")

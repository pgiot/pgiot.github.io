import serial
import requests

# ser = serial.Serial('/dev/ttyUSB0')  # open serial port
# line = ser.readline()

line = "hello \n"

line  = ''.join(line.splitlines())
payload = '{"name": "aa", "text": "bbb"}'
print(line)
r = requests.post("https://kakong.firebaseio.com/index.json", data=payload)
print(r.text)


    # print(ser.name)         # check which port was really used
    # ser.write(b'hello')     # write a string
    # ser.close()‰‰
import serial
import requests

payload = '{"name": "aa", "text": "bbb"}'
while True :
    # ser = serial.Serial('/dev/ttyUSB0')  # open serial port
    ser = serial.Serial('/dev/tty.usbmodem1411')  # open serial port
    line = ser.readline()
    # line  = ''.join(line.splitlines())
    # print(line)

    # line = "hello\n"

    if line == b'click\r\n':
        # print(line)
        r = requests.post("https://kakong.firebaseio.com/index.json", data=payload)
        # print(r.text)

# print(ser.name)         # check which port was really used
# ser.write(b'hello')     # write a string
# ser.close()‰‰
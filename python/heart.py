import serial
import requests

payload = '{"name": "aa", "text": "bbb"}'
while True :
    ser = serial.Serial('/dev/tty.usbmodem1411')  # open serial port
    line = ser.readline()
    if line == b'click\r\n':
        # print(line)
        r = requests.post("https://kakong.firebaseio.com/index.json", data=payload)
        # print(r.text)

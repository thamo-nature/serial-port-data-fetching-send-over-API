#!/usr/bin/python3

import serial
import os
#import mysql.connector
import requests
import time

token = "token123"

#multi port code 
#uncomment the following to enable multi serial port
"""
com_port = ['/dev/ttyUSB0','/dev/ttyUSB1']


for i in com_port:
    
    if(i == ''):
        device_id = "serial_1"
        print(device_id)
    else:
        device_id = "serial_2"
        print(device_id)


    BAUDRATE = 57600
    PORT = i
    TIMEOUT=1

    ser = serial.Serial(port=PORT,baudrate=BAUDRATE,timeout=TIMEOUT)
    
    temp_query= '?:2010:00::c3\r'
    co2_query= '?:2020:00::c0\r'


    ser.write(temp_query.encode())
    resp_temp=ser.readline()
    act_temp=resp_temp[18:25].decode()
    act_temp=float(act_temp)
    print(act_temp)


    ser.write(co2_query.encode())
    resp_co2=ser.readline()
    act_co2=resp_co2[22:25].decode()
    act_co2=float(act_co2)
    print(act_co2)
    
    URL = "http://localhost/serial_api.php"

    PARAMS = { 'device_id':device_id,'inc_co2':act_co2,'inc_temp':act_temp }
    
    r = requests.post(url = URL, data = PARAMS,timeout=5)

    print(r.text)
    print(r.status_code)
"""
#end of multi serial port code
#uncomment the following to enable single serial port device

device_id = "inc_1"

BAUDRATE = 9600
PORT = "/dev/ttyUSB0"
TIMEOUT=1


temp_query= '?:2010:00::c3\r'
co2_query= '?:2020:00::c0\r'

ser = serial.Serial(port=PORT,baudrate=BAUDRATE,timeout=TIMEOUT)

ser.write(temp_query.encode())
resp_temp=ser.readline()
act_temp=resp_temp[18:25].decode()
act_temp=float(act_temp)
print(act_temp)


ser.write(co2_query.encode())
resp_co2=ser.readline()
act_co2=resp_co2[22:25].decode()
act_co2=float(act_co2)
print(act_co2) 



URL = "http://localhost/serial_api.php"

PARAMS = { 'device_id':device_id,'inc_co2':act_co2,'inc_temp':act_temp }

r = requests.post(url = URL, data = PARAMS,timeout=5)

print(r.text)
print(r.status_code)


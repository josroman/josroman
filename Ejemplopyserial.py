#!/usr/bin/env python
import time
import pigpio
import serial

#tiempo de muestreo
Ts = 0.01
t = 0.0

pi = pigpio.pi()
GPin = 13
pi.set_mode(GPin,pigpio.OUTPUT)
flag = 0
#ser = serial.serial("/dev/ttyACM0",115200,baudrate=115200,
#parity = serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE)

if __name__ == '__main__':
	ser = serial.Serial('/dev/ttyACM0',115200)
	ser.reset_input_buffer()
	
	while True:
	
		if ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			if flag == 0:
				flag=1
			else:
				flag=0

			pi.write(GPin,flag)
			print(round(t,3),'\t' ,float(line))
			t = t + Ts
			
pi.stop()	

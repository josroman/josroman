#!/usr/bin/env python

import pigpio
import time

GPIO = 4    		#Numero del GPIO        
pi = pigpio.pi()		#Conectarse al local
pi.set_mode(GPIO,pigpio.OUTPUT)

while True:
	pi.write(GPIO,0)
	time.sleep(1)
	pi.write(GPIO,1)
	time.sleep(0.5)
pi.stop()


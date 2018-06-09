# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 17:31:29 2018

@author: Paul
"""

#!/usr/bin/env python

import RPi.GPIO as GPIO
import time 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

pwm = GPIO.PWM(12, 50)
pwm.start(0)

while True:

    for (i) in range(100):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.1)

    for (i) in range(100, 0, -1):
        pwm.ChangeDutyCycle(i) 
        time.sleep(0.1)
    
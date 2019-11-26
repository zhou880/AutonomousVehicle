#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for running all motors while a touch sensor connected to PORT_1 of the BrickPi3 is being pressed.
# 
# Hardware: Connect EV3 or NXT motor(s) to any of the BrickPi3 motor ports. Make sure that the BrickPi3 is running on a 9v power supply.
#
# Results:  When you run this program, the motor(s) speed will ramp up and down while the touch sensor is pressed. The position for each motor will be printed.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division                                 

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

time1 = time.time()

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

timeElapsed = 3 #time desired for motor to run
try:
    while True:
        
        while (time.time() - time1) < timeElapsed:
            BP.set_motor_power(BP.PORT_A, 50) #set motor power
            time.sleep(0.02)# delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.
            print("Time elapsed is", time.time() - time1)
        #after time elapsed has passed
        BP.set_motor_power(BP.PORT_A, 0)
            

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.


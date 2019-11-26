#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading an NXT ultrasonic sensor connected to PORT_1 of the BrickPi3
# 
# Hardware: Connect an NXT ultrasonic sensor to BrickPi3 Port 1.
# 
# Results:  When you run this program, you should see the distance in CM.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers
import grovepi

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

# Configure for an NXT ultrasonic sensor.
# BP.set_sensor_type configures the BrickPi3 for a specific sensor.
# BP.PORT_1 specifies that the sensor will be on sensor port 1.
# BP.SENSOR_TYPE.NXT_ULTRASONIC specifies that the sensor will be an NXT ultrasonic sensor.
BP.set_sensor_type(BP.PORT_1, BP.SENSOR_TYPE.EV3_ULTRASONIC_CM)

time1 = time.time()
time_turn = 1
stop_dist = 40
forward_speed = 50
side_stop_dist = 40



try:
    while True:

        # read and display the sensor value
        # BP.get_sensor retrieves a sensor value.
        # BP.PORT_1 specifies that we are looking for the value of sensor port 1.
        # BP.get_sensor returns the sensor value (what we want to display).
        try:
            while BP.get_sensor(BP.PORT_1) > stop_dist:
                print(BP.get_sensor(BP.PORT_1))
                BP.set_motor_power(BP.PORT_A, forward_speed)
                BP.set_motor_power(BP.PORT_D, forward_speed)
                    
            if grovepi.ultrasonicRead(4) < side_stop_dist:
                #BP.set_motor_power(BP.PORT_A, 0)
                #BP.set_motor_power(BP.PORT_B, 0)
                while (time.time() - time1) < time_turn:
                    BP.set_motor_power(BP.PORT_A, 10) #set motor power
                    BP.set_motor_power(BP.PORT_D, -10) #set motor opposite to other to turn
                    time.sleep(0.02)# delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.
                    print("Time elapsed is", time.time() - time1)
                    #after timeElapsed has passed
                BP.set_motor_power(BP.PORT_A, 0)
                BP.set_motor_power(BP.PORT_D, 0)
            elif grovepi.ultrasonicRead(8) < side_stop_dist:
                #BP.set_motor_power(BP.PORT_A, 0)
                #BP.set_motor_power(BP.PORT_B, 0)
                while (time.time() - time1) < time_turn:
                    BP.set_motor_power(BP.PORT_A, -10) #set motor power
                    BP.set_motor_power(BP.PORT_D, 10) #set motor opposite to other to turn
                    time.sleep(0.02)# delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.
                    print("Time elapsed is", time.time() - time1)
                    #after timeElapsed has passed
                BP.set_motor_power(BP.PORT_A, 0)
                BP.set_motor_power(BP.PORT_D, 0)

        except brickpi3.SensorError as error:
            print(error)
        
        time.sleep(0.05)  # delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.

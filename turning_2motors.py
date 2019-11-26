import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

time1 = time.time()

BP = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. BP will be the BrickPi3 object.

timeElapsed = 2 #time desired for robot to spin
timeForward = 5
try:
    while True:
        
        while (time.time() - time1) < timeElapsed:
            BP.set_motor_power(BP.PORT_A, 50) #set motor power
            BP.set_motor_power(BP.PORT_D, -50) #set motor opposite to other to turn
            time.sleep(0.02)# delay for 0.02 seconds (20ms) to reduce the Raspberry Pi CPU load.
            print("Time elapsed from turning is: ", time.time() - time1)
        #after timeElapsed has passed
        while (time.time() - time1) < (timeForward + timeElapsed):
            BP.set_motor_power(BP.PORT_A, 30)
            BP.set_motor_power(BP.PORT_D, 30)
            print("Time elapsed from moving forward is: ", (time.time() - timeElapsed) - time1)
            #after forward time has elapsed:
        BP.set_motor_power(BP.PORT_A, 0)
        BP.set_motor_power(BP.PORT_D, 0)
            

except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
    BP.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.




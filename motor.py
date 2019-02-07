import time

# setup the main library for GPIO control.
import pigpio

# Set up an object for this pi via the library.
pi = pigpio.pi()

# Set the three pins used to outputs.
pi.set_mode(20, pigpio.OUTPUT)
pi.set_mode(21, pigpio.OUTPUT)
pi.set_mode(16, pigpio.OUTPUT)

# Write the motor enable
pi.write(21, 1)

try:
    while True:

        # Move in one direction by setting one output high and the other low.
        pi.write(16, 1)
        pi.write(20, 0)
        print("16 = 1 20 =0")
        time.sleep(2)

        # Go back in the other direction at 50% PWM.
        pi.set_PWM_dutycycle(20, int(.5 * 255))
        pi.write(16, 0)
        print("16 = 0 20 = 20%pwm")
        time.sleep(2)

finally:
    # Shunt down the motor - otherwise will continute ot turn in last direction.
    pi.write(16,0)
    pi.write(20,0)
    pi.write(21,0)

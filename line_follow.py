# Write your code here!

from botcore import *
from time import sleep

motor_left = 0
motor_right = 0

def add_left(value):
    return motor_left - value, motor_right + value

def add_right(value):
    return motor_left + value, motor_right - value

def reset_motor(value):
    return value, value

motors.enable(True)

while(1):

    result = ls.check(thresh=2000)
    leds.ls(result)

    motor_left, motor_right = reset_motor(30)

    if (result[0] and not result[2]):
        motor_left, motor_right = add_left(15)
    if (result[1]):
        motor_left, motor_right = add_left(5)
    if (result[4] and not result[2]):
        motor_left, motor_right = add_right(15)
    if (result[3]):
        motor_left, motor_right = add_right(5)
    
    if not result[0]:
        motor_left, motor_right = add_right(10)
    if not result[4]:
        motor_left, motor_right = add_left(10)
    
    if motor_left > 100:
        motor_left = 100
    if motor_left < -100:
        motor_left = -100
    if motor_right > 100:
        motor_right = 100
    if motor_right < -100:
        motor_right = -100
    motors.run(LEFT, motor_left)
    motors.run(RIGHT, motor_right)

motors.enable(False)

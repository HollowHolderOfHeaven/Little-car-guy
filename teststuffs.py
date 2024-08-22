from machine import Pin, PWM, time_pulse_us
from time import sleep

#Motors code
def Motors():
#Code for the 1st motor pins

motor1Enable = PWM(Pin(6, Pin.OUT))
motor1PositivePin = Pin(5, Pin.OUT)
motor1Negativepin = Pin(4, Pin.OUT)

#Code for the 2nd motor pins
motor2Enable = PWM(Pin(8, Pin.OUT))
motor2PositivePin = Pin(7, Pin.OUT)
motor2Negativepin = Pin(4, Pin.OUT)

#Setting speed of the 1st motor
motor1Enable.freq(1000)




#2nd motor code pins
motor2Enable.duty_u16(65535)
motor2PositivePin.off()
motor2Negativepin.on()

#Setting speed of the 2nd motor
motor2Enable.freq(1000)


#temporary code to turn off motors after 5 seconds for testing
sleep(5)

motor1Enable.duty_u16(0)
motor2Enable.freq(0)
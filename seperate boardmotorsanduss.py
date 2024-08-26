from machine import Pin, PWM, time_pulse_us
from time import sleep

echoPin = Pin(16, Pin.IN)
triggerPin = Pin(17, Pin.OUT)

motor1Enable = PWM(Pin(6, Pin.OUT))
motor1PositivePin = Pin(5, Pin.OUT)
motor1Negativepin = Pin(4, Pin.OUT)

motor1Enable.freq(1000)

motor1Enable.duty_u16(65535)
motor1PositivePin.on()
motor1Negativepin.off()



#nunm 2

motor2Enable = PWM(Pin(15, Pin.OUT))
motor2PositivePin = Pin(14, Pin.OUT)
motor2Negativepin = Pin(13, Pin.OUT)

motor2Enable.freq(1000)

motor2Enable.duty_u16(65535)
motor2PositivePin.on()
motor2Negativepin.off()

sleep(5)


motor1Enable = PWM(Pin(6, Pin.OUT))
motor1PositivePin = Pin(5, Pin.OUT)
motor1Negativepin = Pin(4, Pin.OUT)

motor1Enable.freq(1000)

motor1Enable.duty_u16(65535)
motor1PositivePin.off()
motor1Negativepin.off()


motor2Enable = PWM(Pin(15, Pin.OUT))
motor2PositivePin = Pin(14, Pin.OUT)
motor2Negativepin = Pin(13, Pin.OUT)

motor2Enable.freq(1000)

motor2Enable.duty_u16(65535)
motor2PositivePin.off()
motor2Negativepin.off()

echoPin = Pin(16, Pin.IN)
triggerPin = Pin(17, Pin.OUT)


while True:
    
    triggerPin.low()
    sleep(0.05)

    triggerPin.high()
    sleep(0.01)
    triggerPin.low()
    
    duration = time_pulse_us(echoPin, 1)
    distance_cm = 340 * duration / 20000
    print (distance_cm)
    sleep(0.5)
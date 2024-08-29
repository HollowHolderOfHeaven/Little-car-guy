from machine import Pin, PWM, time_pulse_us
from time import sleep

echoPin = Pin(17, Pin.IN)
triggerPin = Pin(18, Pin.OUT)


led1 = Pin(10, Pin.OUT)
led2 = Pin(11, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)

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
    
    if distance_cm < 20:
        led1.on()
    else:
        led1.off()
    if distance_cm < 15:
        led2.on()
    else:
        led2.off()
    if distance_cm < 10:
        led3.on()
    else:
        led3.off()
    if distance_cm < 5:
        led4.on()
    else:
        led4.off()
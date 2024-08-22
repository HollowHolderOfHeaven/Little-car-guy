#Nessecary imports
from machine import Pin, PWM, time_pulse_us
from time import sleep

class Car:
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


    motor1Enable.duty_u16(65535)
    motor1PositivePin.off()
    motor1Negativepin.on()

    #Setting speed of the 2nd motor
    motor2Enable.freq(1000)


    motor2Enable.duty_u16(65535)
    motor2PositivePin.off()
    motor2Negativepin.on()

    #temporary code to turn off motors after 5 seconds for testing
    sleep(5)

    motor1Enable.duty_u16(0)
    
    #LED Pins
    LED1 = Pin(9, Pin.OUT)
    LED2 = Pin(10, Pin.OUT)
    LED3 = Pin(11, Pin.OUT)
    LED4 = Pin(12, Pin.OUT)

    #Below is the code for the ultrasonic senor


    #The pins
    echoPin = Pin(16, Pin.IN)
    triggerPin = Pin(17, Pin.OUT)

    #Ultrasonic sensor activation
    while True:
    
    triggerPin.low()
    sleep(0.05)

    triggerPin.high()
    sleep(0.01)
    triggerPin.low()
    
    duration = time_pulse_us(echoPin, 1)
    distance_cm = 340 * duration / 20000
    
    #Print to test if Ultrasonic sensor is working (temporary)
    print (distance_cm)
    sleep(0.5)
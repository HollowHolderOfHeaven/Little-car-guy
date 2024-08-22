#Nessecary imports
from machine import Pin, PWM, time_pulse_us
from time import sleep

class Car:
    
    def __init__(self) -> None:
        self.LED1 = Pin()
        self.LED2 = Pin()
        self.LED3 = Pin()
        self.LED4 = Pin()
    
        self.sleep = Pin()
        
        
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
    
    #LED Pins
    def LEDs(self):
        
        sleep(0.000001)
        self.LED1 = Pin(9, Pin.OUT)
        self.LED2 = Pin(10, Pin.OUT)
        self.LED3 = Pin(11, Pin.OUT)
        self.LED4 = Pin(12, Pin.OUT)


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
        if distance_cm < 20:
            LED1.on()
        else:
            LED1.off()
        if distance_cm < 15:
            LED2.on()
        else:
            LED2.off()
        if distance_cm < 10:
            LED3.on()
        else:
            LED3.off()
        if distance_cm < 5:
            LED4.on()
        else:
            LED4.off()
            
            
        
    
    #Print to test if Ultrasonic sensor is working (temporary)

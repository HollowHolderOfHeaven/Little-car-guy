from machine import Pin, PWM, time_pulse_us
from time import sleep



#second motor code
button = Pin(0, Pin.IN)



while True:

    if button.value() == True:
        print ("button is pressed")
        motor2Enable = PWM(Pin(6, Pin.OUT))
        motor2PositivePin = Pin(5, Pin.OUT)
        motor2Negativepin = Pin(4, Pin.OUT)

        motor2Enable.freq(1000)

        motor2Enable.duty_u16(65535)
        motor2PositivePin.on()
        motor2Negativepin.off()

        #motor 1 code

        motor1Enable = PWM(Pin(20, Pin.OUT))
        motor1PositivePin = Pin(21, Pin.OUT)
        motor1Negativepin = Pin(22, Pin.OUT)



        motor1Enable.freq(1000)


        motor1Enable.duty_u16(65535)
        motor1PositivePin.on()
        motor1Negativepin.off()
        sleep(0.5)
        echoPin = Pin(17, Pin.IN)
        triggerPin = Pin(18, Pin.OUT)


        led1 = Pin(10, Pin.OUT)
        led2 = Pin(11, Pin.OUT)
        led3 = Pin(13, Pin.OUT)
        led4 = Pin(12, Pin.OUT)


            
        triggerPin.low()
        sleep(0.05)

        triggerPin.high()
        sleep(0.01)
        triggerPin.low()
            
        duration = time_pulse_us(echoPin, 1)
        distance_cm = 340 * duration / 20000
        print (distance_cm)
        
            
        if distance_cm < 20:
            led1.on()
            print (distance_cm)
        else:
            led1.off()
            print (distance_cm)
        if distance_cm < 15:
            led2.on()
            print (distance_cm)
        else:
            led2.off()
            print (distance_cm)
        if distance_cm < 10:
            led3.on()
            print (distance_cm)
        else:
            led3.off()
            print (distance_cm)
        if distance_cm < 5:
            led4.on()
            motor1Enable.duty_u16(0)
            print (distance_cm)
            motor2Enable.duty_u16(0)
            sleep(1)
            led1.off()
            led2.off()
            led3.off()
            led4.off()
            break
        else:
            led4.off()
            print (distance_cm)

    else: 
        print ("Button is not pressed")



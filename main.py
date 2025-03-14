# interrupt tutorial: https://electrocredible.com/raspberry-pi-pico-external-interrupts-button-micropython/
from machine import Pin
import time

#button = Pin(14,Pin.IN,Pin.PULL_UP) #Pi Pico 2
button = Pin(26,Pin.IN,Pin.PULL_UP) #Xiao RP2350
#led= machine.Pin(15, machine.Pin.OUT) #Pi Pico 2
led= machine.Pin(27, machine.Pin.OUT) #Xiao RP2350
flowcontroltime= time.ticks_ms()
buttontime= time.ticks_ms()

shouldblink = 0 # "0" means the LED should NOT blink, "1" it should blink

def myFunction(button):
    global shouldblink
    global buttontime
    
    if time.ticks_diff(time.ticks_ms(), buttontime) > 500: # this IF will be true every 5	00 ms
        buttontime= time.ticks_ms() #update with the "current" time
        
        print("Interrupt has occured")
        
        if shouldblink == 0: # alternate between blinking and not blinking, for every button press
            shouldblink = 1
        else:
            shouldblink = 0

while True:
    button.irq(trigger=Pin.IRQ_RISING, handler=myFunction)
    
    # non-blocking code from: https://fritzenlab.net/2025/03/11/ds18b20-temperature-sensor-with-micropython/
    if time.ticks_diff(time.ticks_ms(), flowcontroltime) > 200: # this IF will be true every 200 ms
            flowcontroltime= time.ticks_ms() #update with the "current" time
            
            if shouldblink == 0:
                led.value(0)
            else:
                if led.value() == 0:
                    led.value(1)
                else:
                    led.value(0)
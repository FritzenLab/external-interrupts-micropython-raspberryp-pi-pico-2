# interrupt tutorial: https://electrocredible.com/raspberry-pi-pico-external-interrupts-button-micropython/
from machine import Pin
import time

button = Pin(14,Pin.IN,Pin.PULL_UP)
led= machine.Pin(15, machine.Pin.OUT)
flowcontroltime= time.ticks_ms()
buttontime= time.ticks_ms()

shouldblink = 0 # "0" means the LED should NOT blink, "1" it should blink

def myFunction(button):
    global shouldblink
    global buttontime
    
    if time.ticks_diff(time.ticks_ms(), buttontime) > 200: # this IF will be true every 200 ms
        buttontime= time.ticks_ms() #update with the "current" time
        
        print("Interrupt has occured")
        
        if shouldblink == 0:
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
from machine import Pin
import time

n = 1

led1 = Pin(18, Pin.OUT)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

while True:
    if sw5.value() == 1:
        time.sleep_ms(100)
        if sw5.value() == 0:
            n+=1
    if n % 2 == 0:
        led1.on()
    else:
        led1.off()


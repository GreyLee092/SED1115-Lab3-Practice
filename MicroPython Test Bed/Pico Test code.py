import time
import machine
print("Hello World!")
led = machine.Pin("LED", machine.Pin.OUT)
while True:
 led.on()
 time.sleep_ms(500)
 led.off()
 time.sleep_ms(500)
from machine import Pin

led1 = Pin(18, Pin.OUT)
led2 = Pin(16, Pin.OUT)
led3 = Pin(17, Pin.OUT)
led4 = Pin(20, Pin.OUT)
led5 = Pin("LED", Pin.OUT)
sw1 = Pin(10, Pin.IN, Pin.PULL_DOWN)
sw2 = Pin(11, Pin.IN, Pin.PULL_DOWN)
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)
sw4 = Pin(13, Pin.IN, Pin.PULL_DOWN)
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

while True:
	if sw1.value() != 1:
		led1.on()
	else:
		led1.off()

	if sw2.value() != 1:
		led2.on()
	else:
		led2.off()

	if sw3.value() != 1:
		led3.on()
	else:
		led3.off()

	if sw4.value() != 1:
		led4.on()
	else:
		led4.off()

	if sw5.value() != 1:
		led5.on()
	else:
		led5.off()

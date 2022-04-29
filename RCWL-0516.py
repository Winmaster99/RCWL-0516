from machine import Pin

RCWL = Pin(6,Pin.IN)

while True:
    if RCWL.value():
        print("detected")
    else:
        print("not detected")

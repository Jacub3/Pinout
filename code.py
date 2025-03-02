import pwmio
import board
import analogio
import digitalio
import time

pwm = pwmio.PWMOut(board.GP13)
pwmspeaker = pwmio.PWMOut(board.GP6)

pin = analogio.AnalogIn(board.GP26)

pintestin= digitalio.DigitalInOut(board.GP0)
pintestout= digitalio.DigitalInOut(board.GP15)

pintestin.direction = digitalio.Direction.INPUT
pintestout.direction = digitalio.Direction.OUTPUT

ison = False




while True:
    pwm.duty_cycle= pin.value 
    time.sleep(0.1)
    
    print(pin.value & 0xFFF)
    
    if pintestin.value:
        ison = not ison
        pintestout.value=ison
        time.sleep(1)

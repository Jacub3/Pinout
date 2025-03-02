# Import necessary libraries
import pwmio        # Library to control PWM signals (Pulse Width Modulation)
import board        # Library to access the pins on the microcontroller
import analogio     # Library to interact with analog pins (e.g., read sensor values)
import digitalio    # Library to interact with digital input/output pins
import time         # Library for time-related functions, like delays

# Initialize PWM output on pin GP13 (used for controlling some hardware, e.g., motor, LED)
pwm = pwmio.PWMOut(board.GP13)

# Initialize PWM output on pin GP6 (likely used for controlling a speaker or other PWM device)
pwmspeaker = pwmio.PWMOut(board.GP6)

# Initialize analog input pin GP26 (used to read an analog sensor, like a potentiometer)
pin = analogio.AnalogIn(board.GP26)

# Initialize digital input pin GP0 (could be a button or switch)
pintestin = digitalio.DigitalInOut(board.GP0)

# Initialize digital output pin GP15 (could control an LED, relay, etc.)
pintestout = digitalio.DigitalInOut(board.GP15)

# Set the direction of the pins (input or output)
pintestin.direction = digitalio.Direction.INPUT
pintestout.direction = digitalio.Direction.OUTPUT

# Variable to track the on/off state of pintestout
ison = False

# Main loop
while True:
    # Set PWM duty cycle based on the analog input value from pin
    pwm.duty_cycle = pin.value
    
    # Add a delay of 0.1 seconds to avoid excessive polling
    time.sleep(0.1)
    
    # Print the analog input value (bitwise AND with 0xFFF to limit it to 12 bits)
    print(pin.value & 0xFFF)
    
    # Check if pintestin (input) is HIGH (button pressed or switch on)
    if pintestin.value:
        # Toggle the state of ison (True/False) when the pin value is HIGH
        ison = not ison
        
        # Set the output pin (pintestout) to match the new state of ison
        pintestout.value = ison
        
        # Delay to avoid bouncing or repeated toggles within a short period
        time.sleep(1)

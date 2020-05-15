
#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

# Pin Definitons:
Enable = 31  # BOARD pin 31 blue
DirA = 29  # BOARD pin 29 yelloq
DirB = 33 # BOARD pin 35 green

def main():
    prev_value = None

    # Pin Setup:
    GPIO.setmode(GPIO.BOARD)  # BOARD pin-numbering scheme
    #GPIO.setmode(GPIO.BCM) 
    GPIO.setup(Enable, GPIO.OUT, initial = GPIO.HIGH)  # Enable pin set as output
    GPIO.setup(DirA, GPIO.OUT)  # Dir A pin as output
    GPIO.setup(DirB, GPIO.OUT) #	Dir B pin set as output

    # Initial state for motors to yeet:
    print("Yeet")
    GPIO.output(Enable, GPIO.HIGH)
    GPIO.output(DirA, GPIO.LOW)
    GPIO.output(DirB, GPIO.HIGH)

    time.sleep(0.8)
    print("Dispense")
    GPIO.output(Enable, GPIO.LOW)
	
    time.sleep(1)
    print("Go Back")
    GPIO.output(DirA, GPIO.HIGH)
    GPIO.output(DirB, GPIO.LOW)
    GPIO.output(Enable, GPIO.HIGH)
    
    time.sleep(0.2)
    print("Done")
    GPIO.output(Enable, GPIO.LOW)
    GPIO.cleanup()

	

    
    

if __name__ == '__main__':
    main()

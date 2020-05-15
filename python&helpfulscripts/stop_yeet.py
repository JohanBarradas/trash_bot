#!/usr/bin/env python

import RPi.GPIO as GPIO

Enable = 31

def main():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Enable, GPIO.OUT,initial = GPIO.LOW)
    #while True:
    #try:
    GPIO.output(Enable, GPIO.LOW)
    #except KeyboardInterrupt:
        #GPIO.cleanup()
       # sys.exit()


if __name__ == '__main__':
    main()


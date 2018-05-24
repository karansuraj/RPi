import RPi.GPIO as GPIO, time, signal, sys, os


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

i = .02

try:
    while(1):
        GPIO.output(17,True)
        time.sleep(i)
        GPIO.output(17, False)
        time.sleep(i)
except KeyboardInterrupt:
    print('Program Interrupted')
    try:
        #GPIO.output(17,False)
        GPIO.cleanup()
    except SystemExit:
        os._exit(0)



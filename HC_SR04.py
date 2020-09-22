import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

def ping(isPlayer1):
	GPIO.setmode(GPIO.BCM)
	TRIG = 23 if isPlayer1 else 5
	ECHO = 24 if isPlayer1 else 6

	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

	GPIO.output(TRIG, False)
	time.sleep(0.01)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	pulse_start, pulse_end = 0, 0
	while GPIO.input(ECHO) == 0:
		pulse_start = time.time()

	while GPIO.input(ECHO) == 1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	GPIO.cleanup()
	return distance
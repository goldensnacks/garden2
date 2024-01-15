import time
import logging
import RPi.GPIO as GPIO
import sys

def main(pin_pump, run_time, sleep_time):
    GPIO.setwarnings(False)          # ignore warnings (unrelevant here)
    GPIO.setmode(GPIO.BCM)           # refer to GPIO pin numbers
    GPIO.setup(pin_pump, GPIO.OUT)    # Pi can send voltage to pump
    logging.info("Pump on for {} seconds".format(run_time))
    GPIO.output(pin_pump, GPIO.LOW)   # turn pump off

    GPIO.output(pin_pump, GPIO.HIGH)  # turn pump on
    time.sleep(int(run_time))         # wait for run_time seconds
    GPIO.output(pin_pump, GPIO.LOW)   # turn pump off



if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 garden.py <pin_pump> <run_time> <sleep_time>")
        sys.exit(1)
    else:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
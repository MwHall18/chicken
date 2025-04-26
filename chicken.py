import serial
import time
import RPi.GPIO as GPIO
import os
import subprocess
import signal
from multiprocessing import Process

# Setup LED
LED_PIN = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

# Setup relay
RELAY_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)
GPIO.output(RELAY_PIN, GPIO.LOW) # Make sure relay starts off

# Import the audio file
AUDIO_FILE = "bearscare.wav"
audio_playing = False

# Distance determanants
last_distance = None
THRESHOLD_DIFF = 0.5  # meters

def read_uart_distance():
    """ Read distance from UART-connected lidar """

    # Reinitialize the UART connection
    ser = serial.Serial('/dev/serial0', 115200, timeout=1)
    time.sleep(0.1)  # Allow time for the connection to stabilize
    
    if ser.in_waiting >= 9:
        data = ser.read(9)
        if data[0] == 0x59 and data[1] == 0x59: # Bit range for UART lidar data
            distance = data[2] + data[3] * 256 # calculations to put to cm
            ser.close()  # Close the connection after reading
            return distance / 100.0  # convert to meters
    ser.close()  # Ensure the connection is closed if no valid data
    return None

try:
    while True:
        distance = read_uart_distance()
        if distance is not None:
            # Print the initial reading or if the change exceeds the threshold - Debugging purposes
            if last_distance is None or abs(distance - last_distance) >= THRESHOLD_DIFF:
                if last_distance is None:
                    print(f"Initial Distance: {distance:.2f} m")
                elif distance <= 1: # printing 1 for debugging purposes - 4,3,2 detect through other means
                    print(f"WARNING: Object within 1m! ({distance:.2f} m)")
                elif distance <= 5: # printing 5 for debugging purposes - 4,3,2 detect through other means
                    print(f"Notice: Object within 5m ({distance:.2f} m)")
                else:
                    print(f"Distance: {distance:.2f} m")
                last_distance = distance  # Update the last distance
                
            # LED control: Turn on within 4 meters, off otherwise
            if distance <= 4:
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_PIN, GPIO.LOW)

            # Audio control: Play within 3 meters, stop otherwise
            if distance <= 3:
                if not audio_playing:
                    process = subprocess.Popen(['aplay', '-D', 'plughw:3,0', 'bearscare.wav'])
                    audio_playing = True
            else:
                if audio_playing:
                    os.kill(process.pid, 9)
                    audio_playing = False

            # Under 2 meters, turn pump on
            if distance <= 2:
                GPIO.output(RELAY_PIN, GPIO.HIGH)
                print("Pump on")
            else:
                GPIO.output(RELAY_PIN, GPIO.LOW)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting.")
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(RELAY_PIN, GPIO.LOW)
    os.kill(process.pid, 9)  # Ensure audio stops
'''
analog test
pin A0 --> esp32 gpio2
Stellsschraube ziemlich ganz rechts, Ausgabe: "No Sound", bei Geräusch "sound detected"
led02 auf sensor ist aus, bei Geräuscherkennung blinkt er
'''

import machine
import time

ANALOG_PIN = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    analog_value = ANALOG_PIN.value()
    print("| Analog State:", "Sound Detected" if analog_value == 1 else "No Sound")
    time.sleep(1)

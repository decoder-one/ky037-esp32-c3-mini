'''
Raspberry Pi Pico/esp32 an KY-037
Pin 2 -> D0
Pin 3V3 
Pin GND

digital
zählt hoch bei Lärm
'''

# Bibliotheken laden
from machine import Pin, Timer
from time import sleep

# Initialisierung von GPIO22 als Eingang
sensor = Pin(2, Pin.IN)

# Zähler
count = 0

# Start
print('Bereit')
print()

# Funktion: Zähler
def release(Pin):
    #print('Ausgelöst')
    #print()
    if sensor.value() == 1:
        global count
        count = count + 1
        print('Zähler:', count)
        print()
    sleep(0.2)

# Interrupt für die Geräuscherkennung
sensor.irq(trigger=Pin.IRQ_RISING, handler=release)
import machine
import urequests 
from machine import Pin
import time, network
import dht

sensor = dht.DHT11(Pin(26))

HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'Your API Key' 

UPDATE_TIME_INTERVAL = 5000  # in ms 
last_update = time.ticks_ms() 

# Configure ESP32 as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)

print('network config:', sta_if.ifconfig()) 

while True: 
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL: 
        while True:
            sensor.measure()
            temp = sensor.temperature()
            hum = sensor.humidity()
            print('Air Temperature: %3.1f C' %temp)
            print('Air Humidity: %3.1f %%' %hum)
            time.sleep(1)
            readings = {'field1':temp, 'field2':hum} 
            request = urequests.post( 'http://api.thingspeak.com/update?api_key=' + THINGSPEAK_WRITE_API_KEY,
                                     json = readings, headers = HTTP_HEADERS )  
            request.close() 
            print(readings) 

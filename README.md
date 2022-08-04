# DHT_Reading_On_ThingSpeak


# `goto this link` https://thingspeak.com/login `Click create one then fill all fields`

![image](https://user-images.githubusercontent.com/63813881/173555964-20010d7e-4d02-4fd3-866e-3668b74d8055.png)

# `Like this then press continue`
![image](https://user-images.githubusercontent.com/63813881/173556025-eac6c757-aefb-4cf3-889b-172543d2c6ae.png)
# `Click My Channel`
![image](https://user-images.githubusercontent.com/63813881/173556072-68d63227-28a2-41bd-8383-500beeab444a.png)

`We will define the channels by entering the a proper name, description, and up to 8 fields can be used to name the parameter. For the Field 1 and Field 2 we have named Temperature and humidity. These field values ​​that you set can be modified later. These values will be in Degree Centigrade and Relative Humidity in %. Once you update the name, click on Save.`
![image](https://user-images.githubusercontent.com/63813881/173556098-51c76d37-e8be-4721-a1d7-53168a5348be.png)

`Once you have saved the channel, you will be automatically redirected to the “Private View” tab. Here the mapped fields are shown as a diagram. You will find the “Channel ID” (we will need it later). Below You will also see API Keys option.`

![image](https://user-images.githubusercontent.com/63813881/173556137-4537918b-9680-47ef-ae7a-0ed1579803e3.png)

`Later, click on the “API Keys” tab. The two values ​​of “Write API key” and “Read API key” are equally necessary for us to write or retrieve data. Copy these keys and keep it safe as we need to put it in the code.`

![image](https://user-images.githubusercontent.com/63813881/173556171-4681026e-ac08-4264-91c3-32575a15a225.png)

<pre>
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
</pre>            

![image](https://user-images.githubusercontent.com/63813881/182765396-c5c76975-880f-4298-8497-f98baee4342b.png)
![image](https://user-images.githubusercontent.com/63813881/182765623-af6c7738-d553-4739-ac4d-e7dbcfafc53a.png)

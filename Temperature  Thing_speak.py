import RPi.GPIO as GPIO
import Adafruit_DHT
import Adafruit_DHT
import urllib.request
import time

key="8N210DXO1OXPA2AR"       # Enter your Write API key from ThingSpeak

sensor = Adafruit_DHT.DHT11           
pin = 3
GPIO.setwarnings(False)

URL = 'https://api.thingspeak.com/update?api_key=%s' % key

print("Temperature Sensor is getting ready")


try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            finalURL = URL +"&field2=%s&field1=%s"%(humidity, temperature)
            print (finalURL)
            s=urllib.request.urlopen(finalURL);
            s.close()
            time.sleep(2)
        else:
            print('Failed to get reading. Try again!')

except KeyboardInterrupt:                   # Reset by pressing CTRL + C
    print("Measurement stopped by User")
    GPIO.cleanup()


import RPi.GPIO as GPIO
import time
import urllib.request

TRIGGER = 3                              # set GPIO Pins
ECHO = 5

key="FXTU59MNQ15PRMB6"   
                            
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)                   # GPIO Mode (BOARD / BCM) 
GPIO.setup(ECHO, GPIO.IN)                  #set GPIO direction (IN / OUT)
GPIO.setup(TRIGGER, GPIO.OUT)  
 
URL = 'https://api.thingspeak.com/update?api_key=%s' % key 
 
def distance():

    GPIO.output(TRIGGER, True)         # set Trigger to HIGH
    time.sleep(0.00001)                      # 10 micro seconds
    GPIO.output(TRIGGER, False)         # set Trigger after 0.01ms to LOW
 
    StartTime = time.time()
    StopTime = time.time()
 
                                             
    while GPIO.input(ECHO) == 0:       # save StartTime
        StartTime = time.time()
 
   
    while GPIO.input(ECHO) == 1:       # save time of arrival
        StopTime = time.time()
 
    
    TimeElapsed = StopTime - StartTime       # time difference between start and arrival
    distance = (TimeElapsed * 34300) / 2     # multiply with the sonic speed (34300 cm/s) and divide by 2, because there and back
    return distance
    
    
 
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            finalURL = URL +"&field1=%s"%(dist)
            print (finalURL)
            s=urllib.request.urlopen(finalURL);
            s.close()
 
        
    except KeyboardInterrupt:                   # Reset by pressing CTRL + C
        print("Measurement stopped by User")
        GPIO.cleanup()


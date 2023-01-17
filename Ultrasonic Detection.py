import  RPi.GPIO as GPIO
import time
import httplib, urllib

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

TRIG=17
ECHO=4
led1=20
led2=25

i=1
print "Distance measurement in progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)

print "Waiting for sensor to settle"
time.sleep(1)
print "Sensor is settled"

while i>0:
   GPIO.output(TRIG,False)
   time.sleep(2)
   GPIO.output(TRIG,True)
   time.sleep(0.00001)
   GPIO.output(TRIG,False)
   while GPIO.input(ECHO)==0:
       pulse_start=time.time()
   while GPIO.input(ECHO)==1:
       pulse_end=time.time()
   pulse_duration = pulse_end - pulse_start
   distance = pulse_duration*17150
   distance = round(distance, 2)
   print "Distance:" ,distance,"cm"
   time.sleep(0.5)
   i=i+1

   if 1<distance<6:
       print "Obstacle is very near!! Stop the car immediately"
       GPIO.output(led1,GPIO.HIGH)
       GPIO.output(led2,GPIO.LOW)

   elif 7<distance<15:
      print "Approaching obstacle slow down your car"
      GPIO.output(led1,GPIO.LOW)
      GPIO.output(led2,GPIO.HIGH)

   elif distance>16:
      GPIO.output(led1,GPIO.LOW)
      GPIO.output(led2,GPIO.LOW)
      print "No obstacle near the car "

GPIO.cleanup()

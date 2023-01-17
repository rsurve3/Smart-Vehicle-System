Import sys
Import RPi.GPIO as g

From Adafruit_IO import MQTTClient

g.setmode(g.BCM)
g.setwarnings(False)
g.setup(24,g.OUT)

ADAFRUIT_IO_KEY = ‘449fc987bcfa46e4a298475a6272a58c’

ADAFRUIT_IO_USERNAME = ‘rahulsurve’

FEED_ID = ‘Home Automation’
def connected(client):

       print(‘Connected to Adafruit IO!  Listening for {0} changes…’ .format(FEED_ID))

       client.subscribe(FEED_ID)

def disconnected(client):
    
       print(‘Disconnected from Adafruit IO!’)
       sys.exit(1)

def message(client,   feed_id,  payload):

       print(‘Feed {0} received new value:  {1}’ .format(feed_id,  payload))
       if payload == ‘ON’:
            g.output(24,g.HIGH)
       elif payload == ‘OFF’:
            g.output(24,g.LOW)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

client.on_connect       =  connected
client.on_disconnect  =  disconnected
client.on_message      =  message
client.connect()
client.loop_blocking()

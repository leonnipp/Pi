#!/usr/bin/python
import sys
import Adafruit_DHT

humidity, temperature = Adafruit_DHT.read_retry(11, 4)
print 'conditions,valid_temperature=true,valid_humidity=true temperature={0:0.1f},humidity={1:0.1f}'.format(temperature, humidity)

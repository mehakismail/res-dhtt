import sys
import board
from time import sleep
import adafruit_dht as dht
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21,GPIO.OUT)


def DHT11_data():
    dhtdevice = dht.DHT11(board.D23)
    humi = dhtdevice.humidity
    temp = dhtdevice.temperature
    return humi, temp

def toggle_gpio(value):

    if value > 50:
        print("GPIO on")
        GPIO.output(21,GPIO.HIGH)
    if value < 50:
        print ("GPIO off")
        GPIO.output(21,GPIO.LOW)


while True:
    try:
        humi, temp = DHT11_data()
        humi = '%.2f' % humi 					   
        temp = '%.2f' % temp
        print ("humidity =" , humi)
        print ("temperature = ", temp)

        toggle_gpio(humi)
        
        sleep(5)
    
    except Exception as error1:
        print (error1)
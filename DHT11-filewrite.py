import sys
import board
from time import sleep
import adafruit_dht as dht

def DHT11_data():
    dhtdevice = dht.DHT11(board.D23)
    humi = dhtdevice.humidity
    temp = dhtdevice.temperature
    return humi, temp

def write_file(value):
    with open("/home/pi/logs.csv", "a+") as file:
        file.write(str(value)) 
while True:
    try:
        humi, temp = DHT11_data()
        humi = '%.2f' % humi 					   
        temp = '%.2f' % temp
        print ("humidity =" , humi)
        print ("temperature = ", temp)
        sleep(1)
        if temp > 30.0:

            write_file(temp)

        sleep(5)
    
    except Exception as error1:
        print (error1)
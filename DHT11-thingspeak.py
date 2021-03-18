import sys
import urllib3
import board
from time import sleep
import adafruit_dht as dht
# Enter Your API key here
myAPI = 'X3P1NR2G62NAMFOC' 
def DHT11_data():
    dhtdevice = dht.DHT11(board.D23)
    humi = dhtdevice.humidity
    temp = dhtdevice.temperature
    return humi, temp

def upload_data(value1,value2):
    link = 'https://api.thingspeak.com/update?api_key=0MMNKLS4N1JDZ1Q3&field1='+value1+'&field2='+value2
        http = urllib3.PoolManager()
        r = http.request('GET',link)
        print (r.status)
        sleep(2)

while True:
    try:
        humi, temp = DHT11_data()
        humi = '%.2f' % humi 					   
        temp = '%.2f' % temp
        print ("humidity = ", humi)
        print ("temperature = ", temp)
        sleep(2)
        upload_data(humi,temp)
        sleep(10)
        
    
    except Exception as error1:
        print (error1)
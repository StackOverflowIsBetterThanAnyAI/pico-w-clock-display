import network
import time
import machine

from lib.env import SSID, PASSWORD

led = machine.Pin('LED', machine.Pin.OUT)

def connect_to_wifi():
    try:
        wlan = network.WLAN(network.STA_IF)
        wlan.active(True)
        wlan.connect(SSID, PASSWORD)
        
        print("Connecting ...")
        
        while not wlan.isconnected():
            led.on()
            print("Waiting for Connection ...")
            time.sleep(0.5)
            led.off()
            print(wlan.status())
            if wlan.status() <= -1:
                raise Exception("Unable to connect to an Access Point.")
            time.sleep(0.25)
    
        print(f"Connected on: {wlan.ifconfig()[0]}")
        led.off()
        
    except Exception as e:
        print(f"An unexpected error has occured: {e}")
        
def disconnect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    print("Disconnected from WiFi.")
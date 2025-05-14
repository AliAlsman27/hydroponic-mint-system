import time
import board
import adafruit_dht

# Initialize DHT22
dht_device = adafruit_dht.DHT22(board.D17)

def read_dht():
    try:
        temperature_c = dht_device.temperature
        humidity = dht_device.humidity
        return temperature_c, humidity
    except RuntimeError:
        return None, None  # Ignore read errors
    except Exception as e:
        dht_device.exit()
        raise e

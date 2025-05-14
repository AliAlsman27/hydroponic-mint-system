import BlynkLib

BLYNK_AUTH = 'YourAuthTokenHere'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def send_to_blynk(temp, dht_temp, humidity, tds, ldr, ph, water_level):
    blynk.virtual_write(1, temp)
    blynk.virtual_write(2, dht_temp)
    blynk.virtual_write(3, humidity)
    blynk.virtual_write(4, tds)
    blynk.virtual_write(5, ldr)
    blynk.virtual_write(6, ph)
    blynk.virtual_write(7, water_level)

import time
from ds_sensor import read_temp
from dht_sensor import read_dht
from tds_sensor import read_tds
from ldr_sensor import read_ldr
from ph_sensor import read_ph
from water_sensor import is_water_present
from relay_control import relay_on, relay_off, relay2_on, relay2_off
from blynk_handler import send_to_blynk, blynk

# Relay timing variables
relay_timer = 0
relay_active = False

print("Main program started")

while True:
    current_time = time.time()

    # Read all sensors
    ds_temp = read_temp()
    dht_temp, dht_humidity = read_dht()
    tds = read_tds()
    ph = read_ph()
    ldr_value = read_ldr()
    water = is_water_present()

    print("\n=== Sensor Readings ===")
    if ds_temp is not None:
        print(f"DS18B20 Temp: {ds_temp:.2f} C")
    else:
        print("DS18B20 Temp: Read failed")

    if dht_temp is not None and dht_humidity is not None:
        print(f"DHT22 Temp: {dht_temp:.1f} C  Humidity: {dht_humidity:.1f}%")
    else:
        print("DHT22: Read failed")

    print(f"pH Value: {ph:.2f}" if ph is not None else "pH: Read failed")
    print(f"TDS: {tds:.2f} ppm" if tds is not None else "TDS: Read failed")
    print(f"LDR Light Level: {ldr_value:.2f}")
    print("Water detected ?" if water else "No water detected ?")

    # === Non-blocking auto control logic ===
    if tds is not None and tds < 600 and not relay_active:
        print("TDS low  turning relays ON for 15 seconds")
        relay_on()
        relay2_on()
        relay_timer = current_time + 15
        relay_active = True

    if relay_active and current_time > relay_timer:
        print("Relay timer expired  turning relays OFF")
        relay_off()
        relay2_off()
        relay_active = False

    # === Send to Blynk ===
    print("Sending data to Blynk...")
    send_to_blynk(ds_temp, dht_temp, dht_humidity, tds, ldr_value, ph, int(water))

    # Process Blynk switch commands (relays, etc.)
    blynk.run()

    # Short delay to prevent overload
    time.sleep(1)

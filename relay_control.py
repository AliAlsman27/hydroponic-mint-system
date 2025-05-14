from gpiozero import OutputDevice

# Relay connected to GPIOs
relay = OutputDevice(27, active_high=False, initial_value=False)
relay2 = OutputDevice(19, active_high=False, initial_value=False)
relay3 = OutputDevice(13, active_high=False, initial_value=False)

def relay_on():
    relay.off()

def relay_off():
    relay.on()

def relay2_on():
    relay2.off()

def relay2_off():
    relay2.on()

def relay3_on():
    relay3.off()

def relay3_off():
    relay3.on()

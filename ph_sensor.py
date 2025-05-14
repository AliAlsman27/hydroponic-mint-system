from gpiozero import MCP3008

# Connect AOUT to MCP3008 channel 2 (CH2)
ph_channel = MCP3008(channel=2)

def read_ph():
    voltage = ph_channel.value * 3.3  # Convert to voltage
    ph_value = (voltage * 5)  # Simple linear scale placeholder
    return ph_value

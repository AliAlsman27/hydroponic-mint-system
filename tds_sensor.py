from gpiozero import MCP3008
import time

# Create MCP3008 channel 0 (TDS analog output connected to CH0)
tds_channel = MCP3008(channel=0)

def read_tds():
    voltage = tds_channel.value * 5  # Convert to voltage
    tds_value = (133.42 * voltage**3 - 255.86 * voltage**2 + 857.39 * voltage) * 0.5
    return tds_value

from gpiozero import MCP3008

# Connect A0 from LDR module to MCP3008 channel 1 (CH1)
ldr_channel = MCP3008(channel=1)

def read_ldr():
    # Returns a float between 0.0 (dark) and 1.0 (bright)
    return ldr_channel.value

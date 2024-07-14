import smbus2
import time

# Define the I2C bus and address
I2C_BUS = 1
I2C_ADDRESS = 0x3e


bus = smbus2.SMBus(I2C_BUS)

def send_command(command):
    bus.write_byte_data(I2C_ADDRESS, 0x00, command)

def send_data(data):
    # Send data to the display
    bus.write_byte_data(I2C_ADDRESS, 0x40, data)

def initialize_display():
    # Initialize the display
    send_command(0x38)  # Function set: 8-bit, 2 line, 5x8 dots
    time.sleep(0.05)
    send_command(0x39)  # Function set: 8-bit, 2 line, 5x8 dots, extended instruction set
    time.sleep(0.05)
    send_command(0x14)  # Internal OSC frequency: Bias=1/5, Freq=183 Hz
    time.sleep(0.05)
    send_command(0x70)  # Contrast set: low byte
    time.sleep(0.05)
    send_command(0x56)  # Power/ICON/Contrast control: Ion, Bon, Contrast high byte
    time.sleep(0.05)
    send_command(0x6C)  # Follower control: internal follower mode, amp ratio
    time.sleep(0.2)
    send_command(0x38)  # Function set: 8-bit, 2 line, 5x8 dots
    time.sleep(0.05)
    send_command(0x0C)  # Display ON/OFF control: Display ON, Cursor OFF, Blink OFF
    time.sleep(0.05)
    send_command(0x01)  # Clear display
    time.sleep(0.05)

def display_message(message):
    # Clear the display
    send_command(0x01)
    time.sleep(0.05)
    
    # Set the cursor to the beginning of the first line
    send_command(0x80)
    
    # Write the message to the display
    for char in message:
        send_data(ord(char))

# Initialize the display
initialize_display()

# Display "123"
display_message("123")

# Import the necessary modules from pynput.keyboard
from pynput.keyboard import Key, Controller
import time

# Define the message you want to spam
message = "spamming"

# Create a Controller object to simulate keyboard input
keyboard = Controller()

# Wait for 8 seconds before starting the spamming
time.sleep(8)

# Loop 10 times to spam the message
for i in range(10):
    # Iterate through each character in the message
    for ch in message:
        # Simulate pressing and releasing the key
        keyboard.press(ch)
        keyboard.release(ch)
    
    # Simulate pressing and releasing the Enter key
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    
    # Wait for 0.2 seconds before typing the next character
    time.sleep(0.2)


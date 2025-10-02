import time
from pythonosc.udp_client import SimpleUDPClient

# Define the IP address and port for OSC messages
IP = "127.0.0.1"
PORT = 7700

# Initialize OSC client
client = SimpleUDPClient(IP, PORT)

# Define message values
VALUE = 255
TIME = 1
# Infinite loop to continuously send messages every 250ms
while True:
    # Send "/downbeat" once
    client.send_message("/downbeat", VALUE)
    print("*Beat!")
    time.sleep(TIME)

    # Send "/beat" three times
    for _ in range(3):
        client.send_message("/beat", VALUE)
        print("Beat!")
        time.sleep(TIME)

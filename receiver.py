# Temperature transmitter

import radio
from microbit import *

RADIO_GROUP = 10
radio.config(group=RADIO_GROUP)
radio.on()
display.scroll("{}".format(RADIO_GROUP))

while True:
    message = radio.receive()
    if message:
        print(message)
        display.show(Image.DIAMOND, delay=100, clear=True)

# Temperature transmitter

import radio
from microbit import *

# each sensor should have a different id
# to track where the temperature is coming from
# this can be a more meaningful string such as "dining_room_window"
SENSOR_ID = "01"


def format_radio_msg(t: int) -> str:
    return "{},{}".format(SENSOR_ID, t)


RADIO_GROUP = 10
radio.config(group=RADIO_GROUP)
radio.on()
display.scroll("{}".format(RADIO_GROUP))
display.scroll("{}".format(SENSOR_ID))

while True:
    t = temperature()
    display.scroll(t)
    radio.send(format_radio_msg(t))
    sleep(1000)

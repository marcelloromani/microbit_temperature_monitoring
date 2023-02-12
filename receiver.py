# Temperature transmitter

import radio
from microbit import *

RADIO_GROUP = 10
radio.config(group=RADIO_GROUP)
radio.on()
display.scroll("{}".format(RADIO_GROUP))


SENSOR_LIST = ["01", "02"]


# format of radio messages:
#
# Command sent by the control node
# C:<sensor_id>:<msg>
#
#   C = identifies the message as a (C)ommand
#   sensor_id = recipient of the command
#
# Response sent by sensor node
#
# R:<sensor_id>:<msg>
#
#   R = identifies the message as a (R)esponse to a command
#   sensor_id = which sensor the message is coming from


# each radio message is directed at a specific sensor
def send_msg(sensor_id: str, msg: str):
    s = "C:{}:{}".format(sensor_id, msg)
    print("S {}".format(s))
    radio.send(s)


while True:
    message = radio.receive()
    if message:
        print("R {}".format(message))
        continue

    if button_a.was_pressed():
        for sensor_id in SENSOR_LIST:
            send_msg(sensor_id, "PING")
        continue

    if button_b.was_pressed():
        for sensor_id in SENSOR_LIST:
            send_msg(sensor_id, "TEMP")
        continue

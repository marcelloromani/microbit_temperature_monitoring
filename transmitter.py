# Temperature transmitter

import radio
from microbit import *

SENSOR_ID = "01"


def temperature_msg(t: int) -> str:
    return "R:{}:TEMP,{}".format(SENSOR_ID, t)


def pong_msg() -> str:
    return "R:{}:PONG".format(SENSOR_ID)


RADIO_GROUP = 10
radio.config(group=RADIO_GROUP)
radio.on()
display.scroll("{}".format(RADIO_GROUP))
display.scroll("{}".format(SENSOR_ID))

while True:
    if button_a.was_pressed():
        radio.send(pong_msg())

    msg = radio.receive()
    if msg:
        msg_type, addr, msg = msg.split(":")
        if msg_type == "R":
            # ignore (R)eplies broadcast by other sensor nodes
            continue
        elif msg_type == "C":
            # process (C)ommands coming from the coordinator module
            if addr == SENSOR_ID:
                # only process (C)ommands meant for us
                if msg == 'TEMP':
                    t = temperature()
                    radio.send(temperature_msg(t))
                elif msg == 'PING':
                    radio.send(pong_msg())

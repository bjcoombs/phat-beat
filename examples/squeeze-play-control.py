#!/usr/bin/env python

import signal
import phatbeat

from pylms.server import Server
from pylms.player import Player

sc = Server(hostname="10.0.1.111", port=9090)
sc.connect()

sq = sc.get_player("00:04:20:1e:fd:59")

print("""
pHAT BEAT: Buttons

Shows off the various ways you can configure buttons on PHAT BEAT.

Press Ctrl+C to exit!

""")

@phatbeat.on(phatbeat.BTN_FASTFWD)
def fast_forward(pin):
    sq.next()
    print("FF Pressed")

@phatbeat.hold(phatbeat.BTN_FASTFWD, hold_time=2)
def hold_fast_forward(pin):
    sq.forward()
    print("FF Held")

@phatbeat.on(phatbeat.BTN_PLAYPAUSE)
def play_pause(pin):
    sq.toggle()
    print("PP Pressed")

@phatbeat.hold(phatbeat.BTN_PLAYPAUSE, hold_time=2)
def hold_play_pause(pin):
    sq.stop()
    print("PP Held")

@phatbeat.on(phatbeat.BTN_VOLUP)
def volume_up(pin):
    sq.volume_up()
    print("VU Pressed")

@phatbeat.hold(phatbeat.BTN_VOLUP)
def hold_volume_up(pin):
    sq.unmute()
    print("VU Held")

@phatbeat.on(phatbeat.BTN_VOLDN)
def volume_down(pin):
    sq.volume_down()
    print("VD Pressed")

@phatbeat.hold(phatbeat.BTN_VOLDN)
def hold_volume_down(pin):
    sq.mute()
    print("VD Held")

@phatbeat.on(phatbeat.BTN_REWIND)
def rewind(pin):
    sq.prev()
    print("RR Pressed")

@phatbeat.hold(phatbeat.BTN_REWIND)
def hold_rewind(btn):
    sq.rewind()
    print("RR Held")

@phatbeat.on(phatbeat.BTN_ONOFF)
def onoff(pin):

    print("OO Pressed")

@phatbeat.hold(phatbeat.BTN_ONOFF)
def hold_onoff(pin):
    sq.toggle()
    print("OO Held")

signal.pause()

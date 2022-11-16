# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Radomir Dopieralski
#
# SPDX-License-Identifier: Unlicense
import board
import busio
import paj7620


i2c = busio.I2C(board.SCL, board.SDA, frequency=400_000)
sensor = paj7620.PAJ7620Gesture(i2c)

while True:
    time.sleep(1)
    gesture = sensor.read()
    print(gesture)
    if gesture & paj7620.UP:
        print("up")
    if gesture & paj7620.DOWN:
        print("down")
    if gesture & paj7620.LEFT:
        print("left")
    if gesture & paj7620.RIGHT:
        print("right")
    if gesture & paj7620.NEAR:
        print("near")
    if gesture & paj7620.FAR:
        print("far")
    if gesture & paj7620.CW:
        print("cw")
    if gesture & paj7620.CCW:
        print("ccw")
    if gesture & paj7620.WAVE:
        print("wave")

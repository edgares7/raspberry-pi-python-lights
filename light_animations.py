# rpi_ws281x library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import math
import random

from rpi_ws281x import *
import signal
import sys
import datetime


# LED strip configuration:
LED_COUNT = 240     # Number of LED pixels.
LED_PIN = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# True to invert the signal (when using NPN transistor level shift)
LED_INVERT = False
LED_CHANNEL = 0
LED_STRIP = ws.SK6812_STRIP_RGBW
#LED_STRIP      = ws.SK6812W_STRIP

LED_1_COUNT      = 240      # Number of LED pixels.
LED_1_PIN        = 19      # GPIO pin connected to the pixels (must support PWM! GPIO 13 and 18 on RPi 3).
LED_1_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_1_DMA        = 1      # DMA channel to use for generating signal (Between 1 and 14)
LED_1_BRIGHTNESS = 255    # Set to 0 for darkest and 255 for brightest
LED_1_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_1_CHANNEL    = 1       # 0 or 1
LED_1_STRIP      = ws.SK6812_STRIP_RGBW

# LED_2_COUNT      = 240      # Number of LED pixels.
# LED_2_PIN        = 12      # GPIO pin connected to the pixels (must support PWM! GPIO 13 or 18 on RPi 3).
# LED_2_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_2_DMA        = 2      # DMA channel to use for generating signal (Between 1 and 14)
# LED_2_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
# LED_2_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
# LED_2_CHANNEL    = 0       # 0 or 1
# LED_2_STRIP      = ws.SK6812_STRIP_RGBW



def SetAll(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)


def SetAll1(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)


def SetAll2(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)


def everything(strip, color):
    for i in range(strip.numPixels()):
        SetAll(strip, color)
        strip.show()


def everything1(strip, color):
    for i in range(strip.numPixels()):
        SetAll1(strip, color)
        strip.show()


def everything2(strip, color):
    for i in range(strip.numPixels()):
        SetAll2(strip, color)
        strip.show()


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        # print(color)
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorWipe1(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        # print(color)
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorWipe2(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        # print(color)
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)


def colorSequence(strip, color, amount = 0):
    """Wipe color across display a pixel at a time."""
    for i in range(amount):
        # print(color)
        strip.setPixelColor(i, color)
        strip.show()


def colorSequence1(strip1, color, amount = 0):
    """Wipe color across display a pixel at a time."""
    for i in range(amount):
        # print(color)
        strip1.setPixelColor(i, color)
        strip1.show()


def colorSequence2(strip, color, amount = 0):
    """Wipe color across display a pixel at a time."""
    for i in range(amount):
        # print(color)
        strip.setPixelColor(i, color)
        strip.show()
                

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


"""
Done
"""
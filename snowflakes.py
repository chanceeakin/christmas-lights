# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data IN strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 50

# The order of the pixel colors - RGB or GRB.
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.RGB

WHITE = ((255, 255, 255))
LIGHT_BLUE = ((0, 0, 127))


pixels = neopixel.NeoPixel(
    pixel_pin,
    num_pixels,
    brightness=1,
    pixel_order=ORDER)


def first_cycle():
    for i in range(num_pixels):
        if (i % 2 == 0):
            pixels[i] = WHITE
        else:
            pixels[i] = LIGHT_BLUE
    pixels.show()
    time.sleep(1)


def second_cycle():
    for i in range(num_pixels):
        if (i % 2 == 0):
            pixels[i] = LIGHT_BLUE
        else:
            pixels[i] = WHITE
    pixels.show()
    time.sleep(1)


while True:
        first_cycle()
        second_cycle()

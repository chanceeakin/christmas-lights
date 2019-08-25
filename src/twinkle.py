import time
import neopixel
import board

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
    brightness=0.1,
    pixel_order=ORDER)


def twinkle(np):
    n = np.n

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            time.sleep(0.01 * j)
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, val, 255)
        np.show()

    # clear
    for i in range(n):
        np[i] = (255, 255, 255)
    np.write()


while True:
    twinkle(pixels)

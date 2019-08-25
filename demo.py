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


# np is the neopixel class
def demo(np):
    n = np.n

    # cycle
    # for i in range(4 * n):
    #     for j in range(n):
    #         np[j] = (255, 255, 255)
    #     np[i % n] = (200, 255, 255)
    #     np.write()
    #     time.sleep(0.06)
    # bounce
    # for i in range(4 * n):
    #     for j in range(n):
    #         np[j] = (0, 0, 128)
    #     if (i // n) % 2 == 0:
    #         np[i % n] = (0, 0, 0)
    #     else:
    #         np[n - 1 - (i % n)] = (0, 0, 0)
    #     np.write()
    #     time.sleep(0.060)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, val, 255)
        np.write()

    # clear
    for i in range(n):
        np[i] = (255, 255, 255)
    np.write()


while True:
    demo(pixels)

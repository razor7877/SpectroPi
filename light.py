#!/home/razor7877/spectro/venv/bin/python
import board
import neopixel
import time

pixels = neopixel.NeoPixel(board.D12, 24)
pixels[0] = (255, 0, 0)

time.sleep(3)

#!/home/razor7877/spectro/venv/bin/python
import board
import neopixel
import time

print(dir(board))
pixels = neopixel.NeoPixel(board.D18, 16)

pixels[0] = (255, 255, 255)
pixels.show()
time.sleep(2)

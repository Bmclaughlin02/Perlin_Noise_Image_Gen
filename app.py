import png
from noise2d import noise2d
import random

width = 500
height = 500
img = []
P = list(range(0,256))
random.shuffle(P)

for y in range(height):
    row = ()
    for x in range(width):
        n = noise2d(x*.01, y*.01, P)
        n += 1.0
        n /= 2.0

        color = round(int(255*n), 0)

        row = row + (color, color, color)
    img.append(row)

with open('noise.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    w.write(f, img)

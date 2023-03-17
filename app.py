import png
from noise2d import noise2d
import random

width = 256
height = 256
img = []
P = list(range(0,256))
random.shuffle(P)

for y in range(height):
    row = ()

    for x in range(width):
        n = 0.1
        a = 1.5
        f = .005

        for o in range(4):
            v = a*noise2d(x*f, y*f, P, 1)
            n += v
            a *= 0.5
            f *= 2

        n += 1.0
        n *= 0.5

        color = round(int(255*n), 0)
        if (color > 255):
            color = 255
        elif (color < 0):
            color = 0

        if (color >= 100):
            row = row + (0, 0, color)
        else:
            row = row + (0, color, 0)
    img.append(row)

with open('noise.png', 'wb') as f:
    w = png.Writer(width, height, greyscale=False)
    try:
        w.write(f, img)
    except:
        print(img)

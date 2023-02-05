from math import floor

class vec2:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

def dotp(self: vec2, other: vec2):
        return self.x*other.x + self.y*other.y

def getConstantVector(v):
    h = v & 3
    if(h == 0):
        a = vec2(1.0, 1.0)
    elif(h == 1):
        a = vec2(-1.0, 1.0)
    elif(h == 2):
        a = vec2(-1.0, -1.0)
    else:
        a = vec2(1.0, -1.0)

    return a

def smoothStepFade(t):
    return t*t*t*((t*6.0 - 15.0)*t + 10)

def lerp(t, a1, a2):
    return a1 + t*(a2-a1)

def fetch(I, r):
    I += 1
    if (r > 1):
        I %= r
    return I

def noise2d(x, y, P, r):
    if (r > 1):
        x = x%r
        y = y%r

    X = floor(x) & 255
    Y = floor(y) & 255

    xf = x-floor(x)
    yf = y-floor(y)

    topRight = vec2(xf-1.0, yf-1.0)
    topLeft = vec2(xf, yf-1.0)
    bottomRight = vec2(xf-1.0, yf)
    bottomLeft = vec2(xf, yf)

    valueTopRight = P[P[fetch(X, r)]+fetch(Y, r)]
    valueTopLeft = P[P[X]+fetch(Y, r)]
    valueBottomRight = P[P[fetch(X, r)]+Y]
    valueBottomLeft = P[P[X]+Y]

    dotTopRight = dotp(topRight, getConstantVector(valueTopRight))
    dotTopLeft = dotp(topLeft, getConstantVector(valueTopLeft))
    dotBottomRight = dotp(bottomRight, getConstantVector(valueBottomRight))
    dotBottomLeft = dotp(bottomLeft, getConstantVector(valueBottomLeft))

    u = smoothStepFade(xf)
    v = smoothStepFade(yf)

    return lerp(u, lerp(v, dotBottomLeft, dotTopLeft), lerp(v, dotBottomRight, dotTopRight))
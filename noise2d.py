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

    top_right = vec2(xf-1.0, yf-1.0)
    top_left = vec2(xf, yf-1.0)
    bottom_right = vec2(xf-1.0, yf)
    bottom_left = vec2(xf, yf)

    value_top_right = P[P[fetch(X, r)]+fetch(Y, r)]
    value_top_left = P[P[X]+fetch(Y, r)]
    value_bottom_right = P[P[fetch(X, r)]+Y]
    value_bottom_left = P[P[X]+Y]

    dot_top_right = dotp(top_right, getConstantVector(value_top_right))
    dot_top_left = dotp(top_left, getConstantVector(value_top_left))
    dot_bottom_right = dotp(bottom_right, getConstantVector(value_bottom_right))
    dot_bottom_left = dotp(bottom_left, getConstantVector(value_bottom_left))

    u = smoothStepFade(xf)
    v = smoothStepFade(yf)

    return lerp(u, lerp(v, dot_bottom_left, dot_top_left), lerp(v, dot_bottom_right, dot_top_right))

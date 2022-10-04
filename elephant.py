import time

from sense_hat import SenseHat

s = SenseHat()
s.low_light = True

o = (0,0,0)
c2 = (255,255,255)
c1 = (220,220,220)
green = (0, 255, 0)
red = (255, 0, 0)
nothing = (0,0,0)

elephant = [
    o, o, c1, c1, o, o, o, o,
    o, c1, c1, c1, c1, c1, c1, o,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, c1, c1, c1, c1, c1, c1, c1,
    c1, c2, c2, c1, c1, c1, c1, c1,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, o, c1, c1, o, c1, c1, o,
    c1, o, c2, c1, o, c2, c1, o,
]


s.clear()
s.set_pixels(elephant)
input()
s.clear()
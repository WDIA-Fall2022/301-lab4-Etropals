from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)
grey = (220,220,220)


def getUserChoice():
    print("What do you want to display (0. to exit): ")
    print("1. Logo")
    print("2. Plus Sign")
    print("3. Equals sign")
    print("4. Rasberry")
    print("5. Heart")
    print("6. Elephant")
    print("0. Exit")


def trinket_logo(O=nothing, Y=yellow, B=blue, G=green):
    
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo(G=green, R=red, O=nothing):

    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus(W=white, O=nothing):
   
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals(W=white, O=nothing):
   
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart(P=pink, O=nothing):

    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def elephant(o=nothing, c1=grey, c2=white):

    logo = [
    o, o, c1, c1, o, o, o, o,
    o, c1, c1, c1, c1, c1, c1, o,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, c1, c1, c1, c1, c1, c1, c1,
    c1, c2, c2, c1, c1, c1, c1, c1,
    c1, o, c1, c1, c1, c1, c1, c1,
    c1, o, c1, c1, o, c1, c1, o,
    c1, o, c2, c1, o, c2, c1, o,
    ]
    return logo

getUserChoice()                       
while True:
    try:
        userchoice = int(input())
        if userchoice == 1:
            s.set_pixels(trinket_logo())

        elif userchoice == 2:
            s.set_pixels(plus())

        elif userchoice == 3:
            s.set_pixels(equals())

        elif userchoice == 4:
            s.set_pixels(raspi_logo())

        elif userchoice == 5:
            s.set_pixels(heart())

        elif userchoice == 6:
            s.set_pixels(elephant())

        elif userchoice == 0:
            print("Come again")
            break
        if userchoice >6 or userchoice <0:
            print("Number must be between 0 and 6")
    except ValueError:
        print("Input must be a number")
            
            
        

images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]
count = 0
while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
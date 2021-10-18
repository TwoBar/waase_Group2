from sense_hat import SenseHat
blue = (0, 0, 255)
red = (100, 0, 70)
green = (0, 150, 100)
black = (0, 0, 0)
b = blue
r = red
g = green
n = black
sense = SenseHat()

def down():
    creeper_pixels = [
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        b, b, b, b, b, b, b, b,
                        b, b, b, b, b, b, b, b,
                        b, b, b, b, b, b, b, b
                    ]
    sense.set_pixels(creeper_pixels)
def up():
    creeper_pixels = [
                    b, b, b, b, b, b, b, b,
                    b, b, b, b, b, b, b, b,
                    b, b, b, b, b, b, b, b,
                    n, n, n, n, n, n, n, n,
                    n, n, n, n, n, n, n, n,
                    n, n, n, n, n, n, n, n,
                    n, n, n, n, n, n, n, n,
                    n, n, n, n, n, n, n, n
                ]                
    sense.set_pixels(creeper_pixels)
def left():
    creeper_pixels = [
                    b, b, b, n, n, n, n, n,
                    b, b, b, n, n, n, n, n,
                    b, b, b, n, n, n, n, n,
                    b, b, b, n, n, n, n, n,
                    b, b, b, n, n, n, n, n,
                    b, b, b, n, n, n, n, n,
                    b, b, b, n, n, n, n, n,
                    b, b, b, n, n, n, n, n
                ]
    sense.set_pixels(creeper_pixels)
def right():
    creeper_pixels = [
                    n, n, n, n, n, b, b, b,
                    n, n, n, n, n, b, b, b,
                    n, n, n, n, n, b, b, b,
                    n, n, n, n, n, b, b, b,
                    n, n, n, n, n, b, b, b,
                    n, n, n, n, n, b, b, b,
                    n, n, n, n, n, b, b, b,
                    n, n, n, n, n, b, b, b
                ]                
    sense.set_pixels(creeper_pixels)
    

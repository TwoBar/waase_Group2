# this library define hou datatype 2 & 3 are displayed by the device's screen


from sense_hat import SenseHat


# define rgb for colours

blue = (0, 0, 255)
red = (100, 0, 70)
green = (0, 150, 100)
black = (0, 0, 0)
yellow = (180, 180, 100)
b = blue
r = red
g = green
n = black
y = yellow
sense = SenseHat()

# define the array of pixel for the direction functions
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





# define the array of pixel for the watch functions
def watch(hh,mm,ss,tt): # args hours minutes seconds and last unit
    if tt <= 8 and tt != 0:
        t1 = y
    else:
        t1 = n
    if tt >= 2 or tt == 0:
        t2 = y
    else:
        t2 = n
    if tt >= 3:
        t3 = y
    else:
        t3 = n
    if tt >= 4:
        t4 = y
    else:
        t4 = n
    if tt >= 5:
        t5 = y
    else:
        t5 = n
    if tt >= 6:
        t6 = y
    else:
        t6 = n
    if tt >= 7:
        t7 = y
    else:
        t7 = n
    if tt >= 8:
        t8 = y
    else:
        t8 = n
    if ss >= 3:
        s1 = g
    else:
        s1 = n
    if ss >= 7:
        s2 = g
    else:
        s2 = n
    if ss >= 10:
        s3 = g
    else:
        s3 = n
    if ss >= 14:
        s4 = g
    else:
        s4 = n
    if ss >= 17:
        s5 = g
    else:
        s5 = n
    if ss >= 21:
        s6 = g
    else:
        s6 = n
    if ss >= 24:
        s7 = g
    else:
        s7 = n
    if ss >= 27:
        s8 = g
    else:
        s8 = n
    if ss >= 30:
        s9 = g
    else:
        s9 = n
    if ss >= 34:
        s10 = g
    else:
        s10 = n
    if ss >= 37:
        s11 = g
    else:
        s11 = n
    if ss >= 41:
        s12 = g
    else:
        s12 = n
    if ss >= 45:
        s13 = g
    else:
        s13 = n
    if ss >= 49:
        s14 = g
    else:
        s14 = n
    if ss >= 53:
        s15 = g
    else:
        s15 = n
    if ss >= 57:
        s16 = g
    else:
        s16 = n
    if mm >= 3:
        m1 = b
    else:
        m1 = n
    if mm >= 7:
        m2 = b
    else:
        m2 = n
    if mm >= 10:
        m3 = b
    else:
        m3 = n
    if mm >= 14:
        m4 = b
    else:
        m4 = n
    if mm >= 17:
        m5 = b
    else:
        m5 = n
    if mm >= 21:
        m6 = b
    else:
        m6 = n
    if mm >= 24:
        m7 = b
    else:
        m7 = n
    if mm >= 27:
        m8 = b
    else:
        m8 = n
    if mm >= 30:
        m9 = b
    else:
        m9 = n
    if mm >= 34:
        m10 = b
    else:
        m10 = n
    if mm >= 37:
        m11 = b
    else:
        m11 = n
    if mm >= 41:
        m12 = b
    else:
        m12 = n
    if mm >= 45:
        m13 = b
    else:
        m13 = n
    if mm >= 49:
        m14 = b
    else:
        m14 = n
    if mm >= 53:
        m15 = b
    else:
        m15 = n
    if mm >= 57:
        m16 = b
    else:
        m16 = n
    if hh >= 1:
        h1 = r
    else:
        h1 = n
    if hh >= 2:
        h2 = r
    else:
        h2 = n
    if hh >= 3:
        h3 = r
    else:
        h3 = n
    if hh >= 4:
        h4 = r
    else:
        h4 = n
    if hh >= 5:
        h5 = r
    else:
        h5 = n
    if hh >= 6:
        h6 = r
    else:
        h6 = n
    if hh >= 7:
        h7 = r
    else:
        h7 = n
    if hh >= 8:
        h8 = r
    else:
        h8 = n
    if hh >= 9:
        h9 = r
    else:
        h9 = n
    if hh >= 10:
        h10 = r
    else:
        h10 = n
    if hh >= 11:
        h11 = r
    else:
        h11 = n
    if hh >= 12:
        h12 = r
    else:
        h12 = n
    if hh >= 13:
        h13 = r
    else:
        h13 = n
    if hh >= 14:
        h14 = r
    else:
        h14 = n
    if hh >= 15:
        h15 = r
    else:
        h15 = n
    if hh >= 16:
        h16 = r
    else:
        h16 = n
    if hh >= 17:
        h17 = r
    else:
        h17 = n
    if hh >= 18:
        h18 = r
    else:
        h18 = n
    if hh >= 19:
        h19 = r
    else:
        h19 = n
    if hh >= 20:
        h20 = r
    else:
        h20 = n
    if hh >= 21:
        h21 = r
    else:
        h21 = n
    if hh >= 22:
        h22 = r
    else:
        h22 = n
    if hh >= 23:
        h23 = r
    else:
        h23 = n
    if hh >= 24:
        h24 = r
    else:
        h24 = n
    watchscreen(h24, h23, h22, m16, m15, s16, s15, t8,
                    h21, h20, h19, m14, m13, s14, s13, t7,
                    h18, h17, h16, m12, m11, s12, s11, t6,
                    h15, h14, h13, m10, m9, s10, s9, t5,
                    h12, h11, h10, m8, m7, s8, s7, t4,
                    h9, h8, h7, m6, m5, s6, s5, t3,
                    h6, h5, h4, m4, m3, s4, s3, t2,
                    h3, h2, h1, m2, m1, s2, s1, t1)
def watchscreen(h24, h23, h22, m16, m15, s16, s15, t8,
                    h21, h20, h19, m14, m13, s14, s13, t7,
                    h18, h17, h16, m12, m11, s12, s11, t6,
                    h15, h14, h13, m10, m9, s10, s9, t5,
                    h12, h11, h10, m8, m7, s8, s7, t4,
                    h9, h8, h7, m6, m5, s6, s5, t3,
                    h6, h5, h4, m4, m3, s4, s3, t2,
                    h3, h2, h1, m2, m1, s2, s1, t1):
    creeper_pixels = [
                    h24, h23, h22, m16, m15, s16, s15, t8,
                    h21, h20, h19, m14, m13, s14, s13, t7,
                    h18, h17, h16, m12, m11, s12, s11, t6,
                    h15, h14, h13, m10, m9, s10, s9, t5,
                    h12, h11, h10, m8, m7, s8, s7, t4,
                    h9, h8, h7, m6, m5, s6, s5, t3,
                    h6, h5, h4, m4, m3, s4, s3, t2,
                    h3, h2, h1, m2, m1, s2, s1, t1
                ]  # plot the watch display
    sense.set_pixels(creeper_pixels)
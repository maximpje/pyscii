# sets the height and width of the frame
def setup(h, w):
    global HEIGHT
    global WIDTH
    HEIGHT = h
    WIDTH = w


# turns i,j pair into x y coordinate system with correction for font dimensions
def to_xy(i, j):
    x = (j - ((WIDTH+1)/2)) / (35/45)
    y = -(i - HEIGHT) - ((HEIGHT+1)/2)
    return (x, y)


# generates and returns 1 frame as a string that can be printed
def generate_frame(t):
    frame = ""
    for i in range(0, HEIGHT):
        line = ""
        for j in range(0, WIDTH):
            (x, y) = to_xy(i, j)
            if round(pow(x, 2)) + round(pow(y, 2)) < t:
                line = line + "###"
            else:
                line = line + "   "
        frame = frame + line + "\n"
    return frame

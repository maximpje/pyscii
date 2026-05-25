import math


points = []


# sets the height and width of the frame
def setup(h, w):
    global HEIGHT
    global WIDTH
    HEIGHT = h
    WIDTH = w


# turns i,j pair into x y coordinate system with correction for font dimensions
def to_xy(i, j):
    x = i - (WIDTH/2)
    y = (HEIGHT/2) - j
    return (x, y)


# generates and returns 1 frame as a string that can be printed
def generate_frame(t):
    print(points)
    frame = ""
    for i in range(0, HEIGHT):
        line = ""
        for j in range(0, WIDTH):
            (x, y) = to_xy(i, j)
            if round(pow(x, 2)) + round(pow(y, 2)) < 256:
                line = line + f"\033[48;2;{round(127*math.sin(t/(2*math.pi))+127)};{round(127*math.sin((t/(2*math.pi))+3.3)+127)};{round(127*math.sin((t/2*math.pi)+6.6)+127)}m  "
            else:
                line = line + "\033[48;2;0;0;0m  "
        frame = frame + line + "\n"
    return frame


def point(x, y):
    points.append((x, y))

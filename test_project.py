import renderer
import os
import time
import math

renderer.setup(40, 40)

t = 0

while True:
    # os.system("clear")
    print(renderer.generate_frame(t))
    t += 0.2
    if t > 30:
        t = 0
    time.sleep(0.5)
    print(f"[48;2;{round(127*math.sin(t/(2*math.pi))+127)};{round(127*math.sin((t/(2*math.pi))+3.3)+127)};{round(127*math.sin((t/2*math.pi)+6.6)+127)}  ")

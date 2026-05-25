import renderer
import os
import time

renderer.setup(35, 35)

timer = 0
while True:
    os.system("clear")
    print(renderer.generate_frame(pow(timer, 2)))
    print(timer)
    timer += 1
    time.sleep(0.2)
    if timer > 30:
        timer = 0

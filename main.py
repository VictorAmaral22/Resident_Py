from graphics import *
from render_functions import renderImage
from datetime import datetime
winW = 1920
winH = 1080

win = GraphWin("Gym Rats", winW, winH)
win.setBackground("#000")

exit = False
loggedUser = False

page = "initial"

while not exit:
    if win.closed:
        break

    if page == "exit":
        exit = True

    if page == "initial":
        background = renderImage(win, winW/2, winH/2, "corridor.png")
        position = 150
        leon = renderImage(win, position, (winH/2)+200, "leon-sprite-right.png")
        leavePage = False
        direction = "right"
        step = 10
        lastTime = 1

        while not leavePage:
            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")

            keyPress = win.checkKey()
            if not keyPress:
                if lastTime != str(int(current_time[-1])%2):
                    if int(current_time[-1])%2 == 1:
                        leon[2]()
                        leon = renderImage(win, position, (winH/2)+200, "./sprites/leon/idle/leon-sprite-idle-"+direction+"-1.png")
                        lastTime = str(int(current_time[-1])%2)
                    else:
                        leon[2]()
                        leon = renderImage(win, position, (winH/2)+200, "./sprites/leon/idle/leon-sprite-idle-"+direction+"-2.png")
                        lastTime = str(int(current_time[-1])%2)

            if keyPress == "d" or keyPress == "a":
                step = 10
            if keyPress == "D" or keyPress == "A":
                step = 30

            if keyPress == "d" or keyPress == "D":
                position += step
                if direction == "right":
                    leon[0].move(step, 0)
                else:
                    direction = "right"
                    leon[2]()
                    leon = renderImage(win, position, (winH/2)+200, "leon-sprite-right.png")

            if keyPress == "a" or keyPress == "A":
                position -= step
                if direction == "left":
                    leon[0].move(-step, 0)
                else:
                    direction = "left"
                    leon[2]()
                    leon = renderImage(win, position, (winH/2)+200, "leon-sprite-left.png")

from graphics import *
from render_functions import renderImage
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
        print("Hello")
        background = renderImage(win, winW/2, winH/2, "corridor.png")
        position = 150
        leon = renderImage(win, position, (winH/2)+200, "leon-sprite-right.png")
        leavePage = False
        direction = "right"
        step = 30
        while not leavePage:
            keyPress = win.checkKey()

            if keyPress == "d":
                position += step
                if direction == "right":
                    leon[0].move(step, 0)
                else:
                    direction = "right"
                    leon[2]()
                    leon = renderImage(win, position, (winH/2)+200, "leon-sprite-right.png")

            if keyPress == "a":
                position -= step
                if direction == "left":
                    leon[0].move(-step, 0)
                else:
                    direction = "left"
                    leon[2]()
                    leon = renderImage(win, position, (winH/2)+200, "leon-sprite-left.png")

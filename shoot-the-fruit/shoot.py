# SHOOT THE FRUIT GAME
# For people practicing on using the mouse

import pgzrun
from random import randint


# Actors
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

points = 0 # Number of points


def draw():
    """Prepares the screen and draws the actors"""

    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()


def place_fruits():
    """Positions the actors"""

    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)


def on_mouse_down(pos):
    """Mouse click event"""

    global points

    if apple.collidepoint(pos) or orange.collidepoint(pos) or pineapple.collidepoint(pos):
        points = points + 1
        print("Good shot! Points: " + str(points))
        place_fruits()
    else:
        points = points - 2
        print("You missed! Points: " + str(points))
        place_fruits()


# Initial placement of actors
place_fruits()

pgzrun.go()
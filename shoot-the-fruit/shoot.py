# SHOOT THE FRUIT GAME
# For people practicing on using the mouse

import pgzrun
from random import randint


# Actors
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
bomb = Actor("bomb")

points = 0 # Number of points


def draw():
    """Prepares the screen and draws the actors"""

    screen.clear()
    screen.fill((255, 255, 255))
    apple.draw()
    orange.draw()
    pineapple.draw()
    bomb.draw()


def place_actors():
    """Positions the actors"""

    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)
    bomb.x = randint(10, 800)
    bomb.y = randint(10, 600)


def on_mouse_down(pos):
    """Mouse click event"""

    global points

    if apple.collidepoint(pos) or orange.collidepoint(pos) or pineapple.collidepoint(pos):
        points = points + 1
        print("Good shot! Points: " + str(points))
        place_actors()
    elif bomb.collidepoint(pos):
        points = points - 10
        print("Kaboom! Points: " + str(points))
        place_actors()
    else:
        points = points - 2
        print("You missed! Points: " + str(points))
        place_actors()


# Initial placement of actors
place_actors()

pgzrun.go()
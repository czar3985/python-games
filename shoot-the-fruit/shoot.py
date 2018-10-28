import pgzrun
from random import randint

apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()

def place_fruits():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)
    pineapple.x = randint(10, 800)
    pineapple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos) or orange.collidepoint(pos) or pineapple.collidepoint(pos):
        print("Good shot!")
        place_fruits()
    else:
        print("You missed!")
        quit()

place_fruits()

pgzrun.go()
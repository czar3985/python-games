# COIN COLLECTOR GAME

import pgzrun
from random import randint


# Game screen size 400px x 400px
WIDTH = 400
HEIGHT = 400

# Game variables
score = 0   # Initializes score
game_over = False

# Actors
fox = Actor("fox")
coin = Actor("coin")

# Position actors
fox.pos = 100, 100
coin.pos = 200, 200


def draw():
    """Draw function of the game"""

    screen.fill("green")

    # Draw actors
    fox.draw()
    coin.draw()

    # Print the score at the top left corner of the screen
    screen.draw.text("Score: " + str(score), color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)


def place_coin():
    """Positions the coin"""

    # Prevent the coin from touching the sides of the screen
    coin.x = randint(20, WIDTH - 20)
    coin.y = randint(20, HEIGHT - 20)
    return


def time_up():
    """Set game over"""

    global game_over

    game_over = True
    return


def update():
    """Runs 60 times a second during the course of the game"""

    global score

    # Move the fox's position based on arrow key presses
    if keyboard.left:
        fox.x = fox.x - 2
    elif keyboard.right:
        fox.x = fox.x + 2
    elif keyboard.up:
        fox.y = fox.y - 2
    elif keyboard.down:
        fox.y = fox.y + 2

    # Increment score when fox touches the coin
    if (fox.colliderect(coin)):
        score = score + 10
        place_coin()

    return


clock.schedule(time_up, 7.0) # Set the game to run for 7 seconds
place_coin()

pgzrun.go()
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import(
    SCREEN_HEIGHT, 
    SCREEN_WIDTH,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS
    )

def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        screen.fill(color="black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
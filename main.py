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

from player import Player

def main():

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #group setup
    updatables = []
    drawables = []
    
    player = Player(x = SCREEN_WIDTH / 2 , y = SCREEN_HEIGHT / 2)
    updatables.append(player)
    drawables.append(player)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(color="black")

        for obj in updatables:
            obj.update(dt)

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()
        dt += clock.tick(60) / 1000

if __name__ == "__main__":
    main()
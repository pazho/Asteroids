import pygame
from constants import * 
from player import *
from asteroidfield import *
from asteroid import *
import sys
import logger 
from logger import log_event


def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0 
    print("Starting Asteroids!")
    print("Screen width:" ,SCREEN_WIDTH)
    print("Screen height:" ,SCREEN_HEIGHT)

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = (updateable, )
    Asteroid.containers = (asteroids, updateable, drawable)
    Player.containers = (updateable, drawable)
    asteroid_field = AsteroidField()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        pygame.Surface.fill(screen,"black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for thing in updateable:
            thing.update(dt)
        for asteroid in asteroids:
            if player.collides(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for thing in drawable:
            thing.draw(screen)


        dt = clock.tick(60) / 1000
        updateable.update(dt)

        player.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()

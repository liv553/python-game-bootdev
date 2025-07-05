# main.py

import pygame
from constants import *
from player import Player
from asteroidfield import *
from asteroid import *
from circleshape import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    clock = pygame.time.Clock()
    
    dt = 0

    asteroids = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = updatables, drawables
    Asteroid.containers = asteroids, updatables, drawables
    AsteroidField.containers = (updatables,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatables.update(dt)

        for asteroid in asteroids:
            if player.is_there_collision(asteroid):
                print("Game over!")
                running = False
                break
        
        if not running:
            break

        screen.fill("black")

        for sprite in drawables:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()

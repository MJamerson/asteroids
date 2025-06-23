import pygame
import sys
from player import *
from asteroid import *
from constants import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)

    group_asteroids = pygame.sprite.Group()
    Asteroid.containers = (group_asteroids, group_updatable, group_drawable)
    AsteroidField.containers = (group_updatable)

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    
    group_shots = pygame.sprite.Group()
    Shot.containers = (group_shots, group_drawable, group_updatable)

    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return
        group_updatable.update(dt)
        for asteroid in group_asteroids:
            for shot in group_shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        for asteroid in group_asteroids:
            if player_1.check_collision(asteroid):
                print("Game over!")
                sys.exit(1)

        screen.fill("black")
        for thing in group_drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
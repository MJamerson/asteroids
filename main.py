import pygame
from player import *
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    Player.containers = (group_updatable, group_drawable)

    player_1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        group_updatable.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              return
        screen.fill("black")
        for thing in group_drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
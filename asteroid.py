import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(ASTEROID_SPLIT_MIN_ANGLE, ASTEROID_SPLIT_MAX_ANGLE)
        split_1_angle = self.velocity.rotate(angle)
        split_2_angle = self.velocity.rotate(angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        split_1 = Asteroid(self.position.x, self.position.y, new_radius)
        split_2 = Asteroid(self.position.x, self.position.y, new_radius)
        split_1.velocity = split_1_angle * 1.2
        split_2.velocity = split_2_angle * 1.2

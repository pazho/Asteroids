import pygame
import random

from logger import log_event
from player import *
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt 


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            old_radius = self.radius
            new_radius = old_radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)*1.2
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)*1.2
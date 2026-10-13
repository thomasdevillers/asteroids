from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x:float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
        self.icon = pygame.image.load("asteroid.png")

    def draw(self, screen):
        scaled_icon = pygame.transform.scale(self.icon, (self.radius*2, self.radius*2))
        rect = scaled_icon.get_rect(center=self.position)
        screen.blit(scaled_icon, rect)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        angle_vect1 = self.velocity.rotate(angle)
        angle_vect2 = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = 1.2 * angle_vect1
        asteroid2.velocity = 1.2 * angle_vect2

        
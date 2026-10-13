from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH

class Shot(CircleShape):
    
    def __init__(self, x, y, radius, rotation, piercing):
        super().__init__(x,y, radius)
        self.rotation = rotation
        self.icon = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("bullet.png"), (30,30)), 90)
        self.piercing = piercing
        self.health = 100

    def draw(self, screen):
        rotated_bullet = pygame.transform.rotate(self.icon, -self.rotation)
        rect = rotated_bullet.get_rect(center=self.position)
        screen.blit(rotated_bullet, rect)

    def update(self, dt):
        self.position += self.velocity * dt
        
        
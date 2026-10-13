import pygame
from constants import SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_SHOOT_SPEED
from shot import Shot

class Weapon():
    def __init__(self, name, cooldown=0.3, piercing=False, size=SHOT_RADIUS, speed=PLAYER_SHOOT_SPEED, num_guns=1):
        self.name = name
        self.cooldown = cooldown
        self.piercing = piercing
        self.size = size
        self.speed = speed
        self.num_guns = num_guns
        self.cooldown_remaining = 0
        self.shots_in_round = num_guns

    def shoot(self, position, rotation, piercing):
        if self.shots_in_round == 0:
            if self.cooldown_remaining > 0:
                return
            self.cooldown_remaining = self.cooldown
            self.shots_in_round = self.num_guns

        shot = Shot(position.x, position.y, self.size, rotation, piercing)
        vect = pygame.Vector2(0,-1)
        vect = vect.rotate(rotation)
        vect = vect * self.speed
        shot.velocity = vect
        self.shots_in_round -= 1

    def update(self, dt):
        self.cooldown_remaining = max(0, self.cooldown_remaining-dt)

    def fire(self, position, rotation):
        # 0, 1, 2, 3 -> [0, 5, -5, 10, -10, 15, -15]
        angles = []

        for i in range(self.num_guns):
            angle = ((i + 1) // 2) * 5

            if i % 2 == 0:
                angle = -angle

            angles.append(angle)

        for angle in angles:
            self.shoot(position, rotation + angle, self.piercing)

    


from asteroidfield import SHOT_RADIUS
import pygame
import random

from circleshape import CircleShape
from weapon import Weapon
from constants import LINE_WIDTH, PLAYER_RADIUS, PLAYER_TURN_SPEED, INITIAL_PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_ACCELERATION, SCREEN_HEIGHT, SCREEN_WIDTH


class Player(CircleShape):

    starter = Weapon(name="Starter Gun")
    triple_shot = Weapon(name="Triple Shot", num_guns=3)
    rapid_shot = Weapon(name="Rapid Shot", cooldown=0.1)
    pierce_gun = Weapon(name="Pierce Gun", piercing=True)
    speed_shot = Weapon(name="Speed Shot", speed=1000)

    weapons = [starter, triple_shot, rapid_shot, pierce_gun, speed_shot]

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0
        self.score = 0
        self.lives = 3
        self.speed = INITIAL_PLAYER_SPEED
        self.icon = pygame.transform.smoothscale(pygame.image.load("rocket.webp"), (100,100))
        self.weapon_index = 4
        self.weapon = Player.weapons[self.weapon_index % 5]

    def draw(self, screen):
        rotated_icon = pygame.transform.rotate(self.icon, -self.rotation)
        rect = rotated_icon.get_rect(center=self.position)
        screen.blit(rotated_icon, rect)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0,-1)
        rotated_vector = unit_vector.rotate(self.rotation)
        self.speed = self.speed * PLAYER_ACCELERATION
        rotated_with_speed_vector = rotated_vector * self.speed * dt
        self.position += rotated_with_speed_vector

        # Wrapping around if player moves off the screen
        if self.position.x >= SCREEN_WIDTH:
            self.position.x = 1
        if self.position.y >= SCREEN_HEIGHT:
            self.position.y = 1
        if self.position.x <= 0:
            self.position.x = SCREEN_WIDTH
        if self.position.y <= 0:
            self.position.y = SCREEN_HEIGHT


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()
        self.weapon.update(dt)

        if not keys[pygame.K_w] and not keys[pygame.K_s]:
            self.speed = INITIAL_PLAYER_SPEED

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()


        self.cooldown -= dt

    def shoot(self):
        self.weapon.fire(self.position, self.rotation)

    def update_score(self, amount):
        self.score += amount

    def use_life(self):
        if self.lives == 1:
            raise Exception("No more lives.")
        self.lives -= 1

    def change_weapon(self):
        cur_index = Player.weapons.index(self.weapon)
        print(f"Old index: {cur_index}")
        new_index = cur_index
        while new_index == cur_index:
            new_index = int(random.uniform(0, 5))
        print(f"New index: {new_index}")
        self.weapon = Player.weapons[new_index]
            
    
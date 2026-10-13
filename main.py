import asteroidfield
from asteroid import Asteroid
import pygame
import sys
import time

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import Explosion

white = (255,255,255)


def main():

    # Game settings and config
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    bg = pygame.image.load("bg.png")


    # Object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Assigning object types to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (updatable, drawable)

    # Long lived objects
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # Players score
    font = pygame.font.SysFont(None, 30)
    score_label = font.render(f"Score: {player.score}", True, white)
    screen.blit(score_label, (20,100))

    # Current Weapon
    weapon_label = font.render(f"Selected Weapon: {player.weapon.name}", True, white)
    screen.blit(weapon_label, (20, 150))

    # Players lives as hearts
    heart = pygame.transform.smoothscale(pygame.image.load("heart.png").convert_alpha(), (50,50))
    heart_pos_x = 20
    heart_pos_y = 40

    # State variables for the game
    clock = pygame.time.Clock()
    dt = 0.0
    game_state = "playing"
    end_start_time = 0
    collide_time = 0
    prev_collide_time = 0

    # Main game loop
    while True:
        log_state()

        # Checking if user clicked the exit button
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player.change_weapon()
                    weapon_label = font.render(f"Selected Weapon: {player.weapon.name}", True, white)

                    print("Changing weapon")

        # User is currently alive and playing
        if game_state == "playing":
            screen.blit(bg, (0,0))

            # Updating objects on the screen.
            for dw in drawable:
                dw.draw(screen)
            updatable.update(dt)

            # Checking if player collided with asteroid
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    try:
                        # Cooldown between losing lives of 3 seconds
                        collide_time = pygame.time.get_ticks()
                        if collide_time - prev_collide_time <= 3000:
                            continue
                        else:
                            prev_collide_time = collide_time
                            player.use_life()
                            explosion = Explosion(asteroid.position.x, asteroid.position.y)
                            asteroid.kill()
                    except Exception:
                        game_state = "not_playing"
                        end_start_time = pygame.time.get_ticks()
                
                # Checking if shot collided with asteroid
                for shot in shots:
                    if shot.collides_with(asteroid):
                        log_event("asteroid_shot")
                        player.update_score(1)
                        score_label = font.render(f"Score: {player.score}", 1, white)
                        screen.blit(score_label, (20, 100))
                        if not shot.piercing:
                            shot.kill()
                        shot.health -= 50
                        explosion = Explosion(asteroid.position.x, asteroid.position.y)
                        asteroid.split()


            # Drawing lives and score to screen after updates occur
            screen.blit(score_label, (20,100))
            screen.blit(weapon_label, (20, 150))
            for i in range(player.lives):
                screen.blit(heart, (heart_pos_x+(i*60), heart_pos_y))

        # Player collided with asteroid - game is over
        elif game_state == "not_playing":
            screen.fill("green")
            score_label = font.render(f"Game Over! Score: {player.score}", True, (255,255,255))
            screen.blit(score_label, (SCREEN_WIDTH/2-100, SCREEN_HEIGHT/2))
            elapsed = pygame.time.get_ticks() - end_start_time
            if elapsed >= 5000:
                sys.exit()

        # Refresh screen to re-render changes
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

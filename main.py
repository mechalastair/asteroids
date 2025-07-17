# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from circleshape import *
from player import *
from asteroid import *
from shot import *
from asteroidfield import *
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    font = pygame.font.SysFont(None, 36)

    #Groups
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = updateables
    Shot.containers = (shots, updateables, drawables)

    # Make clock
    clock = pygame.time.Clock()
    dt = 0 # Delta time

    # Start scoring
    score = 0

    # Make GUI
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()


    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        score_display = font.render(f"Score: {score}", True, "yellow")
        screen.blit(score_display, (10, 10))  # Top-left corner at x=10, y=10

        # Manage groups
        updateables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                print(f"Final score: {score}")
                exit()
            for shot in shots:
                if shot.collision_check(asteroid):
                    score += 100
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()

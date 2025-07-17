# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame, sys
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
        if score > 10000:
            score_color = "blue"
        else:
            score_color = "yellow"
        score_display = font.render(f"Score: {score}", True, score_color)
        screen.blit(score_display, (10, 10))  # Top-left corner at x=10, y=10

        # Manage groups
        updateables.update(dt)
        for drawable in drawables:
            drawable.draw(screen)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                #print("Game over!")
                #print(f"Final score: {score}")
                game_over(screen, score)
            for shot in shots:
                if shot.collision_check(asteroid):
                    score += 100
                    asteroid.split()
                    shot.kill()
        pygame.display.flip()
        dt = clock.tick(60)/1000

# Death screen
def game_over(screen, score):
    screen.fill("black")

    font_large = pygame.font.SysFont(None, 72)
    game_over_text = font_large.render("GAME OVER", True, "red")
    game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 - 40))

    font_small = pygame.font.SysFont(None, 36)
    score_text = font_small.render(f"FINAL SCORE: {score}", True, "yellow")
    score_rect = score_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 15))

    sub_text = font_small.render("Press any key to restart", True, "white")
    sub_rect = sub_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2 + 80))
    
    screen.blit(game_over_text, game_over_rect)
    screen.blit(score_text, score_rect)
    screen.blit(sub_text, sub_rect)
    pygame.display.flip()

    # Wait for any key press or window close
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()
            #elif event.type == pygame.KEYDOWN:
            #    waiting = False

if __name__ == "__main__":
    main()

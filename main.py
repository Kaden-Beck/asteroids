import pygame, sys
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    # Initialize game clock
    game_clock = pygame.time.Clock()
    dt = 0
    # Initialize Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Add common sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Instantiate Player
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Instantiate Asteroid
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidField = AsteroidField()

    # Instantiate Shots
    shots = pygame.sprite.Group()
    Shot.containers = (shots, drawable, updatable)
    
    # Game Loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Update state
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
            
        # Draw Game
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()      
       
        # Game Tick
        delta = game_clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()

import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    pygame.init()
    # Initialize game clock
    game_clock = pygame.time.Clock()
    dt = 0
    # Initialize Screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Instantiate Player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # Game Loop
    while True:
        # Log State
        log_state()
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Draw Game
        screen.fill("black")
        # Draw Player
        player.update(dt)
        player.draw(screen)
        # Flip Screen
        pygame.display.flip()
        # Game Tick
        delta = game_clock.tick(60)
        dt = delta / 1000



if __name__ == "__main__":
    main()

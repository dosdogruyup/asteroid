from player import Player
import pygame
import constants
from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {constants.SCREEN_WIDTH}\nScreen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    playa = Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    while True:
        log_state()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        playa.update(dt)
        playa.draw(screen)
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
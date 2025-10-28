from scripts.utils import SCREEN_SIZE, load_images
import pygame, sys
pygame.init()

SCREEN_WIDTH:int = SCREEN_SIZE[0]
SCREEN_LENGHT:int = SCREEN_SIZE[1]

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_LENGHT))
        self.clock = pygame.time.Clock()
        self.display = pygame.Surface((SCREEN_WIDTH / 2, SCREEN_LENGHT / 2))
        self.running = True

        # Movement for camera
        self.movement = [False, False, False, False]

        self.assets = {
            'wall': load_images('tiles/wall'),
            'floor': load_images('tiles/floor')
        }
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
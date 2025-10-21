import pygame, sys
from scripts.state import State
from scripts.entities import Player
pygame.init()

class GameWorld(State):
    def __init__(self, game):
        super().__init__(game)
        self.player_surf = pygame.Surface((25, 25))
        self.player_rect = self.player_surf.get_frect()
        self.player = Player(game, (20, 20), (25, 25), self.player_surf)

        self.movement = [False, False, False, False]

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.movement[0] = True
                if event.key == pygame.K_d:
                    self.movement[1] = True
                if event.key == pygame.K_w:
                    self.movement[2] = True
                if event.key == pygame.K_s:
                    self.movement[3] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.movement[0] = False
                if event.key == pygame.K_d:
                    self.movement[1] = False
                if event.key == pygame.K_w:
                    self.movement[2] = False
                if event.key == pygame.K_s:
                    self.movement[3] = False

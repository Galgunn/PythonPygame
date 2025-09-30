import pygame
from scripts.state import State
from scripts.utils import *

pygame.init()

class PauseMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.pause_surf = pygame.Surface((SCREEN_SIZE[0] / 3, SCREEN_SIZE[1] / 3))
        self.pause_rect = self.pause_surf.get_frect(center = DISPLAY_CENTER)

    def update(self):
        if self.game.state_interaction_options['left_click']['just_pressed']:
            self.prev_state.exit_state() # type: ignore error due to prev_state being None
            self.exit_state()
        if self.game.state_interaction_options['escape']['just_pressed']:
            self.exit_state()

    def render(self, surf):
        self.prev_state.render(surf) # type: ignore error due to prev_state being None
        self.pause_surf.fill('blue')
        surf.blit(self.pause_surf, self.pause_rect)
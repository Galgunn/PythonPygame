import pygame
from scripts.state import State
pygame.init()

class SettingMenu(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        if self.game.state_interaction_options['left_click']['just_pressed'] or self.game.state_interaction_options['escape']['just_pressed']:
            self.exit_state()
    
    def render(self, surf):
        surf.fill('yellow')

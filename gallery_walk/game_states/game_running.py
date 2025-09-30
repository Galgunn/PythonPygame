import pygame
from scripts.state import State
from game_states.pause_menu import PauseMenu
pygame.init()

class GameRunning(State):
    def __init__(self, game):
        super().__init__(game)

    def update(self):
        if self.game.state_interaction_options['escape']['just_pressed']:
            pause_menu_state = PauseMenu(self.game)
            pause_menu_state.enter_state()
    
    def render(self, surf):
        surf.fill('red')
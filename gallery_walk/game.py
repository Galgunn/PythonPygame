from game_states.menus.main_menu import MainMenu
from scripts.utils import *
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
        self.state_stack = []

        self.state_interaction_options = {
            'escape': {'just_pressed': False},
            'left_click': {'just_pressed': False},
        }

        self.assets = {
            'none': None
        }

        self.load_state()

    def run(self):
        while self.running:

            for key in self.state_interaction_options:
                self.state_interaction_options[key]['just_pressed'] = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.state_interaction_options['enter']['just_pressed'] = True
                    if event.key == pygame.K_ESCAPE:
                        self.state_interaction_options['escape']['just_pressed'] = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.state_interaction_options['left_click']['just_pressed'] = True

            self.update()
            self.render()

    def update(self):
        self.state_stack[-1].update()

    def render(self):
        self.state_stack[-1].render(self.display)
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
        pygame.display.flip()
        self.clock.tick(60)

    def load_state(self):
        self.game_state = MainMenu(self)
        self.state_stack.append(self.game_state)
    
    def reset_keys(self):
        pass

if __name__ == '__main__':
    Game().run()
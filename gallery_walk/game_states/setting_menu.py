import pygame
from scripts.state import State
from scripts.menu_options import MenuOptions

pygame.init()

class SettingMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.menu_options: list = ['Back']
        self.menu = MenuOptions(game, self.menu_options)

    def update(self):
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)
        self.menu.update(mpos)
        if self.menu.get_mouse_pressed('Back') or self.menu.get_key_pressed():
            self.exit_state()

    
    def render(self, surf):
        surf.fill('yellow')
        self.menu.render(surf)

import pygame
from scripts.state import State
from scripts.utils import FONT, DISPLAY_CENTER
from scripts.menu_options import MenuOptions

pygame.init()

class Credits(State):

    def __init__(self, game):
        super().__init__(game)
        self.font = FONT
        self.font_surf = self.font.render('Game by Name Pending', True, (0, 0, 0))
        self.font_rect = self.font_surf.get_rect(center=DISPLAY_CENTER)
        self.menu = MenuOptions(self.game, ['Back'], (DISPLAY_CENTER[0], self.font_rect.bottom + 10))

    def update(self):
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)
        self.menu.update(mpos)
        if self.menu.get_mouse_pressed('Back') or self.menu.get_key_pressed():
            self.exit_state()

    def render(self, surf):
        surf.fill('purple')
        surf.blit(self.font_surf, self.font_rect)
        self.menu.render(surf)
        
        

        
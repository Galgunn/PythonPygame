from scripts.state import State
from scripts.utils import *
import pygame

pygame.init()

class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.font = FONT
        self.center_display = (DISPLAY_SIZE[0] / 2, DISPLAY_SIZE[1] / 2)
        self.text_surf = self.font.render('yeah', True, 'black')
        self.selected_text_surf = self.font.render('yeah', True, 'white')
        self.text_rect = self.text_surf.get_frect(center= self.center_display)
        self.on_text_rect = False

    def update(self):

        self.on_text_rect = False

        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)

        if self.text_rect.collidepoint(mpos):
            self.on_text_rect = True

    def render(self, surf):
        surf.fill(('green'))
        if self.on_text_rect:
            surf.blit(self.selected_text_surf, (self.text_rect.x + 1, self.text_rect.y + 1))
        surf.blit(self.text_surf, (self.text_rect))

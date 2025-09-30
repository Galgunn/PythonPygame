from scripts.state import State
from scripts.utils import *
from game_states.game_running import GameRunning
from game_states.setting_menu import SettingMenu
import pygame

pygame.init()

class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.font = FONT
        self.center_display = DISPLAY_CENTER
        self.menu_text_options = ['Start', 'Settings', 'Credits', 'Exit']
        self.initialize_fonts()
        
    def initialize_fonts(self): # Initializes the font surfaces aswell as rect with their respective pos
        self.menu_fonts_surf = {}
        pos = self.center_display
        for option in self.menu_text_options:
            font_surf = self.font.render(option, True, 'black')
            font_highlight_surf = self.font.render(option, True, 'white')
            font_rect = font_surf.get_frect(center = pos)
            self.menu_fonts_surf[option] = {'text': font_surf, 'highlight': font_highlight_surf, 'rect': font_rect, 'on_font': False}
            pos = (pos[0], pos[1] + 25)

    def check_option_collision(self, mpos): # Check for collision with any of the font rects
        for option in self.menu_fonts_surf:
            self.menu_fonts_surf[option]['on_font'] = False
            if self.menu_fonts_surf[option]['rect'].collidepoint(mpos):
                self.menu_fonts_surf[option]['on_font'] = True          

    def update(self):
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)
        self.check_option_collision(mpos)
        if self.game.state_interaction_options['left_click']['just_pressed'] and self.menu_fonts_surf['Start']['on_font']:
            game_running_state = GameRunning(self.game)
            game_running_state.enter_state()
        if self.game.state_interaction_options['left_click']['just_pressed'] and self.menu_fonts_surf['Settings']['on_font']:
            settings_menu_state = SettingMenu(self.game)
            settings_menu_state.enter_state()

    def render(self, surf):
        surf.fill(('green'))
        for option in self.menu_fonts_surf:
            if self.menu_fonts_surf[option]['on_font']:
                surf.blit(self.menu_fonts_surf[option]['highlight'], (self.menu_fonts_surf[option]['rect'].x + 1, self.menu_fonts_surf[option]['rect'].y + 1))
            surf.blit(self.menu_fonts_surf[option]['text'], self.menu_fonts_surf[option]['rect'])
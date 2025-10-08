from scripts.state import State
from scripts.utils import *
from game_states.game_running import GameRunning
from game_states.setting_menu import SettingMenu
from scripts.menu_options import MenuOptions
import pygame

pygame.init()

class MainMenu(State):
    def __init__(self, game):
        super().__init__(game)
        self.menu_text_options = ['Start', 'Settings', 'Credits', 'Exit']
        self.font_options = MenuOptions(game, self.menu_text_options)
        self.font_dict = self.font_options.font_dict     

    def update(self):
        mpos = pygame.mouse.get_pos()
        mpos = (mpos[0] / 2, mpos[1] / 2)
        self.font_options.update(mpos)
        if self.font_options.get_mouse_pressed('Start'):
            game_running_state = GameRunning(self.game)
            game_running_state.enter_state()
        if self.font_options.get_mouse_pressed('Settings'):
            settings_menu_state = SettingMenu(self.game)
            settings_menu_state.enter_state()

    def render(self, surf):
        surf.fill(('green'))
        self.font_options.render(surf)
        
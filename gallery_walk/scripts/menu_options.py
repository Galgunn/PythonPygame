from scripts.utils import *
class MenuOptions():
    def __init__(self, game, text_options: list, pos: tuple=DISPLAY_CENTER) -> None:
        """
        Requires a list of strings that creates font objects of the stings

        Created to make menu options "buttons"
        """
        self.game = game
        self.text_options:list = text_options
        self.font:pygame.Font = FONT
        self.starting_pos = pos
        self.font_dict:dict = {}
        self.init_fonts()

    def init_fonts(self):
        """
        Creates a dict of font objects with the keys text, highlight, rect, and pos
        """
        pos = self.starting_pos
        for option in self.text_options:
            font_surf = self.font.render(option, True, 'black')
            font_highlight_surf = self.font.render(option, True, 'white')
            font_rect = font_surf.get_frect(center = pos)
            self.font_dict[option] = {'text': font_surf, 'highlight': font_highlight_surf, 'rect': font_rect, 'on_font': False}
            pos = (pos[0], pos[1] + 25)

    def update(self, mpos: tuple): # Check for collision with any of the font rects
        for option in self.font_dict:
            self.font_dict[option]['on_font'] = False
            if self.font_dict[option]['rect'].collidepoint(mpos):
                self.font_dict[option]['on_font'] = True

    def get_mouse_pressed(self, text_option: str) -> bool:
        if self.game.state_interaction_options['left_click']['just_pressed'] and self.font_dict[text_option]['on_font']:
            return True
        return False
    
    def get_key_pressed(self) -> bool:
        if self.game.state_interaction_options['escape']['just_pressed']:
            return True
        return False
    
    def render(self, surf):
        for option in self.font_dict:
            if self.font_dict[option]['on_font']:
                surf.blit(self.font_dict[option]['highlight'], (self.font_dict[option]['rect'].x + 1, self.font_dict[option]['rect'].y + 1))
            surf.blit(self.font_dict[option]['text'], self.font_dict[option]['rect'])
    

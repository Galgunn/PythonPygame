import pygame
from scripts.state import State
from scripts.entities import Player
from scripts.tilemap import Tilemap
from scripts.game_states.pause_menu import PauseMenu
pygame.init()

class GameWorld(State):
    def __init__(self, game):
        super().__init__(game)
        self.player_surf = pygame.Surface((25, 25))
        self.player_rect = self.player_surf.get_frect()
        self.player = Player(game, (20, 20), (25, 25), self.player_surf)
        self.tilemap = Tilemap(self.game)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.K_DOWN:
                if event.key == pygame.K_f:
                    print('yes')
        self.player.update([self.game.movement[1] - self.game.movement[0], self.game.movement[3] - self.game.movement[2]])

        if self.game.state_interaction_options['escape']['just_pressed']:
            pause_menu_state = PauseMenu(self.game)
            pause_menu_state.enter_state()

    def render(self, surf):
        surf.fill('red')
        self.player.render(surf)
'''
Taking a step back to learn how tilemaps work and hopefully use this as a future reference

Working on tile and player collisions now
'''

import pygame, sys

pygame.init()

SCREEN_SIZE:tuple = (600, 400)
TILE_SIZE:int = 16
# Annotate variables
screen: pygame.display
display: pygame.Surface 
clock: pygame.time
running: bool
movement: list
player_movement: tuple
player_surf: pygame.Surface
player_rect: pygame.FRect
floor_surf: pygame.Surface
tilemap: list
physic_rects: list

# Initializing variables
screen = pygame.display.set_mode((SCREEN_SIZE))
display = pygame.Surface((SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2))
clock = pygame.time.Clock()
running = True
movement = [False, False, False, False] # Left, Right, Up, Down
# Loading assets
player_surf = pygame.image.load('examples/tilemap/assets/images/player/00.png').convert_alpha()
player_rect = player_surf.get_rect(topleft=(125, 50)) # NOTE display is being scaled 2x 
floor_surf = pygame.image.load('examples/tilemap/assets/images/tiles/floor/01.png').convert_alpha()
tilemap = [['0', '0', '0', '0', '0', '0', '0'],
           ['0', '0', '0', '0', '0', '0', '0'],
           ['0', '1', '1', '1', '1', '1', '0'],
           ['0', '1', '1', '1', '1', '1', '0'],
           ['1', '1', '1', '1', '1', '1', '1']]

while running:
    # Bliting/rendering to display
    display.fill('blue')


    # Loop for tilemap
    physic_rects = []
    y:int = 0 # Row
    for row in tilemap: # gets the list/row in the tilemap list EX. ['0', '0', '0', '0']
        x:int = 0 # Index
        for tile in row: # gets the tile/index in the row list EX. '0'
            if tile == '1':
                display.blit(floor_surf, (x * TILE_SIZE, y * TILE_SIZE))
            if tile != '0':
                physic_rects.append(pygame.FRect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            x += 1
        y += 1

    display.blit(player_surf, player_rect)
    
    # Calculating and updating position
    player_movement = (movement[1] - movement[0], movement[3] - movement[2])
    player_rect.x += player_movement[0]
    player_rect.y += player_movement[1]

    for physic_tile in physic_rects:
        if physic_tile.colliderect(player_rect):
            pass

    # Scaling to screen/game window
    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), (0, 0))

    # Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Player movement event handler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                movement[0] = True
            if event.key == pygame.K_d:
                movement[1] = True
            if event.key == pygame.K_w:
                movement[2] = True
            if event.key == pygame.K_s:
                movement[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                movement[0] = False
            if event.key == pygame.K_d:
                movement[1] = False
            if event.key == pygame.K_w:
                movement[2] = False
            if event.key == pygame.K_s:
                movement[3] = False
    pygame.display.flip()
    clock.tick(60)

        
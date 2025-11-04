'''
Taking a step back to learn how tilemaps work and hopefully use this as a future reference
'''

import pygame, sys

pygame.init()

SCREEN_SIZE:tuple = (600, 400)
# Annotate variables
screen:pygame.display
display:pygame.Surface 
clock:pygame.time
running:bool 
movement:list # Player movement
player_surf:pygame.Surface
player_rect:pygame.FRect

# Initializing variables
screen = pygame.display.set_mode((SCREEN_SIZE))
display = pygame.Surface((SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2))
clock = pygame.time.Clock()
running = True
movement = [False, False, False, False] # Left, Right, Up, Down
player_surf = pygame.Surface((25, 25))
player_rect = player_surf.get_rect(topleft=(50, 50)) # NOTE display is being scaled 2x 

while running:
    display.fill('blue')
    display.blit(player_surf, player_rect)
    print(movement)

    screen.blit(pygame.transform.scale(display, SCREEN_SIZE), (0, 0)) # Scales 

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

        
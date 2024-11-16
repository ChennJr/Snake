import pygame, sys

pygame.init()
screen = pygame.display.set_mode(((500, 500))) # display surface which created elements are generated on
clock = pygame.time.Clock() # clock object which controls the fps the game runs at
test_surface = pygame.Surface((100, 200))
test_surface.fill((0,0,255))
x_pos = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((175, 215, 70))  
    x_pos += 1   
    screen.blit(test_surface, (x_pos, 250))
    pygame.display.update()
    clock.tick(60)
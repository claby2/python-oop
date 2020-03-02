import pygame, sys

pygame.init()

SIZE = [800, 600]
screen = pygame.display.set_mode(SIZE)

WHITE = [255, 255, 255]
RED = [255, 0, 0]

clock = pygame.time.Clock()

FPS = 60

while True:

    event_list = pygame.event.get()

    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.ext()

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, [55, 200, 100, 70],0)

    pygame.display.update()
    clock.tick(FPS)

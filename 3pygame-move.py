import pygame, random, sys

pygame.init()

SIZE = [800, 600]
SPEED = 10
screen = pygame.display.set_mode(SIZE)

WHITE = [255, 255, 255]
RED = [255, 0, 0]

clock = pygame.time.Clock()

FPS = 60

class Player(pygame.sprite.Sprite):

    def __init__(self, color):
        self.width = 50
        self.height = 50
        self.img = pygame.Surface([self.width, self.height])
        self.img.fill(color)
        self.rect = self.img.get_rect()
        self.rect.centerx = random.randint(0, SIZE[0])
        self.rect.centery = random.randint(0, SIZE[1])

    def moveY(self, direction):
        self.rect.centery += direction*SPEED

    def moveX(self, direction):
        self.rect.centerx += direction*SPEED

    def render(self):
        screen.blit(self.img, self.rect)

    def update(self):
        self.render()

player = Player(RED)
    

while True:

    screen.fill(WHITE)

    event_list = pygame.event.get()

    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.ext()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w: 
                player.moveY(-1)

            if event.key == pygame.K_a:
                player.moveX(-1)

            if event.key == pygame.K_s:
                player.moveY(1)

            if event.key == pygame.K_d:
                player.moveX(1)

    player.update()

    pygame.display.update()
    clock.tick(FPS)

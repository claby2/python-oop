import pygame, random, sys

pygame.init()

SIZE = [800, 600]
SPEED = 10
screen = pygame.display.set_mode(SIZE)

WHITE = [255, 255, 255]

clock = pygame.time.Clock()

FPS = 60

class Firework(pygame.sprite.Sprite):

    def __init__(self, color):
        self.width = random.randint(10,50)
        self.height = random.randint(10,50)
        self.img = pygame.Surface([self.width, self.height])
        self.img.fill(color)
        self.rect = self.img.get_rect()
        self.rect.centerx = random.randint(0, SIZE[0])
        self.rect.centery = random.randint(0, SIZE[1])

    def moveRandom(self):
        self.rect.centerx = random.randint(0, SIZE[0])
        self.rect.centery = random.randint(0, SIZE[1])

    def render(self):
        screen.blit(self.img, self.rect)

    def update(self):
        self.render()

fireworks = []

for i in range(10):
    firework = Firework([random.randint(0,255), random.randint(0,255), random.randint(0,255)])
    fireworks.append(firework)

while True:

    screen.fill(WHITE)

    event_list = pygame.event.get()

    for event in event_list:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.ext()

    for firework in fireworks:
        firework.moveRandom()

    for firework in fireworks:
        firework.update()

    pygame.display.update()
    clock.tick(FPS)
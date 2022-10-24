import os
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

os.environ['SDL_VIDEO_CENTERED'] = '1'
RES = WIDTH, HEIGHT = 1200, 1000
FPS = 60

pygame.init()

screen = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
pygame.display.set_caption('Donut')

running = True
while running:
    clock.tick(FPS)

    # Code

pygame.display.update()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            running = False

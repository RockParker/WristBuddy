import pygame
from player import Player, PlayerFactory

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello, Pygame!")

running = True

p = PlayerFactory().create()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    p.render(screen)
    pygame.display.flip()

pygame.quit()

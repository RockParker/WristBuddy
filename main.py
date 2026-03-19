import pygame
from player import PlayerFactory
from scenebuilder import SceneBuilder, SceneType

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello, Pygame!")

mainScene = SceneBuilder(SceneType.DefaultScene).set_background_image('test_background.gif').set_size((400,300)).build()
p = PlayerFactory().create()
mainScene.subscribe_entity(p)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(mainScene.get_surface())
    mainScene.render_actors()
    #p.render_on(mainScene.get_surface())
    pygame.display.flip()

pygame.quit()

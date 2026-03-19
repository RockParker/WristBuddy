from entity import Entity, EntityFactory
import pygame

class Player(Entity):
    def __init__(self, width: int, height: int, sprite: pygame.Surface):
        super().__init__(width, height, sprite)

class PlayerFactory(EntityFactory):
    
    def create(self):
        player_sprite = pygame.image.load(r'player.png')
        p = Player(player_sprite.width, player_sprite.height, player_sprite)
        return p
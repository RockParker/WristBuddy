import pygame
from abc import ABC, abstractmethod

class Entity(ABC):
    def __init__(self, width: int, height: int, sprite: pygame.Surface):
        self.width = width
        self.height = height
        self.sprite = sprite
        self.entities = []

    def set_image(self, path: str):
        self.image = pygame.image.load(rf'{path}')
        self.scale_image()

    def get_sprite(self) -> pygame.Surface: return self.sprite

    def get_pos(self) -> tuple: return (10, 10)

    def scale_image(self):
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))

    def render_on(self, ctx: pygame.Surface):
        ctx.blit(self.sprite, self.get_pos())

class EntityFactory(ABC):

    @abstractmethod
    def create(self) -> Entity:
        pass

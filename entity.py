import pygame as pg
from abc import ABC, abstractmethod
from scene import Scene

class Entity(ABC):

    def set_image(self, path: str): self.image = pg.image.load(rf'{path}')
    def get_image(self) -> pg.Surface: return self.image
    def get_pos(self) -> tuple: return (10, 10)

    def subscribe_to_scene(self, scene: Scene):
        scene.subcribe_entity(self)

    def render(self, ctx: pg.Surface):
        ctx.blit(self.image, self.get_pos())

class EntityFactory(ABC):

    @abstractmethod
    def create(self) -> Entity:
        pass

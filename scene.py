import pygame
from entity import Entity

# scene.py
# This module controls all rendered elements of the game. This includes the background, player, and UI elements.

class Scene:
    def __init__(self, width: int, height: int, background_image: pygame.Surface):
        self.width = width
        self.height = height
        self.background_image = background_image
        self.entities: list[Entity] = []

    def subscribe_entity(self, entity):
        self.entities.append(entity)

    def get_surface(self):
        return self.background_image
    
    def render_actors(self):
        for entity in self.entities:
            entity.render_on(self.get_surface())

    def update(self):
        for entity in self.entities:
            entity.render()
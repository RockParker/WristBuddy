from enum import Enum
import pygame
from defaultscene import DefaultScene
from scene import Scene

class SceneType(Enum):
    DefaultScene = 1

class SceneBuilder():
    def __init__(self, type = SceneType):
        self.type = type
        self.entities = []
        self.width = 400
        self.height = 300
        self.background_image = pygame.Surface((400, 300))
    
    def set_size(self, size: tuple):
        self.width = size[0]
        self.height = size[1]
        self.scale_image()
        return self

    def set_background_image(self, background_image_path: str):
        self.background_image = pygame.image.load(background_image_path)
        self.scale_image()
        return self
    
    def scale_image(self):
        self.background_image = pygame.transform.scale(self.background_image, (self.width, self.height))

    def set_actors(self, actors: list):
        self.entities = actors
        return self

    def build(self) -> Scene:
        scene: Scene
        match(self.type):
            case SceneType.DefaultScene:
                scene = DefaultScene(self.width, self.height, self.background_image)

        for entity in self.entities:
            entity.subscribe_to_scene(scene)
        return scene
    

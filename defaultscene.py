import pygame
from scene import Scene

class DefaultScene(Scene):
    def __init__(self, width: int, height: int, background: pygame.Surface):
        super().__init__(width, height, background)
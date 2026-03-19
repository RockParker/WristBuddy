from abc import ABC, abstractmethod
from scene import Scene

class Entity(ABC):
    @abstractmethod
    def render(self):
        pass

    
    def subscribe_to_scene(self, scene: Scene):
        scene.subcribe_entity(self)


class EntityFactory(ABC):
    @abstractmethod
    def create(self) -> Entity:
        pass

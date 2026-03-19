
class Scene:
    def __init__(self, name):
        self.name = name
        self.entities = []

    def subcribe_entity(self, entity):
        self.entities.append(entity)
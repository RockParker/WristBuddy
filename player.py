from entity import Entity, EntityFactory

class Player(Entity):

    pass

class PlayerFactory(EntityFactory):
    
    def create(self):
        p = Player()

        p.set_image(r'player.png')

        return p
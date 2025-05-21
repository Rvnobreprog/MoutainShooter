from Code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from Code.Entity import Entity


class EnemyShot(Entity):
     def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]


     def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]


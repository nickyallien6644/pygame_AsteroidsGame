from pygame.math import Vector2
from utils import load_sprite
class GameObject:
    def __init__(self, position, sprite, velocity):
        self.position = Vector2(position)
        self.sprite = sprite
        self.radius = sprite.get_width() / 2
        self.velocity = Vector2(velocity)

    def draw(self, surface):
        blit_position = self.position - Vector2(self.radius)
        surface.blit(self.sprite, blit_position)

    def move(self):
        self.position = self.position + self.velocity

    def collides_with(self, other_obj):
        distance = self.position.distance_to(other_obj.position)
        return distance < self.radius + other_obj.radius

class Spaceship(GameObject):
    # UP = Vector2(0, -1)
    MANEUVERABILITY = 3
    def __init__(self, position):
        # self.direction = Vector2(UP)
        super().__init__(position, load_sprite("spaceship"), Vector2(0))
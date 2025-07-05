import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def is_there_collision(self, other):
        pos_self = self.position
        pos_other = other.position
        distance = pos_self.distance_to(pos_other) 
        if self.radius + other.radius >= distance:
            return True
        else:
            return False


    def draw(self, screen):
        # sub-classes must override
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def update(self, dt):
        # sub-classes must override
        pass
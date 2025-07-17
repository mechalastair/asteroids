import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
         self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20,50)
        v1 = self.velocity.rotate(split_angle)*1.2
        v2 = self.velocity.rotate(-split_angle)*1.2
        split_rad = self.radius - ASTEROID_MIN_RADIUS
        #self.spawn(self, split_rad, self.position, v1)
        #self.spawn(self, split_rad, self.position, v2)
        a1 = Asteroid(self.position.x, self.position.y, split_rad)
        a1.velocity = v1
        a2 = Asteroid(self.position.x, self.position.y, split_rad)
        a2.velocity = v2
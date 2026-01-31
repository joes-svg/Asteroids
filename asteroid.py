from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity *dt
        
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            print(new_angle)
            current_vector = self.velocity
            current_vector.rotate(new_angle)
            rotated_with_speed_vector = current_vector * 1.2
            
            new_astroid1 = Asteroid(self.position.x,self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_astroid1.velocity = rotated_with_speed_vector
            
            new_astroid2 = Asteroid(self.position.x,self.position.y, self.radius - ASTEROID_MIN_RADIUS)
            new_astroid2.velocity = -rotated_with_speed_vector
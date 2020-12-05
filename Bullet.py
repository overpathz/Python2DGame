from settings import*
from images import *
from display import *


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8

    def move(self):
        self.x += self.speed
        if self.x <= screenWidth:
            sc.blit(bullet, (self.x, self.y))
            return True
        else:
            return False

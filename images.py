import pygame as pg
from settings import *

pg.init()

# sprites
bg = pg.image.load("sprites/bg.png")
ground = pg.image.load("sprites/ground.png")
idle = pg.image.load('sprites/idle.png')
walkRight = [pg.image.load('sprites/heroRight.png'), pg.image.load('sprites/heroRight2.png'), pg.image.load('sprites/heroRight.png'), pg.image.load('sprites/heroRight2.png'), pg.image.load('sprites/heroRight.png'), pg.image.load('sprites/heroRight2.png'), pg.image.load('sprites/heroRight.png'), pg.image.load('sprites/heroRight2.png')]
walkLeft = [pg.image.load('sprites/heroLeft.png'), pg.image.load('sprites/heroLeft2.png'), pg.image.load('sprites/heroLeft.png'), pg.image.load('sprites/heroLeft2.png'), pg.image.load('sprites/heroLeft.png'), pg.image.load('sprites/heroLeft2.png'), pg.image.load('sprites/heroLeft.png'), pg.image.load('sprites/heroLeft2.png')]
jumpUp = [pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png'), pg.image.load('sprites/jump.png')]


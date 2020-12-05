import pygame as pg
from settings import *

pg.init()

# game objects
bullet = pg.image.load("sprites/bullet/bullet.png")

# sprites (display)
bg = pg.image.load("sprites/display/bg.png")
ground = pg.image.load("sprites/display/ground.png")

# main player
idlePlayer = pg.image.load('sprites/mainPlayer/idle.png')

walkRightPlayer = [pg.image.load('sprites/mainPlayer/heroRight.png'),
                   pg.image.load('sprites/mainPlayer/heroRight2.png'),
                   pg.image.load('sprites/mainPlayer/heroRight.png'),
                   pg.image.load('sprites/mainPlayer/heroRight2.png'),
                   pg.image.load('sprites/mainPlayer/heroRight.png'),
                   pg.image.load('sprites/mainPlayer/heroRight2.png'),
                   pg.image.load('sprites/mainPlayer/heroRight.png'),
                   pg.image.load('sprites/mainPlayer/heroRight2.png')]

walkLeftPlayer = [pg.image.load('sprites/mainPlayer/heroLeft.png'), pg.image.load('sprites/mainPlayer/heroLeft2.png'),
                  pg.image.load('sprites/mainPlayer/heroLeft.png'), pg.image.load('sprites/mainPlayer/heroLeft2.png'),
                  pg.image.load('sprites/mainPlayer/heroLeft.png'), pg.image.load('sprites/mainPlayer/heroLeft2.png'),
                  pg.image.load('sprites/mainPlayer/heroLeft.png'), pg.image.load('sprites/mainPlayer/heroLeft2.png')]

jumpUpPlayer = [pg.image.load('sprites/mainPlayer/jump.png'), pg.image.load('sprites/mainPlayer/jump.png'),
                pg.image.load('sprites/mainPlayer/jump.png'), pg.image.load('sprites/mainPlayer/jump.png'),
                pg.image.load('sprites/mainPlayer/jump.png'), pg.image.load('sprites/mainPlayer/jump.png'),
                pg.image.load('sprites/mainPlayer/jump.png'), pg.image.load('sprites/mainPlayer/jump.png'),
                pg.image.load('sprites/mainPlayer/jump.png'), pg.image.load('sprites/mainPlayer/jump.png')]

# enemy
idleEnemy = [pg.image.load('sprites/enemy/idle1.png'), pg.image.load('sprites/enemy/idle2.png'),
             pg.image.load('sprites/enemy/idle1.png'), pg.image.load('sprites/enemy/idle2.png'),
             pg.image.load('sprites/enemy/idle1.png'), pg.image.load('sprites/enemy/idle2.png'),
             pg.image.load('sprites/enemy/idle1.png'), pg.image.load('sprites/enemy/idle2.png'),
             pg.image.load('sprites/enemy/idle1.png'), pg.image.load('sprites/enemy/idle2.png')]

walkLeftEnemy = [pg.image.load('sprites/enemy/enemyLeft1.png'), pg.image.load('sprites/enemy/enemyLeft2.png'),
                 pg.image.load('sprites/enemy/enemyLeft1.png'), pg.image.load('sprites/enemy/enemyLeft2.png'),
                 pg.image.load('sprites/enemy/enemyLeft1.png'), pg.image.load('sprites/enemy/enemyLeft2.png'),
                 pg.image.load('sprites/enemy/enemyLeft1.png'), pg.image.load('sprites/enemy/enemyLeft2.png')]

walkRightEnemy = [pg.image.load('sprites/enemy/enemyRight1.png'), pg.image.load('sprites/enemy/enemyRight2.png'),
                  pg.image.load('sprites/enemy/enemyRight1.png'), pg.image.load('sprites/enemy/enemyRight2.png'),
                  pg.image.load('sprites/enemy/enemyRight1.png'), pg.image.load('sprites/enemy/enemyRight2.png'),
                  pg.image.load('sprites/enemy/enemyRight1.png'), pg.image.load('sprites/enemy/enemyRight2.png')]

jumpUpEnemy = [pg.image.load('sprites/enemy/jump1.png'),
               pg.image.load('sprites/enemy/jump2.png'),
               pg.image.load('sprites/enemy/jump3.png'),
               pg.image.load('sprites/enemy/jump4.png'),
               pg.image.load('sprites/enemy/jump1.png'),
               pg.image.load('sprites/enemy/jump2.png'),
               pg.image.load('sprites/enemy/jump3.png'),
               pg.image.load('sprites/enemy/jump4.png')]

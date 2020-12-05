import pygame as pg
from settings import*
from display import*
from player import*
from images import*
from sounds import*
from enemy import *

pg.init()

clock = pg.time.Clock()
running = True
player = Player()
enemy = Enemy()
all_btn_bullets = []


# main function which starts the game / main game loop, which checks all game events
def run():
    global running
    while running:

        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        drawWindow()

        player.movement()
        enemy.movement()

        pg.display.update()

    pg.quit()



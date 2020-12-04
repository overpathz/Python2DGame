import pygame as pg
from settings import*
from display import*
from player import*
from images import*
from sounds import*

pg.init()
clock = pg.time.Clock()
running = True
player = Player()


def run():
    global running
    while running:
        clock.tick(30)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        drawWindow()

        player.movement()

    pg.quit()



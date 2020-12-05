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


# main function which starts the game
def run():
    global running
    while running:

        clock.tick(FPS)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        drawWindow()

        player.movement()

        pg.display.update()

    pg.quit()



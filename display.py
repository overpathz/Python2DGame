import pygame as pg
from settings import*
from images import*

sc = pg.display.set_mode((screenWidth, screenHeight))
pg.display.set_caption('MADE BY KLYMENKO & KUTSELAa')
pg.display.set_icon(pg.image.load('logo/logo.png'))


def drawWindow():
    sc.blit(bg, (0, 0))
    sc.blit(ground, (0, 650))

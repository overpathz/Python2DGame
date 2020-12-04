import pygame as pg
from settings import*
from display import*

pg.init()

# background music
pg.mixer.music.load('sounds/bgsong.mp3')
pg.mixer.music.set_volume(MUSIC_VOLUME)
pg.mixer.music.play(-1)

# sounds

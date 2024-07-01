from random import  randint
import pygame as pg

size = (500, 500)
screen = pg.display.set_mode(size)

fps = 5

clock = pg.time.Clock()

while True:
    r = randint(0,255)
    screen.fill(pg.Color(r, 54, 72))

    pg.display.flip()
    clock.tick(fps)
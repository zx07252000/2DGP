import random
import json
import os

from pico2d import *
import game_framework

name="Stage1_MeiMei"
image=None


def enter():
    global image
    image = load_image('stage1.png')
    pass

def exit():
    global image
    del (image)
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()

    pass

def draw():
    x=0
    frame = 0
    while(x<780):
        clear_canvas()
        image.clip_draw(frame*10, -200, 1040, 767, 500, 382)
        update_canvas()
        frame=(frame+1)%100
        x+=1
        delay(0.1)
    MeiMei.draw()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass
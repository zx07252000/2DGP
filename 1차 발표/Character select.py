import random
import json
import os

from pico2d import *

import game_framework
import Main_Screen

name ="Character select"
image = None

def enter():
    global image
    image = load_image('character select.png')
    pass


def exit():
    global image
    del (image)
    pass


def pause():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.change_state(Main_Screen)
           
    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()
    pass


def update():
    pass


def resume():
    pass
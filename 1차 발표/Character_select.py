import random
import json
import os

from pico2d import *

import game_framework
import Main_Screen
import Stage1_male
import Stage1_female

name ="Character_select"
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
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
                game_framework.change_state(Stage1_male)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
                game_framework.change_state(Stage1_female)

    pass


def draw():
    clear_canvas()
    image.clip_draw(0,0,1020,767,512, 382)
    update_canvas()
    pass


def update():
    pass


def resume():
    pass
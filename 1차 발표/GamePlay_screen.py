import random
import json
import os

from pico2d import *

import game_framework


from CharacterMeiMei import MeiMei
from Stage1screen import Stage1

name = "GamePlay_screen"

CharacterMeiMei=None
Stage1screen=None



def enter():
    global CharacterMeiMei,Stage1screen
    CharacterMeiMei = MeiMei()
    Stage1screen=Stage1()

def exit():
    global CharacterMeiMei,Stage1screen
    del CharacterMeiMei
    del Stage1screen


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            CharacterMeiMei.handle_event(event)

def update():
    CharacterMeiMei.update()

def draw():
    clear_canvas()
    Stage1screen.draw()
    CharacterMeiMei.draw()
    update_canvas()







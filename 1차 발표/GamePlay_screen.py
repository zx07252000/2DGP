import random
import json
import os

from pico2d import *

import game_framework


from CharacterMeiMei import MeiMei
from Stage1screen import Stage1
from Stage2screen import Stage2

name = "GamePlay_screen"

CharacterMeiMei=None
Stage1screen=None
Stage2screen=None
logo_time=0

def enter():
    global CharacterMeiMei,Stage1screen,Stage2screen
    CharacterMeiMei = MeiMei()
    Stage1screen=Stage1()
    Stage2screen = Stage2()

def exit():
    global CharacterMeiMei,Stage1screen,Stage2screen
    del CharacterMeiMei
    del Stage1screen
    del Stage2screen


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
    global logo_time

    if (logo_time > 1.0):
        Stage2screen.draw()
    delay(0.01)
    logo_time += 0.01
    CharacterMeiMei.draw()
    update_canvas()







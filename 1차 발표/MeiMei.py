from pico2d import *
import game_framework

IDLE, RUN = range(2)

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP = range(4)

key_event_table = {

    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,

    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,

    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,

    (SDL_KEYUP, SDLK_LEFT): LEFT_UP

}


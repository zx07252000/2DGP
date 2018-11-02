
from pico2d import *
import game_framework
import Character_select

name="Main_Screen"
image=None


def enter():
    global image
    image=load_image('Resource\\Main_Screen.png')
    pass

def exit():
    global image
    del(image)
    pass

def handle_events():
    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type,event.key)==(SDL_KEYDOWN,SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(Character_select)

    pass

def draw():
    clear_canvas()
    image.draw(512,382)
    update_canvas()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass

def Main_Screen_to_Character_Screen():
    global x,y
    events=get_events()
    pass


def Character_Screen_to_GamePlay_Screen():
    pass


def Main_Screen_to_Ranking():
    pass


def Main_Screen_to_Shop():
    pass


def Main_Screen_to_Exit():
    pass





import game_framework
from pico2d import *


Main_Screen_WIDTH,Main_Screen_HEIGHT=1020,767

open_canvas(Main_Screen_WIDTH,Main_Screen_HEIGHT)

Start_background = load_image('Main_Screen.png')

def handle_events():
    global Background
    global x,y
    events = get_events()

    for event in events:
        if event.type==SDL_QUIT:
            Background = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, Main_Screen_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Background = False
        elif event.type==SDL_KEYDOWN and event.key==SDLK_1
            game_framework.Change_state(pause1)



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


x=0
y=0
frame=0
Background=True

while Background:

    clear_canvas()
    Start_background.draw(Main_Screen_WIDTH//2,Main_Screen_HEIGHT//2)
   

    update_canvas()
    frame=(frame+1)%1
    delay(0.01)
    handle_events()
    get_events()


close_canvas()


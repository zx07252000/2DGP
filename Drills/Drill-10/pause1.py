import game_framework
from pico2d import *
import main_state

time=0
twinkle=0
name = "pause1"
image = None


def enter():
    global image
    image=load_image('pause.png')
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
            elif(event.type,event.key)==(SDL_KEYDOWN,SDLK_p):
                game_framework.pop_state()
    pass


def draw():
    clear_canvas()
    if twinkle==0:
        image.draw(400,300)
    main_state.boy.draw()
    main_state.grass.draw()
    update_canvas()
    pass



def update():
    global time
    global twinkle
    if time>1.0:
        if twinkle==1:
            twinkle=0
        else:
            twinkle=1
        time=0
    time+=0.005
    pass


def pause():
    pass


def resume():
    pass
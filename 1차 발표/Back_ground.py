from pico2d import *



Start_background_WIDTH,Start_background_HEIGHT=1020,897

open_canvas(Start_background_WIDTH,Start_background_HEIGHT)

Start_background = load_image('Title background2.png')

def handle_events():
    global moving
    global x,y
    events = get_events()

    for event in events:
        if event.type==SDL_QUIT:
            moving = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, Start_background_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            moving = False



def Start_background_to_Character_background():
    global x,y
    events=get_events()
    pass

def Character_background_to_GamePlay_background():
    pass



x=0
y=0
frame=0
Background=True

while Background:

    clear_canvas()
    Start_background.draw(Start_background_WIDTH//2,Start_background_HEIGHT//2)
    update_canvas()
    frame=(frame+1)%1
    delay(0.01)
    handle_events()
    get_events()


close_canvas()


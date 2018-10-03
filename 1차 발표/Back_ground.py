from pico2d import *



Start_background_WIDTH,Start_background_HEIGHT=600,600

open_canvas(Start_background_WIDTH,Start_background_HEIGHT)

Start_background = load_image('Title background.png')

def handle_events():
    pass


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
    Start_background.draw(Start_background_WIDTH//2+50,Start_background_HEIGHT//2-220)
    update_canvas()
    frame=(frame+1)%1
    delay(0.01)
    get_events()


close_canvas()


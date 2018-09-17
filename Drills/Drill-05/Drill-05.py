from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x, y, frame = 0, 0, 0


def right_direction(x,y,frame):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    delay(0.01)
    get_events()


def left_direction(x,y,frame):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    delay(0.01)
    get_events()



def move_point_to_point(x1, y1, x2, y2):
    #right_direction(x1, y1, frame)
    left_direction(x1,y1,frame)

    
while True:
    move_point_to_point(203, 535, 132, 243)



close_canvas()


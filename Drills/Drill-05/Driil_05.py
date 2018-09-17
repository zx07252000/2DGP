from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x=0
y=0
frame=0

def move_point_to_point1(x1,y1,x2,y2,frame):
    if(x1>x2):
        x_distance=x1-x2
        y_distance=y1-y2
        gradient=y_distance//x_distance

    while(x1>x2):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,0,100,100,x1,y1)
        update_canvas()
        frame=(frame+1)%8
        x1-=1
        y1-=1*gradient

        delay(0.01)
        get_events()
def move_point_to_point2(x1,y1,x2,y2,frame):
    if(x1<x2):
        x_distance=x2-x1
        y_distance=y2-y1

        gradient=x_distance//y_distance

    while(x1<x2):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,100,100,100,x1,y1)
        update_canvas()
        frame=(frame+1)%8
        x1+=1.5
        y1+=1*gradient

        delay(0.01)
        get_events()
def move_point_to_point3(x1,y1,x2,y2,frame):
    if (x1 > x2):
        x_distance = x1 - x2
        y_distance = y1 - y2
        gradient = y_distance // x_distance

    while (x1 > x2):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 1
        y1 -= 1 * gradient

        delay(0.01)
        get_events()
def move_point_to_point4(x1,y1,x2,y2,frame):

        x_distance=x2-x1
        y_distance=y2-y1
        gradient=y_distance//x_distance

        while(x2>x1):
            clear_canvas()
            grass.draw(400,30)
            character.clip_draw(frame*100,100,100,100,x1,y1)
            update_canvas()
            frame=(frame+1)%8
            x1+=2
            y1+=1*gradient

            delay(0.01)
            get_events()


def move_point_to_point4(x1, y1, x2, y2, frame):
    x_distance = x2 - x1
    y_distance = y2 - y1
    gradient = y_distance // x_distance

    while (x2 > x1):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 100, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 += 2
        y1 += 1 * gradient

        delay(0.01)
        get_events()
def move_point_to_point5(x1, y1, x2, y2, frame):
    x_distance = x1 - x2
    y_distance = y1 - y2
    gradient = y_distance // x_distance

    while (x2 < x1):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x1, y1)
        update_canvas()
        frame = (frame + 1) % 8
        x1 -= 2
        y1 -= 0.5* gradient

        delay(0.01)
        get_events()


while True:
    #move_point_to_point1(203,535,132,243,frame)
    #move_point_to_point2(132,243,535,470,frame)
    #move_point_to_point3(535, 470,477, 203, frame)
    move_point_to_point4(477,203,715,136,frame)
    move_point_to_point5(715, 136, 316, 225, frame)







close_canvas()


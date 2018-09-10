from pico2d import *
import math

os.chdir('C:\\Program Files (x86)\\2D Game\\Labs\\Lecture03')


open_canvas()
r=0
x=0
y=90

grass = load_image('grass.png')
character = load_image('character.png')
while True:
    r=90
    y=90
    while (x<800):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x + 2
        delay(0.01)
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y + 2
        delay(0.01)
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x = x - 2
        delay(0.01)
    while(y>0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y = y - 2
        delay(0.01) 
    

    while(r<=450):
        fx=400+math.cos(r*3.14/180)*100
        fy=180-math.sin(r*3.14/180)*100
        r+=30
        
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(fx,fy)
        delay(0.2)
    
        

    
    
close_canvas()

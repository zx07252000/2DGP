from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('stage1.png')

        self.event_que = []

        self.x, self.y = 500 , 382

        self.dir = 1

        self.velocity = 0
    def enter_IDLE(self):
        self.timer = 1000
        self.frame = 0

    def exit_IDLE(self):
        pass

    def do_IDLE(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1

    def draw(self):

        self.frame = 0


        self.image.clip_draw(self.frame * 10, -200, 1040, 767, self.x,self.y)

        self.x -= 10
        if(self.x==300):
            self.x=500

        delay(0.1)
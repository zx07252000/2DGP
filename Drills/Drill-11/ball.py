from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1,frame=1):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity,self.frame = x, y, velocity,frame

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 16, 30, self.x, self .y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)

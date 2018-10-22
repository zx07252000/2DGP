from pico2d import *
import game_framework

IDLE, Attack = range(2)

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP,UP_DOWN,DOWN_DOWN = range(6)

key_event_table = {

    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,

    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,

    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,

    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,


    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,


    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN



}
next_state_table = { IDLE: {RIGHT_UP: Attack, LEFT_UP: Attack, RIGHT_DOWN: Attack, LEFT_DOWN: Attack,
                            UP_DOWN:Attack,DOWN_DOWN:Attack},
                     Attack: {RIGHT_UP: IDLE, LEFT_UP: IDLE, LEFT_DOWN: IDLE, RIGHT_DOWN: IDLE,UP_DOWN:IDLE,DOWN_DOWN:IDLE} }
class MeiMei:
    image=None
    def __init__(self):

        self.event_que = []

        self.x, self.y = 70, 70
        if MeiMei.image==None:
            MeiMei.image = load_image('CharacterMeiMei.png')

        self.cur_state = IDLE

        self.dir = 1

        self.velocity = 0


        self.enter_state[IDLE](self)
    def enter_IDLE(self):
        self.timer = 1000
        self.frame = 0
    def exit_IDLE(self):
        pass
    def do_IDLE(self):
        self.frame = (self.frame + 1) % 8
        self.timer -=1
    def draw_IDLE(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame * 0, 170, 60, 60, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 0, 170, 60, 60, self.x, self.y)

    def enter_Attack(self):
        self.frame = 0
        self.dir = self.velocity
    def exit_Attack(self):
        pass
    def do_Attack(self):
        self.frame = (self.frame + 1) % 8
        self.y += self.velocity


        self.x = clamp(25, self.x, 800-25)
    def draw_Attack(self):
        if self.velocity == 1:
            self.image.clip_draw(self.frame * 0, 170, 60, 60, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 0, 170, 60, 60, self.x, self.y)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def change_state(self,  state):
        self.exit_state[self.cur_state](self)
        self.enter_state[state](self)
        self.cur_state = state
    enter_state = {IDLE: enter_IDLE, Attack: enter_Attack}
    exit_state = {IDLE: exit_IDLE, Attack: exit_Attack}
    do_state = {IDLE: do_IDLE, Attack: do_Attack}
    draw_state = {IDLE: draw_IDLE, Attack: draw_Attack}

    def update(self):
        self.do_state[self.cur_state](self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.change_state(next_state_table[self.cur_state][event])

    def draw(self):

        self.draw_state[self.cur_state](self)


    def handle_event(self, event):

        if (event.type, event.key) in key_event_table:

            key_event = key_event_table[(event.type, event.key)]

            if key_event == RIGHT_DOWN:

                self.velocity += 1

            elif key_event == LEFT_DOWN:

                self.velocity -= 1

            elif key_event == RIGHT_UP:

                self.velocity -= 1

            elif key_event == LEFT_UP:

                self.velocity += 1
            elif key_event==UP_DOWN:
                self.length += 1
            elif key_event==DOWN_DOWN:
                self.velocity -= 1

            self.add_event(key_event)


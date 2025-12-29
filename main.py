import random
import tkinter
from time import sleep

class Ball:
    def __init__(self,canvas:tkinter.Canvas,pad,score):
        self.canvas = canvas
        self.my_obj = self.canvas.create_oval(0,0,30,30,fill='white')
        self.canvas.move(self.my_obj,485,285)
        rnd_x = random.choice([-3,-2,2,3])
        self.speed_x = rnd_x
        rnd_y = random.choice([-3,-2])
        self.speed_y = rnd_y
        self.pad = pad
        self.score = score
        self.game_over = False

    def draw(self):
        self.canvas.move(self.my_obj,self.speed_x,self.speed_y)
        pos = self.canvas.coords(self.my_obj)
        print(pos)
        if pos[1] <= 0:
            self.speed_y = -self.speed_y
        if pos[3] >= 600:
            self.canvas.create_text(500,300, text='ВЫ ПРОИГРАЛИ(',fill='red',font=(None,50))
            self.game_over = True
        if pos[0] <= 0:
            self.speed_x = -self.speed_x
        if pos[2] >= 1000:
            self.speed_x = -self.speed_x
        if self.hit_pad(pos):
            self.speed_y = -self.speed_y

    def hit_pad(self,pos):
        pad_pos = self.canvas.coords(self.pad.my_obj)
        if pos[2] >= pad_pos[0] and pos[0] <= pad_pos[2]:
            if pad_pos[1] <= pos[3] <=pad_pos[3]:
                self.score.hit_pad2()
                return True
        return False


class Pad:
    def __init__(self,canvas:tkinter.Canvas):
        self.canvas = canvas
        self.my_obj = self.canvas.create_rectangle(0,0,150,15,fill='red')
        self.canvas.move(self.my_obj,425,550)
        self.speed_x = 0
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)

    def draw(self):
        self.canvas.move(self.my_obj,self.speed_x,0)
        pos = self.canvas.coords(self.my_obj)
        if pos[0] <= 0:
            self.speed_x = -self.speed_x
        if pos[2] >= 1000:
            self.speed_x = -self.speed_x

    def turn_left(self,event):
        self.speed_x = -3

    def turn_right(self,event):
        self.speed_x = 3


class Score:
    def __init__(self,canvas:tkinter.Canvas):
        self.canvas = canvas
        self.score = 0
        self.my_obj = self.canvas.create_text(500,20, text=self.score,fill='red',font=(None,14))

    def hit_pad2(self):
        self.score += 1
        self.canvas.itemconfig(self.my_obj,text=self.score)

window = tkinter.Tk()
window.title('ping-pong')
window.geometry('1000x600+255+105')
window.resizable(0,0)
window.wm_attributes('-topmost',1)
canvas = tkinter.Canvas(window,width=1000,height=600,bg='light blue',bd=0,highlightthickness=0)
canvas.pack()
window.update()

score = Score(canvas)
pad = Pad(canvas)
ball = Ball(canvas,pad,score)

while True:
    if ball.game_over is False:
        ball.draw()
        pad.draw()
    else:
        sleep(3)
        break
    window.update()
    window.update_idletasks()
    sleep(0.01)
window.destroy()
from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle_1, paddle_2, color):
        self.canvas = canvas
        self.paddle_1 = paddle_1
        self.paddle_2 = paddle_2
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_left = False
        self.hit_right = False

    def hit_paddle(self, pos):
        paddle_pos_1 = self.canvas.coords(self.paddle_1.id)
        if pos[0] <= paddle_pos_1[1] and pos[1] <= paddle_pos_1[0]:
            if pos[2] >= paddle_pos_1[3] and pos[2] <= paddle_pos_1[3]:
                return True
            return False
        paddle_pos_2 = self.canvas.coords(self.paddle_2.id)
        if pos[3] >= paddle_pos_2[1] and pos[1] <= paddle_pos_2[3]:
            if pos[2] >= paddle_pos_2[0] and pos[2] <= paddle_pos_2[0]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_width:
            self.hit_right = True
        if pos[2] <= 0:
            self.hit_left = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if self.hit_paddle(pos) == True:
            self.y = 3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

class Paddle_First:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10, 100, fill=color)
        self.canvas.move(self.id, 450, 200)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Up>', self.go_up)
        self.canvas.bind_all('<KeyRelease-Up>', self.go_nowhere)
        self.canvas.bind_all('<KeyPress-Down>', self.go_down)
        self.canvas.bind_all('<KeyRelease-Down>', self.go_nowhere)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)

    def go_up(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[1] < 0:
            self.y = 0
        else:
            self.y = -3

    def go_down(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[3] > self.canvas_height:
            self.y = 0
        else:
            self.y = 3

    def go_nowhere(self, evt):
        self.y = 0

class Paddle_Second:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 10, 100, fill=color)
        self.canvas.move(self.id, 50, 200)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-W>', self.go_up)
        self.canvas.bind_all('<KeyRelease-W>', self.go_nowhere)
        self.canvas.bind_all('<KeyPress-S>', self.go_down)
        self.canvas.bind_all('<KeyRelease-S>', self.go_nowhere)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)

    def go_up(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[1] < 0:
            self.y = 0
        else:
            self.y = -3

    def go_down(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[3] > self.canvas_height:
            self.y = 0
        else:
            self.y = 3

    def go_nowhere(self, evt):
        self.y = 0

def game():
    w = 0
    v = 0
    canvas.delete(button_window)
    timer1 = time.time()
    while 1:
        if ball.hit_right == False and ball.hit_left == False:
            ball.draw()
            paddle_1.draw()
            paddle_2.draw()
        root.update_idletasks()
        root.update()
        time.sleep(0.01)
        if ball.hit_left == True:
            v = 1
            break
        if ball.hit_right == True:
            w = 1
            break
    canvas.delete("all")
    canvas.create_text(250, 150, font="Arial 70", text="Game Over")
    if w == 1:
        canvas.create_text(250, 300, font="Times 48", text='Left Wins!')
    if v == 1:
        canvas.create_text(250, 300, font="Times 48", text='Right Wins!')

root = Tk()
root.title("Game")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=500, height=400, bd=0, highlightthickness=0)

canvas.pack()
root.update()

paddle_1 = Paddle_First(canvas, 'blue')
paddle_2 = Paddle_Second(canvas, 'blue')
ball = Ball(canvas, paddle_1, paddle_2, 'red')

button_start = Button(master=None, font="Times 80", text="Start?", command=game)
button_window = canvas.create_window(250, 100, anchor=N, window=button_start)


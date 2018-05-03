#!/usr/bin/env python3

from tkinter import *

import time

import random

from copy import *

tk = Tk()

# tk button
# button = Button(tk, 
#                    text="QUIT", 
#                    fg="red",
#                    command=quit)
# button.pack(side=LEFT)

tk.title('Game')
tk.resizable(0,0)
tk.wm_attributes("-topmost", 1)
# while True:
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
# tk.update()
# for x in range(0, 100):
# 	width = random.randint(1, 50)
# 	height = random.randint(1, 300)
# 	canvas.create_rectangle(10,10, width, height)

class Ball(object):
	"""docstring for Ball"""
	def __init__(self, canvas, color, paddle_id):
		super(Ball, self).__init__()
		# self.arg = arg
		self.color = color
		self.canvas = canvas
		start = [1,2,3,-1,-2,-3]
		random.shuffle(start)
		# x, y speed
		self.x = start[0]
		self.y = -1
		self.paddle_id = paddle_id
		self.canvas_height = self.canvas.winfo_reqheight()
		self.canvas_width = self.canvas.winfo_reqwidth()
		# id show current canvas element
		self.id = canvas.create_oval(10,10,25,25,fill=color)
		canvas.move(self.id, 245, 100)

	# loop execution to prevent reach the limit
	def draw(self):
		self.canvas.move(self.id, self.x, self.y)
		pos = self.canvas.coords(self.id)
		paddle_pos = self.canvas.coords(self.paddle_id)
		if pos[1] <= 1:
			self.y = 1
		if pos[3] >= self.canvas_height:
			self.y = -1
		if self.hit_paddle(pos, paddle_pos):
			start = [1,2,3,-1,-2,-3]
			random.shuffle(start)
			# x, y speed
			self.x = start[0]
			self.y = -1
		if pos[0] <= 1:
			self.x = 1
		if pos[2] >= self.canvas_width:
			self.x = -1

	# hit return True
	def hit_paddle(self, pos, paddle_pos):
		# paddle_pos = self.canvas.coords(self.paddle_id)
		if pos[2] >=paddle_pos[0] and pos[0] <=paddle_pos[2]:
			if pos[3] >= paddle_pos[1] and pos[3] <=paddle_pos[3]:
				return True
		return False

class Paddle(object):
	"""docstring for Paddle"""
	def __init__(self, canvas, color):
		super(Paddle, self).__init__()
		self.canvas = canvas
		self.color = color
		self.id = canvas.create_rectangle(0,0,100,10, fill=color)
		self.canvas_width = self.canvas.winfo_reqwidth()
		canvas.move(self.id, 200, 300)
		# x, speed
		self.x = 0
		canvas.bind_all('<KeyPress-Left>', self.move)
		canvas.bind_all('<KeyPress-Right>', self.move)

	def move(self, event):
		if event.keysym == 'Up':
			canvas.move(self.id, 0, -4)
		elif event.keysym == 'Down':
			canvas.move(self.id, 0, 4)
		elif event.keysym == 'Left':
			# canvas.move(self.id,-3, 0)
			self.x = -3
		elif event.keysym == 'Right':
			# canvas.move(self.id, 3, 0)
			self.x = 3
		# self.draw()


	# loop execution to prevent the limit
	def draw(self):
		pos = self.canvas.coords(self.id)
		if pos[0] <= 1 and self.x <= 0:
			self.x = 0
		if pos[2] >= self.canvas_width and self.x >= 0:
			self.x = 0
		self.canvas.move(self.id, self.x, 0)
		self.x = 0


class Button(object):
	"""docstring for Button"""
	def __init__(self, canvas, text, color, pos, ball):
		super(Button, self).__init__()
		self.text = text
		self.color = color
		self.ball = ball
		self.st = True
		self.canvas = canvas
		canvas.create_text(pos['x'] + 40, pos['y'] + 15, text=text)
		self.save_ball_pos = [0, 0]
		self.id = canvas.create_rectangle(0,0,80,30, outline=color)
		canvas.move(self.id, pos['x'], pos['y'])
		canvas.bind_all('<KeyPress-W>', self.toggle)
				
	def toggle(self, event):
		print(event.keysym)
		if self.ball.x != 0:
			self.save_ball_pos[0] = copy(self.ball.x)
			self.ball.x = 0
			self.st = False
		else:
			self.st = True
			self.ball.x = self.save_ball_pos[0]
		if self.ball.y != 0:
			self.save_ball_pos[1] = copy(self.ball.y)
			self.ball.y = 0
			self.st = False
		else:
			self.st = True
			self.ball.y = self.save_ball_pos[1]
		print(self.save_ball_pos)

red_Paddle = Paddle(canvas, 'green')

red_ball = Ball(canvas, 'red', red_Paddle.id)

start_btn = Button(canvas, 'start', 'grey', {'x': 10, 'y': 20}, red_ball)
# pause_btn = Button('pause', 'purple', {'x': 120, 'y': 20})


while True:
	if start_btn.st:
		red_ball.draw()
	red_Paddle.draw()
	tk.update_idletasks()
	tk.update()
	time.sleep(0.01)

# tk.mainloop()

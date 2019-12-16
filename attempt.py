from tkinter import *
import math
import time

root = Tk()
canv = Canvas(root, width=1200, height=800, bg='white')
canv.pack(fill=BOTH, expand=1)
dt = 3

class Ball:
    def __init__(self):  # создание шарика
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Ax = 0
        self.Ay = 0


def yes(n):  # Создание n шариков
    for i in range(0, n):
        ball.append(Ball())


def start_from(x_0, y_0):
    for i in range(0, len(ball)):
        ball[i].x = (i + 1) * x_0  # начальные x координаты шариков
        ball[i].y = y_0  # начальные y координаты шариков
    

def move_ball():  # новые координаты шариков
    for i in range(0, len(ball)):
        if i != len(ball) // 2:
            ball[i].x += ball[i].Vx + ball[i].Ax
            ball[i].Vx += ball[i].Ax
            ball[i].y += ball[i].Vy + ball[i].Ay
            ball[i].Vy += ball[i].Ay
        else:
            ball[i].y += ball[i].Vy


def acceleration(parameter, l_0, u):
    '''
    l_0 длина пружины в нерастянутом состоянии
    parameter = жесткость/масса
    u скорость движения центрального шарика
    '''
    main_ball_num = len(ball) // 2
    for i in range(0, len(ball)):
        if i == 0:  # крайний левый шарик (первый)
            x_0 = ball[i].x
            y_0 = ball[i].y
            x_1 = ball[i + 1].x
            y_1 = ball[i + 1].y
            l_01 = math.sqrt((x_0 - x_1) ** 2 + (y_0 - y_1) ** 2)
            # alpha_12 = math.acos((y_2 - y_1) / l_12)
            ball[i].Ax = parameter * (l_01 - l_0) * (x_1 - x_0) / l_01
            ball[i].Ay = parameter * (l_01 - l_0) * (y_1 - y_0) / l_01
            # ball[i].Vx += ball[i].Ax 
            # ball[i].Vy += ball[i].Ay
        if i < main_ball_num and i != 0:
            x_0 = ball[i - 1].x
            y_0 = ball[i - 1].y
            x_1 = ball[i].x
            y_1 = ball[i].y
            x_2 = ball[i + 1].x
            y_2 = ball[i + 1].y
            l_12 = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
            l_01 = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
            # alpha_01 = math.acos((y_1 - y_0) / l_01)
            # alpha_12 = math.acos((y_2 - y_1) / l_12)
            ball[i].Ax = parameter * ((l_12 - l_0) * (x_2 - x_1) / l_12 - (l_01 - l_0) * (x_1 - x_0) / l_01)
            ball[i].Ay = parameter * ((l_12 - l_0) * (y_2 - y_1) / l_12 + (l_01 - l_0) * (y_1 - y_0) / l_01)
            # ball[i].Vx += ball[i].Ax
            # ball[i].Vy += ball[i].Ay
        if i == main_ball_num:
            ball[i].Vy = u
        if i > main_ball_num and i != len(ball) - 1:  # все остальные
            x_1 = ball[i].x
            y_1 = ball[i].y
            x_2 = ball[i - 1].x
            y_2 = ball[i - 1].y
            x_0 = ball[i + 1].x
            y_0 = ball[i + 1].y
            l_12 = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
            l_01 = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
            # alpha_01 = math.asin((x_1 - x_0) / l_01)
            # alpha_12 = math.asin((x_2 - x_1) / l_12)
            ball[i].Ax = parameter * ((l_12 - l_0) * (x_2 - x_1) / l_12 - (l_01 - l_0) * (x_1 - x_0) / l_01)
            ball[i].Ay = parameter * ((l_12 - l_0) * (y_2 - y_1) / l_12 + (l_01 - l_0) * (y_1 - y_0) / l_01)
            # ball[i].Vx += ball[i].Ax
            # ball[i].Vy += ball[i].Ay 
        if i == len(ball) - 1:  # крайний правый (последний шарик)
            x_0 = ball[i - 1].x
            y_0 = ball[i - 1].y
            x_1 = ball[i].x
            y_1 = ball[i].y
            l_01 = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
            # alpha_12 = math.asin((x_1 - x_0) / l_01)
            ball[i].Ax = parameter * (l_01 - l_0) * (x_0 - x_1) / l_01
            ball[i].Ay = parameter * (l_01 - l_0) * (y_0 - y_1) / l_01
            # ball[i].Vx += ball[i].Ax
            # ball[i].Vy += ball[i].Ay 


def rendering():  # отрисовка линии
    for i in range(0, len(ball) - 1):
        canv.create_line(ball[i].x, ball[i].y, ball[i + 1].x, ball[i + 1].y)
        canv.create_oval(ball[i].x, ball[i].y-2.5, ball[i].x + 5, ball[i].y + 2.5)
    canv.create_oval(ball[len(ball) - 1].x, ball[len(ball) - 1].y-2.5, ball[len(ball) - 1].x + 5, ball[len(ball) - 1].y + 2.5)


def modeling():
    canv.delete("all")
    acceleration(0.02, 10, 0.5)
    move_ball()
    rendering()
    root.after(dt, modeling)


ball = []
yes(50)
start_from(10, 10)
modeling()
# root.mainloop()

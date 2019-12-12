from tkinter import *
import math
import time


root = Tk()
root.geometry('10000x700')
canv = Canvas(root, width=800, height=600, bg='white')
canv.pack(fill=BOTH, expand=1)
colors = ['red']

class Ball:
    def __init__(self):  # создание шарика
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0


def yes(n):  # Создание n шариков
    for i in range(n):
        ball.append(Ball())

def natch (x_0, y_0):
    for i in range(len(ball)):
        ball[i].x = i * x_0  # начальные x коардинаты шариков
        ball[i].y = y_0      # начальные y коардинаты шариков
        
def move_central(u): # перемещение
    central_k = int((len(ball)- 1)/2)
    ball[central_k].y += u

def move_ball(): # новые каординаты шариков
    for i in range(len(ball) - 1):
        ball[i].x += ball[i].Vx
        ball[i].y += ball[i].Vy

def  acceleration(parameter, l_0):
    '''
    l_0 длинна пружины в нерастянутом состоянии 
    parameter = жесткость/масс
    '''
    for i in range(0, len(ball)-1, 1):
        if i == 0:                  # крайне лейвый шарик (первый)
            x_1 = ball[i].x
            y_1 = ball[i].y
            x_2 = ball[i + 1].x
            y_2 = ball[i + 1].y
            l_12 = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
            alpha_12 = math.asin((x_2 - x_1)/l_12)
            ball[i].Vx += parameter * (l_12 - l_0) * math.sin(alpha_12)
            ball[i].Vy += parameter * (l_12 - l_0) * math.cos(alpha_12)
        elif i < (len(ball) - 1) / 2: 
            x_1 = ball[i].x
            y_1 = ball[i].y
            x_2 = ball[i + 1].x
            y_2 = ball[i + 1].y
            x_0 = ball[i - 1].x
            y_0 = ball[i - 1].y
            l_12 = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
            l_01 = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
            alpha_01 = math.asin((x_1 - x_0)/l_01)
            alpha_12 = math.asin((x_2 - x_1)/l_12)
            ball[i].Vx += parameter * ((l_12 - l_0) * math.sin(alpha_12) - (l_01 - l_0) * math.sin(alpha_01))
            ball[i].Vy += parameter * ((l_12 - l_0) * math.cos(alpha_12) + (l_01 - l_0) * math.cos(alpha_01))
        elif i == (len(ball) - 1) / 2: # центральный шарик
            ball[i].Vx += 0
            ball[i].Vy += 0
        elif i > (len(ball) - 1) / 2 and i != len(ball) - 1:                       # все остальные
            x_1 = ball[i].x
            y_1 = ball[i].y
            x_2 = ball[i + 1].x
            y_2 = ball[i + 1].y
            x_0 = ball[i - 1].x
            y_0 = ball[i - 1].y
            l_12 = math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2)
            l_01 = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
            alpha_01 = math.asin((x_1 - x_0)/l_01)
            alpha_12 = math.asin((x_2 - x_1)/l_12)
            ball[i].Vx += parameter * ((l_12 - l_0) * math.sin(alpha_12) - (l_01 - l_0) * math.sin(alpha_01))
            ball[i].Vy += parameter * (+(l_12 - l_0) * math.cos(alpha_12) + (l_01 - l_0) * math.cos(alpha_01))  
        elif i == len(ball) - 1:       # крайний правый (последний шарик) 
            x_1 = ball[i].x
            y_1 = ball[i].y
            x_0 = ball[i - 1].x
            y_0 = ball[i - 1].y
            l_01 = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
            alpha_12 = math.asin((x_1 - x_0)/l_01)
            ball[i].Vx += -parameter * (l_01 - l_0) * math.sin(alpha_01)
            ball[i].Vy += parameter * (l_01 - l_0) * math.cos(alpha_01)
def rendering(): # отрисовка линии
    for i in range(len(ball) - 2):
        canv.create_line(ball[i].x, ball[i].y, ball[i + 1].x, ball[i + 1].y)



def modeling():
    canv.delete("all")
    move_central(0.05)
    move_ball()
    acceleration(0.01, 10)
    rendering()
    root.after(10, modeling)


ball = []
yes(120)
natch(10, 10)
modeling()
print(len(ball))

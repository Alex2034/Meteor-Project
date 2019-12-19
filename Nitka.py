from tkinter import *
import math
import time

root = Tk()
canv = Canvas(root, width=1000, height=800, bg='white')
canv.pack(fill=BOTH, expand=1)


class Ball:
    def __init__(self):  # СЃРѕР·РґР°РЅРёРµ С€Р°СЂРёРєР°
        self.x = 0
        self.y = 0
        self.Vx = 0
        self.Vy = 0
        self.Ax = 0
        self.Ay = 0


def yes(n):  # РЎРѕР·РґР°РЅРёРµ n С€Р°СЂРёРєРѕРІ
    for i in range(0, n):
        ball.append(Ball())


def start_from(x_0, y_0):
    for i in range(0, len(ball)):
        ball[i].x = (i + 1) * x_0  # РЅР°С‡Р°Р»СЊРЅС‹Рµ x РєРѕРѕСЂРґРёРЅР°С‚С‹ С€Р°СЂРёРєРѕРІ
        ball[i].y = y_0  # РЅР°С‡Р°Р»СЊРЅС‹Рµ y РєРѕРѕСЂРґРёРЅР°С‚С‹ С€Р°СЂРёРєРѕРІ
    

def move_ball():  # РЅРѕРІС‹Рµ РєРѕРѕСЂРґРёРЅР°С‚С‹ С€Р°СЂРёРєРѕРІ
    for i in range(0, len(ball)):
        ball[i].x += ball[i].Vx + ball[i].Ax
        ball[i].y += ball[i].Vy + ball[i].Ay


def acceleration(parameter, l_0, u):
    '''
    l_0 РґР»РёРЅР° РїСЂСѓР¶РёРЅС‹ РІ РЅРµСЂР°СЃС‚СЏРЅСѓС‚РѕРј СЃРѕСЃС‚РѕСЏРЅРёРё
    parameter = Р¶РµСЃС‚РєРѕСЃС‚СЊ/РјР°СЃСЃР°
    u СЃРєРѕСЂРѕСЃС‚СЊ РґРІРёР¶РµРЅРёСЏ С†РµРЅС‚СЂР°Р»СЊРЅРѕРіРѕ С€Р°СЂРёРєР°
    '''
    main_ball_num = len(ball) // 2
    for i in range(0, len(ball)):
        if i == 0:  # РєСЂР°Р№РЅРёР№ Р»РµРІС‹Р№ С€Р°СЂРёРє (РїРµСЂРІС‹Р№)
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
            ball[i].Ax = parameter * ((1 - l_0/l_12) * (x_2 - x_1) - (1 - l_0/l_01) * (x_1 - x_0))
            ball[i].Ay = parameter * ((l_12 - l_0) * (y_2 - y_1) / l_12 + (l_01 - l_0) * (y_1 - y_0) / l_01)
            # ball[i].Vx += ball[i].Ax
            # ball[i].Vy += ball[i].Ay
        if i == main_ball_num:
            ball[i].Vy = u
        if i > main_ball_num and i != len(ball) - 1:  # РІСЃРµ РѕСЃС‚Р°Р»СЊРЅС‹Рµ
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
        if i == len(ball) - 1:  # РєСЂР°Р№РЅРёР№ РїСЂР°РІС‹Р№ (РїРѕСЃР»РµРґРЅРёР№ С€Р°СЂРёРє)
            x_0 = ball[i - 1].x
            y_0 = ball[i - 1].y
            x_1 = ball[i].x
            y_1 = ball[i].y
            l_01 = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
            # alpha_12 = math.asin((x_1 - x_0) / l_01)
            ball[i].Ax = parameter * (1 - l_0/l_01) * (x_0 - x_1)
            ball[i].Ay = parameter * (1 - l_0/l_01) * (y_0 - y_1)
            # ball[i].Vx += ball[i].Ax
            # ball[i].Vy += ball[i].Ay 


def rendering():  # РѕС‚СЂРёСЃРѕРІРєР° Р»РёРЅРёРё
    for i in range(0, len(ball) - 1):
        canv.create_line(ball[i].x, ball[i].y, ball[i + 1].x, ball[i + 1].y)
        canv.create_oval(ball[i].x, ball[i].y-2.5, ball[i].x + 5, ball[i].y + 2.5)
    canv.create_oval(ball[len(ball) - 1].x, ball[len(ball) - 1].y-2.5, ball[len(ball) - 1].x + 5, ball[len(ball) - 1].y + 2.5)


def modeling():
    canv.delete("all")
    acceleration(0.05, 20, 1)
    move_ball()
    rendering()
    root.after(50, modeling)


ball = []
yes(41)
start_from(20, 10)
modeling()

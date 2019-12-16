from tkinter import *
import math
import time

root = Tk()
root.geometry('10000x700')
canv = Canvas(root, width=800, height=600, bg='white')
canv.pack(fill=BOTH, expand=1)

class Point:
    def __init__(self):  # класс шарика
        self.x = 0
        self.y = 0
        self.z = 0
        self.Vx = 0
        self.Vy = 0
        self.Vz = 0


def line_masiv(n):  # Создание n нитей без шариков, создание двумерного масива
    for i in range(n):
        membrane.append([])
        
def zapolnenie_membrane(m): # на каждую нити создается по m шариков
    from i in range(m):
        masiv = []
        from j in range(m):
            masiv.append(Point())   
        membrane[i] = masiv



def entry_conditions (x_0, y_0, y_0, Vx_0, Vy_0, Vz_0):
    '''
    initial conditions (coordinates and scorti) for each point
    '''
    for i in range(len(membrane) - 1):
        from j in range(len(membrane[i]):            
            membrane[i][j].x = i * x_0
            membrane[i][j].y = j * y_0
            membrane[i][j].y = z_0
            membrane[i][j].Vx = Vx_0
            membrane[i][j].Vy = Vy_0
            membrane[i][j].Vz = Vz_0


def centrel(V_cx, V_cy, V_cz, i_c, j_c):
    membrane[i_c - 1][j_c - 1].Vx = V_cx
    membrane[i_c - 1][j_c - 1].Vy = V_cy
    membrane[i_c - 1][j_c - 1].Vz = V_cz


def move_point():
    for i in range(len(membrane) - 1):
        from j in range(len(membrane[i]):            
            membrane[i][j].x += Vx
            membrane[i][j].y += Vy
            membrane[i][j].y += Vz

def acceleration(parameter, l_0):
    '''
    l_0 is the length of the spring in the unstretched condition 
    parameter = stiffness / mass
    '''
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            c = membrane[i][j]
            b = c
            l = c
            t = c
            r = c
            if i == 0 and j == 0: 
                b = c
                b.x += l_0
                l = c
                l.x += l_0
                r = membrane[i][j+1]
                t = membrane[i+1][j]
            elif j == 0 and i != 0 and i != len(membrane):
                c = membrane[i][j] 
                b = c
                b.x += l_0
                r = membrane[i][j+1]
                l = membrane[i][j-1]
                t = membrane[i+1][j]
            elif  j == 0 and i == len(membrane):
                b = c
                b.x += l_0
                r = c
                r.x += l_0
                l = membrane[i][j-1]
                t = membrane[i+1][j]
            elif i == len(membrane) and j != len(membrane[i]) and j != 0:
                r = c
                r.x += l_0
                b = membrane[i][j+1]
                l = membrane[i][j-1]
                t = membrane[i+1][j]
            elif i == len(membrane) and j == len(membrane[i]): 
                r = c
                r.x += l_0
                t = c
                t.x += l_0
                b = membrane[i][j+1]
                l = membrane[i][j-1]
            elif i != len(membrane) and i != 0 and j == len(membrane[i]):
                t = c
                t.x += l_0
                r = membrane[i][j+1]
                b = membrane[i][j+1]
                l = membrane[i][j-1]
            elif i == 0 and j == len(membrane[i]):
                t = c
                t.x += l_0
                l = c
                l.x += l_0
                r = membrane[i][j+1]
                b = membrane[i][j+1]
            elif i == 0 and j != len(membrane[i]) and j != 0: 
                l = c
                l.x += l_0
                r = membrane[i][j+1]
                b = membrane[i][j+1]
                t = membrane[i+1][j]
            elif i != i_c and j != j_c:
                b = membrane[i][j+1]
                t = membrane[i+1][j]
                l = membrane[i][j-1]
                r = membrane[i][j+1]
            else:
                b, l, r, t = c # так можно?
                b, l, r, t += l_0   
            environment = []
            environment.append(r)
            environment.append(l)
            environment.append(t)
            environment.append(b)
            for k in range(len(environment)):
                length = math.sqrt((environment[k].x - c.x) ** 2 + (environment[k].y - c.y) ** 2 + (environment[k].z - c.z)**2))
                gamma = parameter * (1 - l_0 / length)
                c.Vx += gamma * (environment[k].x - c.x) 
                c.Vy += gamma * (environment[k].y - c.y)
                c.Vx += gamma * (environment[k].z - c.z)

def modeling():
    move_point()
    acceleration(parameter, l_0)
    root.after(10, modeling)

membrane = []
line_masiv(n)
zapolnenie_membrane(m)
entry_conditions (x_0, y_0, y_0, Vx_0, Vy_0, Vz_0)
centrel(V_cx, V_cy, V_cz, i_c, j_c)
modeling()

root.mainloop()

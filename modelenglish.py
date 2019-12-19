from tkinter import Tk, Canvas, BOTH

import math

import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D



root = Tk()

root.geometry('1000x700')

canv = Canvas(root, width=800, height=600, bg='white')

canv.pack(fill=BOTH, expand=1)





class Point:

    """

    Class of joints (further called points) of the membrane

    """

    def __init__(self):

        """

    x, y, z -- coordinates of a junction

    vx, vy, vz -- velocity projections of a junction

        """

        self.x = 0

        self.y = 0

        self.z = 0

        self.vx = 0

        self.vy = 0

        self.vz = 0





def line_array(n):  # Создание n нитей без шариков

    for i in range(n):

        membrane.append([])

        

def membrane_filling(n, m): # Создание m шариков на каждой нити

    for i in range(n):

        array = []

        for j in range(m):

            array.append(Point())   

        membrane[i] = array





def line_image(n):  # Создание "пустого" образа мебраны

    for i in range(n):

        image.append([])


def image_filling(n, m): # Заполнение образа мембраны

    for i in range(n):

        array = []

        for j in range(m):

            array.append(Point())   

        image[i] = array


def initial_conditions (x_0, y_0, z_0, vx_0, vy_0, vz_0):

    '''

    initial conditions (coordinates and velocities) for each point

    '''

    for i in range(len(membrane)):

        for j in range(len(membrane[i])):

            membrane[i][j].x = (i+1) * x_0 + 150

            membrane[i][j].y = (j+1) * y_0 + 250

            membrane[i][j].z = z_0 + 150

            membrane[i][j].vx = vx_0

            membrane[i][j].vy = vy_0

            membrane[i][j].vz = vz_0



def central(v_cx, v_cy, v_cz, i_c, j_c):

    membrane[i_c - 1][j_c - 1].vx = v_cx

    membrane[i_c - 1][j_c - 1].vy = v_cy

    membrane[i_c - 1][j_c - 1].vz = v_cz





def move_point():

    for i in range(len(membrane)):

        for j in range(len(membrane[i])):            

            membrane[i][j].x += membrane[i][j].vx

            membrane[i][j].y += membrane[i][j].vy

            membrane[i][j].z += membrane[i][j].vz



def acceleration(parameter, l_0, i_c, j_c):

    '''

    l_0 is the distance between points in equilibrum 

    parameter = stiffness / mass

    '''

    for i in range(len(membrane)):

        for j in range(len(membrane[i])):

            if i == 0 and j == 0:

                c = membrane[i][j] # c - central point

                b = Point() # b - bottom point

                b.x, b.y, b.z = c.x + l_0, c.y, c.z

                r = Point() # r - right point

                r.x, r.y, r.z = c.x - l_0, c.y, c.z

                l = membrane[i+1][j] # l - left point

                t = membrane[i][j+1]# t - top point

            elif j == 0 and i != 0 and i != len(membrane) - 1:

                c = membrane[i][j]

                b = Point()

                b.x, b.y, b.z = c.x + l_0, c.y, c.z

                r = membrane[i-1][j]

                l = membrane[i+1][j]

                t = membrane[i][j+1]

            elif  j == 0 and i == len(membrane) - 1:

                c = membrane[i][j]

                b = Point()

                b.x, b.y, b.z = c.x + l_0, c.y, c.z

                l = Point()

                l.x, l.y, l.z = c.x + l_0, c.y, c.z

                r = membrane[i-1][j]

                t = membrane[i][j+1]

            elif i == len(membrane) - 1 and j != len(membrane[i]) - 1 and j != 0:

                c = membrane[i][j]

                l = Point()

                l.x, l.y, l.z = c.x + l_0, c.y, c.z

                b = membrane[i][j-1]

                r = membrane[i-1][j]

                t = membrane[i][j-1]

            elif i == len(membrane) - 1 and j == len(membrane[i]) - 1:

                c = membrane[i][j]

                l = Point()

                l.x, l.y, l.z = c.x + l_0, c.y, c.z

                t = Point()

                t.x, t.y, t.z = c.x + l_0, c.y, c.z

                b = membrane[i][j-1]

                r = membrane[i-1][j]

            elif i != len(membrane) - 1 and i != 0 and j == len(membrane[i]) - 1:

                c = membrane[i][j]

                t = Point()

                t.x, t.y, t.z = c.x + l_0, c.y, c.z

                r = membrane[i-1][j]

                b = membrane[i][j-1]

                l = membrane[i+1][j]

            elif i == 0 and j == len(membrane[i]) - 1:

                c = membrane[i][j]

                t = Point()

                t.x, t.y, t.z = c.x + l_0, c.y, c.z

                r = Point()

                r.x, r.y, r.z = c.x + l_0, c.y, c.z

                l = membrane[i+1][j]

                b = membrane[i][j-1]

            elif i == 0 and j != len(membrane[i]) - 1 and j != 0:

                c = membrane[i][j]

                r = Point()

                r.x, r.y, r.z = c.x + l_0, c.y, c.z

                l = membrane[i+1][j]

                b = membrane[i][j-1]

                t = membrane[i][j+1]

            elif i == i_c - 1 and j == j_c - 1:

                c = membrane[i][j]

                l = Point()

                l.x, l.y, l.z = c.x + l_0, c.y, c.z

                t = Point()

                t.x, t.y, t.z = c.x + l_0, c.y, c.z

                r = Point()

                r.x, r.y, r.z = c.x + l_0, c.y, c.z

                b = Point()

                b.x, b.y, b.z = c.x + l_0, c.y, c.z

            else:

                c = membrane[i][j]

                b = membrane[i][j-1]

                t = membrane[i][j+1]

                l = membrane[i+1][j]

                r = membrane[i-1][j]

            neighbours = []

            neighbours.append(r)

            neighbours.append(l)

            neighbours.append(t)

            neighbours.append(b)


            for k in range(len(neighbours)):

                length = math.sqrt((neighbours[k].x - c.x) ** 2 + (neighbours[k].y - c.y) ** 2 + (neighbours[k].z - c.z)**2)

                if length != 0:

                    gamma = parameter * (1 - l_0 / length)

                    c.vx += gamma * (neighbours[k].x - c.x) 

                    c.vy += gamma * (neighbours[k].y - c.y)

                    c.vz += gamma * (neighbours[k].z - c.z)

                    
                    



def rendering(): # отрисовка мембраны

    for i in range(len(image)):

        for j in range(0, len(image[i]) - 1):

            canv.create_line(image[i][j].x, image[i][j].y, image[i][j+1].x, image[i][j+1].y)

        for j in range(len(image[i])):

            for i in range(len(image) - 1):

                canv.create_line(image[i][j].x, image[i][j].y, image[i+1][j].x, image[i+1][j].y)


def rotation(ux, uy, uz):

     for i in range(len(membrane)):

        for j in range(len(membrane[i])):

            a = Point()

            b = Point()

            c = Point()

            a.x = membrane[i][j].x

            a.y = membrane[i][j].y

            a.z = membrane[i][j].z            

            b.x = a.x

            b.y = np.cos(ux) * a.y - np.sin(ux)* a.z

            b.z = np.cos(ux) * a.z + np.sin(ux)* a.y

            c.x = b.x * np.cos(uy) + b.z * np.sin(uy)

            c.y = b.y

            c.z = b.z * np.cos(uy) - b.x * np.sin(uy)

            image[i][j].x = c.x * np.cos(uz) - c.y * np.sin(uz)

            image[i][j].y = c.z * np.cos(uz) + c.y * np.sin(uz)

            image[i][j].z = c.z


def modeling():

    canv.delete("all")

    central(0, 0, 0.25, 4, 4)

    move_point()

    acceleration(0.7, 90, 4, 4)

    rotation(0.3, 0.4, 0.1)

    rendering()

    root.after(20, modeling)





membrane = []

image = []

line_image(7)

image_filling(7, 7)

line_array(7)

membrane_filling(7, 7)

initial_conditions(90, 90, 90, 0, 0, 0)

modeling()

root.mainloop()

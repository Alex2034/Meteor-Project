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
    Class of junctions (further called points) of the web
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


def starting_lines(n):
    """
    Creates n parallel "strings" in a list membrane
    """
    for i in range(n):
        membrane.append([])


def filling_web(n, m):
    """
    Creates points between strings as class Point objects
    """
    for i in range(n):
        for j in range(m):
            membrane[i].append(Point())


def entry_conditions(x_0, y_0, z_0, vx_0, vy_0, vz_0):
    """
    initial conditions (coordinates and velocities) for each joint
    """
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            membrane[i][j].x = (i + 1) * x_0 + 50
            membrane[i][j].y = (j + 1) * y_0 + 50
            membrane[i][j].z = z_0 + 50
            membrane[i][j].vx = vx_0
            membrane[i][j].vy = vy_0
            membrane[i][j].vz = vz_0


def central(v_cx, v_cy, v_cz, i_c, j_c):
    membrane[i_c - 1][j_c - 1].vx = v_cx
    membrane[i_c - 1][j_c - 1].vy = v_cy
    membrane[i_c - 1][j_c - 1].vz = v_cz


def move_point():
    """
    makes points move
    """
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):            
            membrane[i][j].x += membrane[i][j].vx
            membrane[i][j].y += membrane[i][j].vy
            membrane[i][j].z += membrane[i][j].vz


def acceleration(parameter, l_0, i_c, j_c):
    """
    describes the movement of points
    :param parameter: stiffness of the string divided by mass of a point
    :param l_0: length of an unstretched string between two points
    :param i_c:
    :param j_c:
    """
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            if i == 0 and j == 0:
                c = membrane[i][j]
                b = Point()
                b.x, b.y, b.z = c.x + l_0, c.y, c.z
                r = Point()
                r.x, r.y, r.z = c.x - l_0, c.y, c.z
                l = membrane[i+1][j]
                t = membrane[i][j+1]
            elif j == 0 and i != 0 and i != len(membrane) - 1:
                c = membrane[i][j]
                b = Point()
                b.x, b.y, b.z = c.x + l_0, c.y, c.z
                r = membrane[i-1][j]
                l = membrane[i+1][j]
                t = membrane[i][j+1]
            elif j == 0 and i == len(membrane) - 1:
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

            environment = [r, l, t, b]

            for k in range(len(environment)):
                length = math.sqrt((environment[k].x - c.x) ** 2 +
                                   (environment[k].y - c.y) ** 2 + (environment[k].z - c.z)**2)
                gamma = parameter * (1 - l_0 / length)
                c.vx += gamma * (environment[k].x - c.x)
                c.vy += gamma * (environment[k].y - c.y)
                c.vz += gamma * (environment[k].z - c.z)


def rendering():  # отрисовка линии
    for i in range(len(membrane)):
        for j in range(0, len(membrane[i]) - 1):
            canv.create_line(membrane[i][j].x, membrane[i][j].y, membrane[i][j + 1].x, membrane[i][j + 1].y)
        for j in range(len(membrane[i])):
            for i in range(len(membrane) - 1):
                canv.create_line(membrane[i][j].x, membrane[i][j].y, membrane[i + 1][j].x, membrane[i + 1][j].y)


def graph():
    x = np.array([])
    y = np.array([])
    z = np.array([])
    s = np.array([])
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            x.np.append(membrane[i][j].x)
            y.np.append(membrane[i][j].y)
            z.np.append(membrane[i][j].z)
            s.np.append(2)
    print(x, y, z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_wireframe(x, y, z)
    plt.show()


def rotation(ux, uy, uz):
    for i in range(len(membrane)):
        for j in range(len(membrane[i])):
            """
            membrane[i][j].x = membrane[i][j].x * (np.cos(uz) * np.cos(uy) + membrane[i][j].y * np.sin(uz) * np.cos(uy) 
            - membrane[i][j].z * np.sin(uy))
            membrane[i][j].y = membrane[i][j].x * (np.cos(uz) * np.sin(uy) * np.sin(ux) - 
            membrane[i][j].y * np.sin(uz) * np.cos(ux) + membrane[i][j].z * np.sin(uz) * np.sin(uy) * np.sin(ux) + 
            np.cos(uz) * np.cos(ux) + np.cos(uy) * np.sin(ux))
            membrane[i][j].z = membrane[i][j].x * (np.cos(uz) * np.sin(uy) * np.cos(ux) + 
            membrane[i][j].y * np.sin(uz) * np.sin(ux) + membrane[i][j].z * np.sin(uz) * np.sin(uy) * np.cos(ux)
            - np.cos(uz) * np.sin(ux) + np.cos(uy) * np.cos(ux))
            """
            a = Point()
            b = Point()
            c = Point()
            a.x = membrane[i][j].x
            a.y = membrane[i][j].y
            a.z = membrane[i][j].z
            
            b.x = a.x
            b.y = np.cos(ux) * a.y - np.sin(ux) * a.z
            b.z = np.cos(ux) * a.z + np.sin(ux) * a.y
            c.x = b.x * np.cos(uy) + b.z * np.sin(uy)
            c.y = b.y
            c.z = b.z * np.cos(uy) - b.x * np.sin(uy)
            membrane[i][j].x = c.x * np.cos(uz) - c.y * np.sin(uz)
            membrane[i][j].y = c.z * np.cos(uz) + c.y * np.sin(uz)
            membrane[i][j].z = c.z

            """
            membrane[i][j].x *= (np.cos(uz) + np.sin(uz)) * (np.cos(uy) - np.sin(uy))
            membrane[i][j].y *= (np.cos(uz) - np.sin(uz)) * (np.cos(ux) + np.sin(ux))
            membrane[i][j].z *= (np.cos(uy) + np.sin(uy)) * (np.cos(ux) - np.sin(ux))
            """


def modeling():
    canv.delete("all")
    central(0, 0, 0.25, 4, 4)
    move_point()
    acceleration(0.7, 90, 4, 4)
    rotation(0, 0.5, 0)
    rendering()
    root.after(20, modeling)


membrane = []
membrane = []
starting_lines(7)
filling_web(7, 7)
entry_conditions(90, 90, 90, 0, 0, 0)
modeling()
graph()
root.mainloop()

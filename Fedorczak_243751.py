#!/usr/bin/env python3
import sys

# Lista pakietów wraz z wersją wykorzystanych w projekcie (pobrane za pomocą narzędzia PIP3)
# bandit==1.6.2
# flake8==3.8.4
# gitdb==4.0.5
# GitPython==3.1.10
# glfw==2.0.0
# mccabe==0.6.1
# numpy==1.19.2
# pbr==5.5.1
# pycodestyle==2.6.0
# pyflakes==2.2.0
# PyOpenGL==3.1.5
# PyYAML==5.3.1
# scipy==1.5.3
# six==1.15.0
# smmap==3.0.4
# stevedore==3.2.2



from glfw.GLFW import *
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from random import random

global N
global matrix1
global matrix2
N = 22
matrix1 = np.zeros((N,N,3))
matrix2 = np.zeros((N,N,3))

def generate_matrix(matrix1):
    u = [i / (N - 1) for i in range(0,N)]
    v = [i / (N - 1) for i in range(0,N)]

    for i in range(0, N):
        for j in range(0, N):
            matrix1[i][j][0] = (-90 * u[i]**5 + 225 * u[i]**4 - 270 * u[i]**3 + 180 * u[i]**2 - 45 * u[i])*np.cos(np.pi * v[j])
            matrix1[i][j][1] = (160 * u[i]**4 - 320 * u[i]**3 + 160 * u[i]**2)
            matrix1[i][j][2] = (-90 * u[i]**5 + 225 * u[i]**4 - 270 * u[i]**3 + 180 * u[i]**2 - 45 * u[i])*np.sin(np.pi * v[j])
            for k in range(3):
                matrix2[i][j][k] = random()

def show_data_matrix(matrix1):
    print(matrix1)
def show_color_matrix(matrix1):
    print(matrix2)


def startup():
    global matrix1
    generate_matrix(matrix1)
    update_viewport(None, 400, 400)
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)



def shutdown():
    pass

def spin(angle):
    glRotatef(angle, 1.0, 0.0, 0.0)
    glRotatef(angle, 0.0, 1.0, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)

def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)

    glEnd()





def zad30():
    for i in range(N):
        for j in range(N):
            glColor3f(0.5, 0.7, 1.0)
            glBegin(GL_POINTS)
            glVertex3f(matrix1[i][j][0], matrix1[i][j][1], matrix1[i][j][2])
            glEnd()



def zad35():
    glColor3f(1, 0.5, 1)
    for i in range(N - 1):
        for j in range(N - 1):
            glBegin(GL_LINES)
            glVertex3f(matrix1[i][j][0], matrix1[i][j][1], matrix1[i][j][2])
            glVertex3f(matrix1[i][j + 1][0], matrix1[i][j + 1][1], matrix1[i][j + 1][2])
            glEnd()

            glBegin(GL_LINES)
            glVertex3f(matrix1[i][j][0], matrix1[i][j][1], matrix1[i][j][2])
            glVertex3f(matrix1[i + 1][j][0], matrix1[i + 1][j][1], matrix1[i + 1][j][2])
            glEnd()



def zad40():
    for i in range(N - 1):
        for j in range(N - 1):
            glBegin(GL_TRIANGLES)
            glColor3f(matrix2[i][j][0], matrix2[i][j][1], matrix2[i][j][2])
            glVertex3f(matrix1[i][j][0], matrix1[i][j][1], matrix1[i][j][2])
            glColor3f(matrix2[i + 1][j][0], matrix2[i + 1][j][1], matrix2[i + 1][j][2])
            glVertex3f(matrix1[i + 1][j][0], matrix1[i + 1][j][1], matrix1[i + 1][j][2])
            glColor3f(matrix2[i][j+1][0], matrix2[i][j+1][1], matrix2[i][j+1][2])
            glVertex3f(matrix1[i][j+1][0], matrix1[i][j+1][1], matrix1[i][j+1][2])
            glEnd()

            glBegin(GL_TRIANGLES)
            glColor3f(matrix2[i][j+1][0], matrix2[i][j+1][1], matrix2[i][j+1][2])
            glVertex3f(matrix1[i][j+1][0], matrix1[i][j+1][1], matrix1[i][j+1][2])
            glColor3f(matrix2[i + 1][j + 1][0], matrix2[i + 1][j + 1][1], matrix2[i + 1][j + 1][2])
            glVertex3f(matrix1[i + 1][j + 1][0], matrix1[i + 1][j + 1][1], matrix1[i + 1][j + 1][2])
            glColor3f(matrix2[i+1][j][0], matrix2[i+1][j][1],matrix2[i+1][j][2])
            glVertex3f(matrix1[i+1][j][0], matrix1[i+1][j][1], matrix1[i+1][j][2])
            glEnd()


def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    
    axes()
    spin(time *180/np.pi)

    #zad na 3.0
    #zad30()
    #zad na 3.5
    #zad35()
    #zad na 4.0
    #zad40()

    glFlush()


def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-12.5, 12.5, -12.5 / aspect_ratio, 12.5 / aspect_ratio, 12.5, -12.5)
    else:
        glOrtho(-12.5 * aspect_ratio, 12.5 * aspect_ratio, -12.5, 12.5, 12.5, -12.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def main():
    if not glfwInit():
        sys.exit(-1)

    window = glfwCreateWindow(400, 400, __file__, None, None)
    if not window:
        glfwTerminate()
        sys.exit(-1)
    

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSwapInterval(1)

    startup()
    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()
    shutdown()

    glfwTerminate()


if __name__ == '__main__':
    main()

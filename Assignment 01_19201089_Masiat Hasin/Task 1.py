from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random

def init():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    init()
    draw()
    glutSwapBuffers()

def draw():
    glColor3f(0.0, 1.0, 1.0)
    glPointSize(5)

    for i in range(50):
        x = random.randint(5, 495)
        y =random.randint(5, 495)
        glBegin(GL_POINTS)
        glVertex2f(x,y)
        glEnd()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Task 1: Drawing Pixels")
glutDisplayFunc(showScreen)
glutMainLoop()
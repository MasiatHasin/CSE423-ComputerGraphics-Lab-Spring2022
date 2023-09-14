from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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
    glLineWidth(2)

    glBegin(GL_LINES)
    #Roof
    glColor3f(0.0, 0.5, 1.0)
    glVertex2f(250, 400)
    glVertex2f(150, 250)

    glVertex2f(250, 400)
    glVertex2f(350, 250)

    glVertex2f(150, 250)
    glVertex2f(350, 250)

    #Wall
    glColor3f(0.0, 0.5, 1.0)
    glVertex2f(150, 250)
    glVertex2f(150, 50)

    glVertex2f(350, 250)
    glVertex2f(350, 50)

    glVertex2f(150, 50)
    glVertex2f(350, 50)

    #Left Window
    glColor3f(2.0, 0.5, 1.0)
    glVertex2f(170, 220)
    glVertex2f(220, 220)

    glVertex2f(170, 220)
    glVertex2f(170, 170)

    glVertex2f(220, 220)
    glVertex2f(220, 170)

    glVertex2f(170, 170)
    glVertex2f(220, 170)

    #Right Window
    glVertex2f(280, 220)
    glVertex2f(330, 220)

    glVertex2f(280, 220)
    glVertex2f(280, 170)

    glVertex2f(330, 220)
    glVertex2f(330, 170)

    glVertex2f(280, 170)
    glVertex2f(330, 170)

    #Door
    glColor3f(2.0, 0.5, 1.0)
    glVertex2f(230, 50)
    glVertex2f(230, 125)

    glVertex2f(270, 50)
    glVertex2f(270, 125)

    glVertex2f(230, 125)
    glVertex2f(270, 125)
    glEnd()

    # Door Knob
    glColor3f(0.0, 0.5, 1.0)
    glPointSize(5)
    glBegin(GL_POINTS)
    glVertex2f(260, 85)
    glEnd()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Task 2: House Building")
glutDisplayFunc(showScreen)
glutMainLoop()
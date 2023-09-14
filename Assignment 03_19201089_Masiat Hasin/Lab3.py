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
    main()
    glutSwapBuffers()

def findZone(x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    zone = 0

    if abs(dx)>abs(dy):
        if dx>0 and dy>0:
            zone = 0
        elif dx<0 and dy>0:
            zone = 3
        elif dx>0 and dy<0:
            zone = 7
        elif dx<0 and dy<0:
            zone = 4
    elif abs(dx)<abs(dy):
        if dx>0 and dy>0:
            zone = 1
        elif dx<0 and dy>0:
            zone = 2
        elif dx>0 and dy<0:
            zone = 6
        elif dx<0 and dy<0:
            zone = 5

    return zone

def convert2zone(x,y,zone):
    if zone==0:
        X = y
        Y = x

    if zone == 1:
        X = x
        Y = y

    elif zone == 2:
        X = -x
        Y = y

    elif zone == 3:
        X = -y
        Y = x

    elif zone == 4:
        X = -y
        Y = -x

    elif zone == 5:
        X = -x
        Y = -y

    elif zone == 6:
        X = x
        Y = -y

    elif zone == 7:
        X = y
        Y = -x

    return X,Y

def MidPointCircle(r,x1=0,y1=0):
    d = 1-r
    x = 0
    y = r
    while x<y:
        for i in range(0,8,1):
            X, Y = convert2zone(x, y, i)
            glBegin(GL_POINTS)
            glVertex2f(X+250+x1, Y+250+y1)
            glEnd()
        if d>=0:
            #SE
            d = d+(2*x)-(2*y)+5
            x+=1
            y-=1
        else:
            #E
            d = d+(2*x)+3
            x+=1
        glBegin(GL_POINTS)
        glVertex2f(x+250+x1, y+250+y1)
        glEnd()

def main():
    glColor3f(0.5, 1.0, 0.5)
    glPointSize(2)
    MidPointCircle(200)
    MidPointCircle(100,0,100)
    MidPointCircle(100,0,-100)
    MidPointCircle(100, 100, 0)
    MidPointCircle(100, -100, 0)
    MidPointCircle(100, -70.71, 70.71)
    MidPointCircle(100, 70.71, 70.71)
    MidPointCircle(100, 70.71, -70.71)
    MidPointCircle(100, -70.71, -70.71)

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Lab3- 19201089")
glutDisplayFunc(showScreen)
glutMainLoop()
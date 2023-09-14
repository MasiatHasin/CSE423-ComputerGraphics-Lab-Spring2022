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
    X = 0
    Y = 0

    if zone==0:
        X = x
        Y = y

    if zone == 1:
        X = y
        Y = x

    elif zone == 2:
        X = y
        Y = -x

    elif zone == 3:
        X = -x
        Y = y

    elif zone == 4:
        X = -x
        Y = -y

    elif zone == 5:
        X = -y
        Y = -x

    elif zone == 6:
        X = -y
        Y = x

    elif zone == 7:
        X = x
        Y = -y

    return X,Y

def originalZone(x,y,zone):
    X = 0
    Y = 0

    if zone==0:
        X = x
        Y = y

    elif zone == 1:
        X = y
        Y = x

    elif zone == 2:
        X = -y
        Y = x

    elif zone == 3:
        X = -x
        Y = y

    elif zone == 4:
        X = -x
        Y = -y

    elif zone == 5:
        X = -y
        Y = -x

    elif zone == 6:
        X = y
        Y = -x

    elif zone == 7:
        X = x
        Y = -y

    return X, Y

def midpoint(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1

    d = 2*dy - dx

    zone = findZone(x1, y1, x2, y2)
    x1, y1 = convert2zone(x1, y1, zone)
    x2, y2 = convert2zone(x2, y2, zone)

    if x1==x2:
        while y1!=y2:
            glBegin(GL_POINTS)
            glVertex2f(x1, y1)
            glEnd()
            y1+=1

    else:
        while x1 != x2 or y1 != y2:
            x1, y1 = originalZone(x1, y1, zone)
            glBegin(GL_POINTS)
            glVertex2f(x1, y1)
            glEnd()

            if d >= 0:
                d = d + 2*dy - 2*dx
                x1 += 1
                y1 += 1
            else:
                d = d + 2*dy
                x1 += 1
def main():
    glColor3f(0.5, 1.0, 0.5)
    glPointSize(4)

    # 8
    midpoint(140, 325, 240, 325)  # -1
    midpoint(140, 250, 240, 250)  # -2
    midpoint(140, 175, 240, 175)  # -3
    midpoint(140, 175, 140, 325)  # |1
    midpoint(240, 175, 240, 325)  # |2

    # 9
    midpoint(260, 325, 360, 325)  # -1
    midpoint(260, 250, 360, 250)  # -2
    midpoint(260, 175, 360, 175)  # -3
    midpoint(260, 250, 260, 325)  # |-1
    midpoint(360, 175, 360, 325)  # |-2

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Lab2- Student ID: 19201089, Drawing- 89")
glutDisplayFunc(showScreen)
glutMainLoop()
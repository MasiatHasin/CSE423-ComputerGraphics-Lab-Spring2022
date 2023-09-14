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
    glColor3f(1.0, 1.0, 0.0)
    if int(id) % 2 == 0:
        result = "even"
    else:
        result = "odd"
    if result=="odd":
        DDADot(200, 175, 200, 325)
        DDA(200, 250, 300, 250)
        DDA(300, 175, 300, 325)

    else:
        DDADot(175, 325, 325, 325)
        DDA(250, 175, 250, 325)

def drawPoints(x,y):
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(round(x), round(y))
    glEnd()

def DDA(x0,y0,x1,y1):
    dx = x1-x0;
    dy = y1-y0;

    if abs(dx)>abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xi = dx/int(steps)
    yi = dy/int(steps)

    for i in range(0, steps, 1):
        x0 += xi
        y0 += yi
        drawPoints(round(x0),round(y0))

def DDADot(x0,y0,x1,y1):
    dx = x1-x0;
    dy = y1-y0;

    if abs(dx)>abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xi = dx/int(steps)
    yi = dy/int(steps)

    draw = 6
    draw2 = 0
    for i in range(0, steps, 1):
        x0 += xi
        y0 += yi
        draw += 1
        if draw>=6:
            drawPoints(x0, y0)
            draw2+=1
            if draw2>=2:
                draw = 0
                draw2=0

id = input("Student ID: ")
print("\nPlease look at Coin Toss Window for result")
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Task 3: Coin Toss")
glutDisplayFunc(showScreen)
glutMainLoop()
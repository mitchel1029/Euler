from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import serial
import os
import threading
from BeeldVerwerking import BeeldVerwerking

ESCAPE = '\033'

window = 0

# rotation
X_AXIS = 0.0
Y_AXIS = 0.0
Z_AXIS = 0.0

DIRECTION = 1


def InitGL(Width, Height):
    global basePos, b
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

    b = BeeldVerwerking()
    basePos = [
        [1.5,1.0,1.0, 1.0],
        [1.5,-1.0,1.0, 1.0],
        [1.5,-1.0,-1.0, 1.0],
        [1.5,1.0,-1.0, 1.0],
        [-1.5, 1.0, 1.0, 1.0],
        [-1.5, -1.0, 1.0, 1.0],
        [-1.5, -1.0, -1.0, 1.0],
        [-1.5, 1.0, -1.0, 1.0]
    ]

def keyPressed(*args):
    if args[0] == ESCAPE:
        sys.exit()

def DrawGLScene():
    global X_AXIS, Y_AXIS, Z_AXIS, basePos, b
    global DIRECTION
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(0.0, 0.0, -10.0)
    # glRotate(Z_AXIS,0.5,2.0,1.0)

    pos = b.calcAll(basePos, 0, 0, Z_AXIS, [5, 2, -5])
    # pos = basePos
    print basePos
    print pos,  "\n"
    glBegin(GL_QUADS)

    for i in range(8):
        if i == 0:
            glColor3f(0.5, 1.0, 0.5)
        elif i == 4:
            glColor3f(1.0, 0.5, 0.5)
        glVertex3f(pos[i][0],pos[i][1],pos[i][2])

    for i in range(4):
        glColor3f(0.0, 1.0, i/4.0)
        glVertex3f(pos[i][0], pos[i][1], pos[i][2])
        glVertex3f(pos[(i+1)%4][0], pos[(i+1)%4][1], pos[(i+1)%4][2])
        glVertex3f(pos[(i+1)%4+4][0], pos[(i+1)%4+4][1], pos[(i+1)%4+4][2])
        glVertex3f(pos[i+4][0], pos[i+4][1], pos[i+4][2])

    glEnd()

    Z_AXIS = (Z_AXIS-0.2)%360

    glutSwapBuffers()

def main():
    global window

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1920, 1080)

    window = glutCreateWindow('OpenGL Python Cube')
    glutFullScreen()
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutKeyboardFunc(keyPressed)
    InitGL(1920, 1080)
    glutMainLoop()


if __name__ == "__main__":
    main()

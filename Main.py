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
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.0, float(Width) / float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def keyPressed(*args):
    if args[0] == ESCAPE:
        sys.exit()


def DrawGLScene():
    global X_AXIS, Y_AXIS, Z_AXIS
    global DIRECTION

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()
    glTranslatef(0.0, 0.0, -10.0)

    glRotatef(Z_AXIS, 0.0, 1.0, 1.0)

    # Draw Cube (multiple quads)

    glBegin(GL_QUADS)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.5)
    glVertex3f(-1.0, 1.0, -1.5)
    glVertex3f(-1.0, 1.0, 1.5)
    glVertex3f(1.0, 1.0, 1.5)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.5)
    glVertex3f(-1.0, -1.0, 1.5)
    glVertex3f(-1.0, -1.0, -1.5)
    glVertex3f(1.0, -1.0, -1.5)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(1.0, 1.0, 1.5)
    glVertex3f(-1.0, 1.0, 1.5)
    glVertex3f(-1.0, -1.0, 1.5)
    glVertex3f(1.0, -1.0, 1.5)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.5)
    glVertex3f(-1.0, -1.0, -1.5)
    glVertex3f(-1.0, 1.0, -1.5)
    glVertex3f(1.0, 1.0, -1.5)

    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.5)
    glVertex3f(-1.0, 1.0, -1.5)
    glVertex3f(-1.0, -1.0, -1.5)
    glVertex3f(-1.0, -1.0, 1.5)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.5)
    glVertex3f(1.0, 1.0, 1.5)
    glVertex3f(1.0, -1.0, 1.5)
    glVertex3f(1.0, -1.0, -1.5)

    glEnd()

    Z_AXIS += 0.25

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
    b = BeeldVerwerking()
    b.calcAll([[1,1,1,1],[1,1,1,1]],90,180,0,[2,4,3])
    main()

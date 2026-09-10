from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
camera_pos=(0,200,200)
gm_over=False
score=0
speed=10
g=9.8
jump_power=9
velo=0
dino_y=0
delta_time=0.015
dino={"x": 50,"y": 0,"width": 40,"height": 50}
obstacle = {"x": 300,"y": 0,"width": 30,"height": 40}
def jump():
 global velo
 if dino_y<=0:
   velo=jump_power
def keyboard(key, x, y):
 if key==b' ':
  jump()
def collision(dino, obstacle):
 horizontal=(dino["x"]<obstacle["x"]+obstacle["width"] and dino["x"]+dino["width"]>obstacle["x"])
 vertical=(dino["y"]<obstacle["y"]+obstacle["height"] and dino["y"]+dino["height"]>obstacle["y"])
 return horizontal and vertical
def update():
 global velo, score, gm_over, dino_y
 if gm_over:
  return
velo-=g*delta_time
dino_y+=velo*delta_time
if dino_y<=0:
 dino_y=0
 velo=0
 dino["y"]=dino_y
 obstacle["x"]-=speed*delta_time
if collision(dino,obstacle):
 gm_over=True
 print("Game Over")
def game_over():
 return gm_over
def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    iterate()
    update()

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)

wind = glutCreateWindow(b"Dino Game")

glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboard)

glutMainLoop()
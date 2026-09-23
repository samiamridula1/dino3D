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
dino_x=60
dino_y=50
dino_width=40
dino_height=50
cactus_x=300
cactus_y=50
cactus_width=30
cactus_height=40
# dino={"x": 50,"y": 0,"width": 40,"height": 50}
# obstacle = {"x": 300,"y": 0,"width": 30,"height": 40}
def draw_points(x, y):
    # The parameter that is passed in the function dictates the size of the pixel.
    glPointSize(10)

    glBegin(GL_POINTS)

    # Think of this as a co-ordinate. At the given x and y position the pixel will be drawn.
    glVertex2f(x, y)

    glEnd()
def draw_rec(x,y,width,height):
  glBegin(GL_QUADS)
  glVertex2f(x,y)
  glVertex2f(x+width,y)
  glVertex2f(x+width,y+height)
  glVertex2f(x,y+height)
  glEnd()
def draw_dino():
  draw_rec(dino_x,dino_y,dino_width,dino_height) #body
  glColor3f(0.0,0.8,0.0)
  draw_rec(dino_x+10,dino_y+50,22,17)
  glColor3f(0.0,0.0,0.8) #eye
  draw_points(dino_x+25,dino_y+55)
def draw_cactus():
  draw_rec(cactus_x,cactus_y,cactus_width,cactus_height)
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
def drawQuads():
    glBegin(GL_QUADS)

    # The points have to be in anticlockwise order.
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(300, 300)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(400, 300)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(400, 100)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(300, 100)

    glEnd()
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
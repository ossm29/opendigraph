from PIL import Image, ImageDraw
import math
from datetime import datetime
from modules.open_digraph import *


random.seed(datetime.now())
WIDTH = 500
HEIGHT = 500
RADIUS = 25
POINTEUR = 50

class point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def __str__(self):
    return "(" + str(self.x) + ", " + str(self.y) + ")"
  def __repr__(self):
    return "point"+str(self)
  def n(self):# return a simple tuple of int
    return (round(self.x), round(self.y)) 
  def copy(self):
    return point(self.x, self.y)
  def __add__(self, p2):
    return point(self.x + p2.x, self.y + p2.y)
  def __rmul__(self, s):
    return point(s*self.x, s*self.y)
  def __sub__(self, p2):
    return point(self.x - p2.x, self.y - p2.y)
  def __eq__(self, p2):
    return (self.x == p2.x and self.y == p2.y)
  def rotate(self, theta, c):
    delta = math.sqrt((self.x - c.x)*(self.x - c.x) + (self.y - c.y)*(self.y - c.y))
    alpha = math.acos(abs(self.y - c.y)/delta)
    self.x = c.x + delta*math.cos(theta + alpha)
    self.y = c.y + delta*math.sin(theta + alpha)

def drawarrows(self, p1, p2):
  '''doc : todo'''
  self.line([p1.n(), p2.n()], 'black')
  theta = math.acos((p2.x - p1.x)/math.sqrt((p2.x - p1.x)*(p2.x - p1.x) + (p2.y - p1.y)*(p2.y - p1.y)))
  if p2.y < p1.y:
    theta = -theta
  r = 10.0
  alpha = math.pi/6

  t1 = point(p2.x - r*math.cos(theta + alpha), p2.y - r*math.sin(theta + alpha))
  t2 = point(p2.x - r*math.cos(theta - alpha), p2.y - r*math.sin(theta - alpha))
  self.line([t1.n(), p2.n()], 'black')
  self.line([t2.n(), p2.n()], 'black')

ImageDraw.ImageDraw.arrows = drawarrows # we define the method 'arrows'
                                          # from the function 'arrows' above

def drawnode(self, p, node, verbose=False):
  self.ellipse((p.x - RADIUS, p.y - RADIUS, p.x + RADIUS, p.y + RADIUS), fill='white', outline='red') 
  self.text((p.x - 6*len(node.label)/2,p.y - 6), node.label, fill='black')
  if verbose :
    self.text((p.x - 3,p.y + 12), str(node.id), fill='black')

ImageDraw.ImageDraw.node = drawnode

def drawgraph(self, g, node_pos,  input_pos, output_pos, method='manual'):
  '''doc : todo'''
  if(method=='manual'):
    for i in range(len(input_pos)):
      self.arrows(input_pos[i], point(node_pos[g.get_input_ids()[i]].x - (node_pos[g.get_input_ids()[i]].x - input_pos[i].x)*RADIUS/POINTEUR, (node_pos[g.get_input_ids()[i]].y - (node_pos[g.get_input_ids()[i]].y - input_pos[i].y)*RADIUS/POINTEUR)))
    for i in range(len(output_pos)):
      self.arrows(node_pos[g.get_output_ids()[i]], output_pos[i])
    for n in g.get_nodes():
      self.node(node_pos[n.get_id()], n, verbose=True)
  if(method =='random'):
    np,ip,op = random_layout(g)
    self.graph(g,np,ip,op,method='manual')

ImageDraw.ImageDraw.graph = drawgraph

def random_layout(g): #
  node_pos = {}
  input_pos = []
  output_pos = []  
  tuplist = [(i + 50,j + 50) for i in range(WIDTH - 100) for j in range(HEIGHT - 100)]
  tirage = random.sample(tuplist,len(g.get_nodes()))
  tmp = 0
  for node in g.get_nodes():
    node_pos[node.get_id()] = point(tirage[tmp][0],tirage[tmp][1])
    tmp+=1
  for node in g.get_input_ids():
    x = random.uniform(-1,1)
    n = random.choice([-1,1])
    y = POINTEUR*n*math.sqrt(1-x*x)
    x *= POINTEUR
    input_pos.append(point(x+node_pos[node].x ,y+node_pos[node].y))
  for node in g.get_output_ids():
    x = random.uniform(-1,1)
    n = random.choice([-1,1])
    y = POINTEUR*n*math.sqrt(1-x*x)
    x *= POINTEUR
    output_pos.append(point(x+node_pos[node].x ,y+node_pos[node].y))

  return node_pos,input_pos,output_pos






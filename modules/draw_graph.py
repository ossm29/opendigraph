#Oussama Konate et Thomas Delépine

from PIL import Image, ImageDraw
import math
from datetime import datetime
from modules.open_digraph import *


random.seed(datetime.now())
WIDTH = 500
HEIGHT = 500
RADIUS = 25 #rayon du cercle présentant les noeuds
POINTEUR = 50 #taille des fleches qui pointent les inputs/outputs
START = 125 #coordonnée en x et y du point de départ du cercle de circle_layout
FLECHE = 10 #taille de la pointe de la fleche
ECART = 20 #ecart entre 2 courbes de bezier

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
def rotate(self, theta, c=point(0,0)): #erreur avec c=point(0,0) (point is not defined)
  x = (self.x - c.x)*math.cos(theta) + (self.y - c.y)*math.sin(theta) + c.x
  y = -(self.x - c.x)*math.sin(theta) + (self.y - c.y)*math.cos(theta) + c.y
  self.x = x
  self.y = y
point.rotate = rotate


def drawarrows(self, p1, p2, m = 1, method = 'bezier'):
  '''m est le nombre d'arrete de p1 vers p2
    méthod : stroke si juste un flêche + nombre
             berier si courbe de bezier'''
  
  if method == 'stroke':
    rad = math.sqrt((p2.x - p1.x)*(p2.x - p1.x) + (p2.y - p1.y)*(p2.y - p1.y))
    if not rad == 0 :
      self.line([p1.n(), p2.n()], 'black')
      theta = math.acos((p2.x - p1.x)/rad)
      if p2.y < p1.y:
        theta = -theta
      r = FLECHE
      alpha = math.pi/6

    t1 = point(p2.x - r*math.cos(theta + alpha), p2.y - r*math.sin(theta + alpha))
    t2 = point(p2.x - r*math.cos(theta - alpha), p2.y - r*math.sin(theta - alpha))
    t3 = point(p2.x - 2*r*math.cos(theta + alpha), p2.y - 2*r*math.sin(theta + alpha))
    self.line([t1.n(), p2.n()], 'black')
    self.line([t2.n(), p2.n()], 'black')
    if(m>0):
      self.text((t3.x + 6,t3.y + 4), str(m), fill='black')
  elif method == 'bezier':
    Bprime = p2 - p1
    normale = point(Bprime.y/math.sqrt(Bprime.x**2 + Bprime.y**2), -Bprime.x/math.sqrt(Bprime.x**2 + Bprime.y**2))
    tangenteNormalisee = point(normale.y, -normale.x)
    mediatrice = 0.5*(p2 + p1)
    for i in range(1, m + 1):
      p = mediatrice + ECART*i*normale
      paux = 2*(p - 0.25*(p2 + p1))
      self.bezier(p1, paux, p2)
      t1 = p + (FLECHE/math.sqrt(2))*(normale - tangenteNormalisee)
      t2 = p - (FLECHE/math.sqrt(2))*(normale + tangenteNormalisee)
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
  '''doc : 
  dessine un graph : method 'manual' si entrée manuelle des node_pos
                            'random' pour génération aléatoire des node_pos
                            'circle' pour une disposition en cercle des node_pos
                            '''
  if(method=='manual'):
    #dessin des arêtes :
    for node in g.get_nodes():
      i = 0
      while i < len(node.get_children_ids()):
        child = node.get_children_ids()[i]
        m = 1
        while(i + 1 < len(node.get_children_ids()) and node.get_children_ids()[i + 1] == child):
          i += 1
          m += 1
        if(m>5):
          delta = math.sqrt((node_pos[child].x - node_pos[node.get_id()].x)*(node_pos[child].x - node_pos[node.get_id()].x) + (node_pos[child].y - node_pos[node.get_id()].y)*(node_pos[child].y - node_pos[node.get_id()].y))    
          self.arrows(node_pos[node.get_id()], point(node_pos[child].x - (node_pos[child].x - node_pos[node.get_id()].x)*RADIUS/delta, node_pos[child].y - (node_pos[child].y - node_pos[node.get_id()].y)*RADIUS/delta), m)
        else:
          self.arrows(node_pos[node.get_id()], node_pos[child], m)
        m = 1
        i+=1
    for i in range(len(input_pos)):
      self.arrows(input_pos[i], point(node_pos[g.get_input_ids()[i]].x - (node_pos[g.get_input_ids()[i]].x - input_pos[i].x)*RADIUS/POINTEUR, (node_pos[g.get_input_ids()[i]].y - (node_pos[g.get_input_ids()[i]].y - input_pos[i].y)*RADIUS/POINTEUR)), 0, 'stroke')
    for i in range(len(output_pos)):
      self.arrows(node_pos[g.get_output_ids()[i]], output_pos[i], 0, 'stroke')
    for n in g.get_nodes():
      self.node(node_pos[n.get_id()], n, verbose=True)
  if(method =='random'):
    np,ip,op = random_layout(g)
    self.graph(g,np,ip,op,method='manual')
  if(method == 'circle'):
    np,ip,op = circle_layout(g)
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

def circle_layout(g): #renvoie un layout affichant les noeuds en cercle autour du milieu de l'image
  node_pos = {}
  input_pos = []
  output_pos = []
  centre = point(WIDTH/2, HEIGHT/2)
  n = len(g.get_nodes())
  p = point(START, START)
  for node in g.get_nodes():
    p2 = p.copy()
    node_pos[node.get_id()] = p2
    p.rotate(2*math.pi/n, centre)
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

def slope_angle(p1, p2):#renvoie l'angle entre le segment [p1, p2] et l'axe des abscisses
  if(p1.x == p2.x):
    return math.pi/2
  else:
    return math.atan((p2.y - p1.y)/(p2.x - p1.x))

def Bezier(self,p0,paux,p1, dt=0.01):
#construit une courbe de bezier de p0 à p1.
  Blast = p0
  t = dt
  while(t < 1):
    B = (1 - t)*((1 - t)*p0 + t*paux) + t*((1 - t)*paux + t*p1)
    self.line([Blast.n(), B.n()], 'black')
    Blast = B
    t += dt
    
ImageDraw.ImageDraw.bezier = Bezier

#memo:

'''def drawarrows(self, p1, p2, n=1, m=0):#ancienne v à la fin du fichier
  
  rad = math.sqrt((p2.x - p1.x)*(p2.x - p1.x) + (p2.y - p1.y)*(p2.y - p1.y))
  rad2 = math.sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))

  if not rad == 0 :
    self.line([p1.n(), p2.n()], 'black')
    theta = math.acos((p2.x - p1.x)/rad)
    theta2 = math.acos((p1.x - p2.x)/rad2)

    if p2.y < p1.y:
      theta = -theta
    if p1.y < p2.y:
      theta2 = -theta2
    r = FLECHE
    alpha = math.pi/6
  if(n > 0):
    t1 = point(p2.x - r*math.cos(theta + alpha), p2.y - r*math.sin(theta + alpha))
    t2 = point(p2.x - r*math.cos(theta - alpha), p2.y - r*math.sin(theta - alpha))
    self.line([t1.n(), p2.n()], 'black')
    self.line([t2.n(), p2.n()], 'black')
    self.text((t2.x - 6,t2.y - 4), str(n), fill='black')

  if(m > 0):
    s1 = point(p1.x - r*math.cos(theta2 + alpha), p1.y - r*math.sin(theta2 + alpha))
    s2 = point(p1.x - r*math.cos(theta2 - alpha), p1.y - r*math.sin(theta2 - alpha))
    self.line([s1.n(), p1.n()], 'black')
    self.line([s2.n(), p1.n()], 'black')
    self.text((s1.x + 6,s1.y + 4), str(m), fill='black')
'''




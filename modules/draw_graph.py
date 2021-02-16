from PIL import Image, ImageDraw
import math
from modules.open_digraph import *


class point:
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def n(self):
    return (round(self.x), round(self.y)) # return a simple tuple de int
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

def drawarrows(self, p1, p2):
  '''doc : todo'''
  self.line([p1.n(), p2.n()], 'black')

ImageDraw.ImageDraw.arrows = drawarrows # we define the method 'arrows'
                                          # from the function 'arrows' above

def drawnode(self, p, node, verbose=False):
  self.ellipse((p.x - 25, p.y - 25, p.x + 25, p.y + 25), fill='white', outline='red') 
  self.text((p.x - 6*len(node.label)/2,p.y - 6), node.label, fill='black')
  if verbose :
    self.text((p.x - 3,p.y + 12), str(node.id), fill='black')

ImageDraw.ImageDraw.node = drawnode

def drawgraph(self, g, node_pos, method='manual',  input_pos, output_pos):
  '''doc : todo'''
  for i in range(len(input_pos)):
    self.arrows(input_pos[i], node_pos[g.get_input_ids[i]])
  for i in range(len(output_pos)):
    self.arrows(output_pos[i], node_pos[g.get_output_ids[i]])
  for n in g.get_nodes():
    self.node(node_pos[n.get_id()], n, verbose=True)
  


ImageDraw.ImageDraw.graph = drawgraph








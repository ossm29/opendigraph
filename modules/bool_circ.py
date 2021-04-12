#Oussama Konate et Thomas Delépine :)

from PIL import Image, ImageDraw
import math
from datetime import datetime
from modules.open_digraph import *
from modules.draw_graph import *

class bool_circ(open_digraph): #class représentant les circuits booléens
  def __init__(self, g):
    super().__init__(g.inputs.copy(), g.outputs.copy(), [node.copy() for node in g.get_nodes()])
    if(not self.is_well_formed()):
      raise NameError('g is not a well formed boolean circ')

  def __eq__(self,other):
    return ((self.get_input_ids()== other.get_input_ids()) and (self.get_output_ids() == other.get_output_ids()) 
    and ( self.get_nodes() == other.get_nodes()))

  def __str__(self):
    return ("("+str(self.inputs)+", "+str(self.nodes)
                +", "+str(self.outputs)+")")

  def __repr__(self):
    return "boolean_circ"+str(self)
  
  def convert(self): #transforme un circuit booléen en graph simple
    return open_digraph(self.inputs, self.outputs, self.nodes)

  def is_well_formed(self): #test si un circuit booléen est bien formé
    for node in self.get_nodes():
      if((node.label == "&" or node.label == "|") and (node.outdegree() != 1 or node.indegree() != 2)):#noeud est un OU ou un ET
        return False
      if((node.label == "∼") and (node.indegree() != 1 or node.outdegree() != 1)):#noeud est un not   
        return False
      if(node.label == "" and node.indegree() != 1 ): #noeud est une copie    
        return False
      if((node.label == "1" or node.label == "0") and (node.indegree() != 0 or node.outdegree() != 1)): #noeud est une constante    
        return False     
    return (not self.is_cyclic())

def parse_parentheses(*s, fusion_flag=True):
  #creation du graph
  g = open_digraph([], [0], [node(0, '', [], [])])
  #creations des noeuds et ajouts au graph
  current_node = 0
  s2 = ''
  for prop in s:
    for char in prop:
      if char == '(':
        g.nodes[current_node].label += s2
        current_node = g.add_node('', [], [current_node])
        s2 = ''
      elif char == ')':
        g.nodes[current_node].label += s2
        current_node = g.nodes[current_node].children[0]
        s2 = ''
      else:
        s2 += char
  #gestion des inputs
    for i in range(len(g.get_nodes())):  
      n_local = g.nodes[i]      #n_local est un node
      label = n_local.get_label()
      if(not label in ["|", "&", "~", ""]):
        if(not n_local.id in g.get_input_ids()):
          g.add_input_id(n_local.get_id())
  print(g)
  if fusion_flag:
    #fusion
    to_fuse = {}
    for n_local in g.get_nodes():
      if(n_local.get_label() in to_fuse.keys()):
        to_fuse[n_local.get_label()].append(n_local.get_id())
      else:
        if(not n_local.get_label() in ["|", "&", "~", ""]):
          to_fuse[n_local.get_label()] = [n_local.get_id()]
    for i in to_fuse.keys():
      if(not i in ["|", "&", "~", ""]):
        print(i)
        for j in range(1,len(to_fuse[i])):
          g.fusion(to_fuse[i][0],to_fuse[i][j])
  #return
  return g
        





















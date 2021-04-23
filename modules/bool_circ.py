#Oussama Konate et Thomas Delépine :)

from PIL import Image, ImageDraw
import math
from datetime import datetime
from modules.open_digraph import *
from modules.draw_graph import *
from modules.matrix import *

class bool_circ(open_digraph): #class représentant les circuits booléens
  def __init__(self, g):
    inp = g.inputs.copy()
    out = g.outputs.copy()
    ntab = [node.copy() for node in g.get_nodes()]
    super().__init__(inp, out , ntab)
    if(not self.is_well_formed()):
      raise NameError('g is not a well formed boolean circ')
    self.starters = {} #dict {int:str} un id, un nom de variables

  def __eq__(self,other):
    return ((self.get_input_ids() == other.get_input_ids()) and (self.get_output_ids() == other.get_output_ids()) 
    and ( self.get_nodes() == other.get_nodes()))

  def __str__(self):
    return ("("+str(self.inputs)+", "+str(self.nodes)
                +", "+str(self.outputs)+")")

  def __repr__(self):
    return "boolean_circ"+str(self)
  
  def convert(self): #transforme un circuit booléen en graph simple
    return open_digraph(self.inputs, self.outputs, self.nodes)

  def is_well_formed(self): #test si un circuit booléen est bien formé
    tmp = self.copy()
    for node in tmp.get_nodes():
      if((node.label == "&" or node.label == "|") and (node.outdegree() != 1)):#noeud est un OU ou un ET
        print(node.id)
        print("code d'erreur a")
        return False
      if((node.label == "∼") and (node.indegree() != 1 or node.outdegree() != 1)):#noeud est un not   
        print(node.id)
        print("code d'erreur b")
        return False
      if(node.label == "" and node.indegree() != 1 ): #noeud est une copie
        print(node.id)
        print("code d'erreur c")
        #return False
      if((node.label == "1" or node.label == "0") and (node.indegree() != 0 or node.outdegree() != 1)): #noeud est une constante    
        print(node.id)
        print("code d'erreur d")
        return False   
    if(tmp.is_cyclic()):
      print("Y")
    return (not tmp.is_cyclic())

def parse_parentheses(*s, fusion_flag=True):
  graphs = []
  for prop in s:
    #creation du graph
    local = open_digraph([], [0], [node(0, '', [], [])])
    #creations des noeuds et ajouts au graph
    current_node = 0
    s2 = ''
    for char in prop:
      if char == '(':
        local.nodes[current_node].label += s2
        current_node = local.add_node('', [], [current_node])
        s2 = ''
      elif char == ')':
        local.nodes[current_node].label += s2
        current_node = local.nodes[current_node].children[0]
        s2 = ''
      else:
        s2 += char
  #gestion des inputs
    for i in range(len(local.get_nodes())):  
      n_local = local.nodes[i]      #n_local est un node
      label = n_local.get_label()
      if(not label in ["|", "&", "~", ""]):
        if(not n_local.id in local.get_input_ids()):
          local.add_input_id(n_local.get_id())
    graphs.append(local)
  g = graphs[0]
  for i in range(1, len(graphs)):
    g.iparallel(graphs[i])
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
        for j in range(1,len(to_fuse[i])):
          g.fusion(to_fuse[i][0],to_fuse[i][j])
  res = bool_circ(g)
  for id in res.get_input_ids():
    res.starters[id] = g.nodes[id].get_label()
  #renvoie
  #print(res.starters)
  return res
        
def random_bool_circ(n):
  g = random_graph(n,1,form="DAG")

  for node in g.get_nodes():
    if( node.parents == []):
      g.inputs.append(node.get_id())
    if(node.children == []):
      g.outputs.append(node.get_id())

  for node in g.get_nodes():
    if(node.indegree() == node.outdegree() and node.indegree() == 1):
      g.nodes[node.get_id()].label = "~"
    if(node.indegree() > 1 and node.outdegree() == 1):
      tmp = random.randint(0,2)
      if (tmp == 1):
        g.nodes[node.get_id()].label = "&" 
      else :
        g.nodes[node.get_id()].label ="|"
      #g.nodes[node.get_id()].label = "&" if tmp == 1 else "|"

    if(node.indegree() > 1 and node.outdegree() > 1):
      tmp = random.randint(0,2)
      if (tmp == 1):
        local = "&" 
      else :
        local = "|"
      
      id1 = g.add_node(local,node.get_parents_ids(),[])
      id2 = g.add_node("",[],node.get_children_ids())
      g.add_edge(id1,id2)
      for i in range(len(g.get_input_ids())):
        if(g.get_input_ids()[i] == node.get_id()):
          g.inputs[i] = id1
        
      for i in range(len(g.get_output_ids())):
        if(g.get_output_ids()[i] == node.get_id()):
          g.outputs[i] = id2
      g.remove_node_by_id(node.get_id())

    if(node.indegree() == 1 and node.outdegree() > 1):
      g.nodes[node.get_id()].label = ""
  res = bool_circ(g)
  for i in range(len(res.get_input_ids())):
    res.nodes[res.get_input_ids()[i]].label = 'input ' + str(i)
  for i in range(len(res.get_output_ids())):
    res.nodes[res.get_output_ids()[i]].label = 'output ' + str(i)
  return res
















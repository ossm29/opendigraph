import random
from modules.open_digraph import *

def random_int_list(n, bound): #@param : n (int) : nb éléments | bound (int) : valeur max
  liste = []
  for i in range(0,n):
    liste.append(random.randint(0,bound))
  return liste #@return : int list


def random_matrix(n, bound, null_diag=False, symetric=False, oriented=False, triangular=False):
  liste = []
  for element in range(0,n):
    liste.append(random_int_list(n,bound))
  if null_diag:
    for i in range(0,n):
      liste[i][i] = 0
  if symetric:
    for i in range(0, n):
      for j in range(0, i + 1):
        liste[i][j] = liste[j][i]
  if oriented:
    for i in range(0, n):
      for j in range(0, n):
        if liste[i][j] != 0 and liste[j][i] != 0:
          rand = random.randint(0, 1)
          if rand == 0:
            liste[i][j] = 0
          else :
            liste[j][i] = 0
  if triangular:
    for i in range(0, n):
      for j in range(i + 1, n):
        liste[i][j] = 0

  return liste

def  graph_from_adjacency_matrix(matrix):
  nodeNumber = len(matrix)
  nodeList = []
  for i in range(nodeNumber):
    nodeList.append(node(i, "value", [], []))
  for i in range(nodeNumber):
    for j in range(nodeNumber):
      for iteration in range(matrix[i][j]):
        nodeList[i].add_child_id(j)
        nodeList[j].add_parent_id(i)
  return open_digraph([],[],nodeList)

def random_graph(n, bound, inputs=0, outputs=0, form="free"):
  '''
  form:
    "free" = graph sans contraintes
    "DAG" = graph dirigé acyclique
    "oriented" = graph dirigé avec arête entre 2 nodes que dans un sens
    "undirected" = graph non-dirigé : symétrique
    "loop-free undirected" = sans boucle et non-dirigé

  '''
  if form=="free":
    g = graph_from_adjacency_matrix(random_matrix(n, bound))
  elif form=="DAG":
    g = graph_from_adjacency_matrix(random_matrix(n, bound, null_diag=True, triangular=True))
  elif form=="oriented":
    g = graph_from_adjacency_matrix(random_matrix(n, bound, null_diag=True, oriented=True))
  elif form=="undirected":
    g = graph_from_adjacency_matrix(random_matrix(n, bound, symetric=True))
  elif form=="loop-free undirected":
    g = graph_from_adjacency_matrix(random_matrix(n, bound, null_diag=True, symetric=True))
  l = list(range(n))
  for i in range(inputs):
    e = random.choice(l)
    g.add_input_id(e)
    l.remove(e)
  l = list(range(n))
  for i in range(outputs):
    e = random.choice(l)
    g.add_output_id(e)
    l.remove(e)
  return g













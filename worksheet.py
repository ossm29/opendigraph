#Oussama Konate, Thomas Delépine, groupe 8
from modules.open_digraph import *
import inspect

print("-------test :-----------")
print("hello, world")
for i in range(10):
  print("1 2 3 viva : ", i);

print("----affichage d'un noeud----")
n0 = node(0, '&', [], [])
print(n0)

print("----affichage de graphes----")
n1 = node(1, 'j', [0], [])
g = open_digraph([0], [1], [n0, n1])
e = open_digraph.empty()
print(g)
print(e)

print("----Q3 TD2----")
print(dir(node))

print(dir(open_digraph))

print(inspect.getsource(node.copy))
print(inspect.getdoc(node.copy))
print(inspect.getfile(node.copy))
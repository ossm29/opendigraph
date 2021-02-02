from modules.open_digraph import *
import unittest  

print("hello, world")
for i in range(10):
  print("1 2 3 viva : ", i);

n0 = node(0, '&', [], [])
print(n0)

n1 = node(1, 'j', [0], [])
g = open_digraph([0], [1], [n0, n1])
e = open_digraph.empty()
print(g)
print(e)
f = g.copy()

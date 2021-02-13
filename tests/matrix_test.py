#Oussama Konate, Thomas Delépine, groupe 8
import sys
import unittest
import random
sys.path.append('../') # allows us to fetch files from the project root
from modules.matrix import *
from modules.open_digraph import *

def print_matrix(matrix):
  print("########################")
  for i in range(len(matrix)):
    print(matrix[i])
  print("########################")

class ListTest(unittest.TestCase):
  def test_random_int_list(self):
    self.assertEqual(random_int_list(100,1000)==random_int_list(100,1000),False)
    self.assertEqual(len(random_int_list(10,10)),10)

class MatrixTest(unittest.TestCase):
  def test_random_int_matrix(self):
    test = random_matrix(10,10)
    for element in test:
      self.assertEqual(len(element),10)

  def test_random_int_matrix2(self):
    test2 = random_matrix(10,10,null_diag=True)
    for i in range(0,10):
      self.assertEqual(test2[i][i],0)

  def test_sym_rand_matrix(self):
    m = random_matrix(5, 10, null_diag = True, symetric = True)
    for i in range(5):
      for j in range(5):
        self.assertEqual(m[i][j], m[j][i])
      self.assertEqual(m[i][i], 0)
  
  def test_oriented_int_matrix(self):
    m = random_matrix(5, 10, oriented = True)
    for i in range(5):
      for j in range(5):
        if m[i][j] != 0:
          self.assertEqual(m[j][i], 0)

  def test_triangular_int_matrix(self):
    m = random_matrix(5, 10, triangular = True)
    for i in range(5):
      for j in range(i+1, 5):
        self.assertEqual(m[i][j], 0)

  def test_graph_from_adjacency_matrix(self):
    self.assertEqual(graph_from_adjacency_matrix(random_matrix(3, 3)).is_well_formed(), True)
    self.assertEqual(graph_from_adjacency_matrix(random_matrix(10, 9, null_diag=True)).is_well_formed(), True)
    self.assertEqual(graph_from_adjacency_matrix(random_matrix(10, 9, symetric=True)).is_well_formed(), True)
    self.assertEqual(graph_from_adjacency_matrix(random_matrix(10, 9, null_diag=True, symetric=True)).is_well_formed(), True)
    self.assertEqual(graph_from_adjacency_matrix(random_matrix(10, 9, oriented=True)).is_well_formed(), True)
    self.assertEqual(graph_from_adjacency_matrix(random_matrix(10, 9, triangular=True)).is_well_formed(), True)
    self.assertEqual(graph_from_adjacency_matrix(random_matrix(10, 9, null_diag=True, triangular=True)).is_well_formed(), True)

  def test_graph_from_adjacency_matrix(self):
    self.assertEqual(random_graph(2, 2, inputs=0, outputs=0, form="free").is_well_formed(), True)
    self.assertEqual(random_graph(2, 2, inputs=0, outputs=0, form="DAG").is_well_formed(), True)
    self.assertEqual(random_graph(2, 2, inputs=0, outputs=0, form="oriented").is_well_formed(), True)
    self.assertEqual(random_graph(2, 2, inputs=0, outputs=0, form="undirected").is_well_formed(), True)
    self.assertEqual(random_graph(2, 2, inputs=0, outputs=0, form="loop-free undirected").is_well_formed(), True)

'''
  def test_print(self):
    print("rand int matrix")
    print_matrix(random_matrix(10, 9))
    print("rand int matrix diag = 0")
    print_matrix(random_matrix(10, 9, null_diag=True))
    print("rand int matrix sym")
    print_matrix(random_matrix(10, 9, symetric=True))
    print("rand int matrix diag = 0 sym")
    print_matrix(random_matrix(10, 9, null_diag=True, symetric=True))
    print("rand int matrix oriented")
    print_matrix(random_matrix(10, 9, oriented=True))
    print("rand int matrix triangular")
    print_matrix(random_matrix(10, 9, triangular=True))
    print("rand int matrix diag = 0 triangular")
    print_matrix(random_matrix(10, 9, null_diag=True, triangular=True))
'''

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.














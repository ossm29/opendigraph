#Oussama Konate, Thomas Delépine, groupe 8
import sys
import unittest
import random
sys.path.append('../') # allows us to fetch files from the project root
from modules.matrix import *

class ListTest(unittest.TestCase):
  def test_random_int_list(self):
    self.assertEqual(random_int_list(100,1000)==random_int_list(100,1000),False)
    self.assertEqual(len(random_int_list(10,10)),10)

class MatrixTest(unittest.TestCase):
  def test_random_int_matrix(self):
    test = random_int_matrix(10,10)
    for element in test:
      self.assertEqual(len(element),10)
  def test_random_int_matrix2(self):
    test2 = random_int_matrix(10,10,null_diag=True)
    for i in range(0,10):
      self.assertEqual(test2[i][i],0)




if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.


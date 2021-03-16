#Oussama Konate, Thomas Delépine, groupe 8
import sys
sys.path.append('../') # allows us to fetch files from the project root
import math
import unittest
from modules.bool_circ import *
import time

class boolTest(unittest.TestCase):
  def test_init(self):
    n0 = node(0, 'i', [], [1])
    n1 = node(1, 'j', [0], [])
    g = open_digraph([0], [1], [n0, n1])
    c1 = bool_circ(g)
    c2 = bool_circ(g)
    self.assertEqual(c1, c2)

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.   

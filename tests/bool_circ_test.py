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
  
  def test_is_well_formed(self):
    b0 = node(0,'&',[1],[4])
    b1 = node(1,"",[],[0,2])
    b2 = node(2,"|",[1],[3])
    b3 = node(3,"∼",[2],[4])
    b4 = node(4,"|",[0,3],[])
    c = bool_circ(open_digraph([0,1,2], [4], [b0,b1,b2,b3,b4]))
    self.assertEqual(c.is_well_formed(), True)

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.   

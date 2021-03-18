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
    c1 = node(5, '1', [], [0])
    c2 = node(6, '0', [], [1])
    c3 = node(7, '1', [], [2])
    b0 = node(0,'&',[1,5],[4])
    b1 = node(1,"",[6],[0,2])
    b2 = node(2,"|",[1, 7],[3])
    b3 = node(3,"∼",[2],[4])
    b4 = node(4,"|",[0,3],[8])
    s1 = node(8, "sortie", [4], [])
    c = bool_circ(open_digraph([5,6,7], [4], [b0,b1,b2,b3,b4,c1,c2,c3,s1]))


    self.assertEqual(c.is_well_formed(), True)

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.   

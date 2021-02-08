#Oussama Konate, Thomas Delépine, groupe 8
import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.utils import *

class listTest(unittest.TestCase):
  
  def test_list(self):
    l = []
    self.assertEqual(l, remove_all(l, 1))
    self.assertEqual(l, remove_all(l, "1"))
    l = [1,2,1,2,1,2,1]
    self.assertEqual([2,2,2], remove_all(l, 1))
  
  def test_count_occurence(self):
    l = [0,0,1,2,1,2,3,5,100,8,5,9,10]
    self.assertEqual(count_occurence(l, 0), 2)
    self.assertEqual(count_occurence(l, 1), 2)
    self.assertEqual(count_occurence(l, 2), 2)
    self.assertEqual(count_occurence(l, 100), 1)
    self.assertEqual(count_occurence(l, 42), 0)
    self.assertEqual(count_occurence([], 1), 0)

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.

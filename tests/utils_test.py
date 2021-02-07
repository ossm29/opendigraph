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

if __name__ == '__main__':  # the following code is called only when
  unittest.main()           # precisely this file is run.

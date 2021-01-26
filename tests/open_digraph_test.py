import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest

from modules.open_digraph import *

class InitTest(unittest.TestCase):
  def test_init_node(self):
    n0 = node(0, 'i', [], [1])
    self.assertEqual(n0.id, 0)
    self.assertEqual(n0.label, 'i')
    self.assertEqual(n0.parents, [])
    self.assertEqual(n0.children, [1])
    self.assertIsInstance(n0, node)
if __name__ == '__main__': # the following code is called only when
unittest.main() # precisely this file is run

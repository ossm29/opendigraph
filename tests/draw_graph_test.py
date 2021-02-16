#Oussama Konate, Thomas Delépine, groupe 8
import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.draw_graph import *

class pointtest(unittest.TestCase):
  def test_point(self):
    p1 = point(1, 2)
    p2 = point(5, 5)
    self.assertEqual(p1, p1.copy())
    self.assertIsNot(p1, p1.copy())
    self.assertEqual(p1 + p2, point(6, 7))
    self.assertEqual(p2 - p1, point(4, 3))
    self.assertEqual(2*p1, point(2, 4))

  def test_draw(self):
    width = 400
    height = 400
    image = Image.new("RGB", (width, height), 'white')
    draw = ImageDraw.Draw(image)
    n1 = node(1, 'i', [], [])
    n2 = node(2, 'j', [], [])
    g = open_digraph([], [], [n1, n2])
    node_pos = {}
    node_pos[1] = point(100, 100)
    node_pos[2] = point(200, 200)
    draw.graph(g, node_pos)
    image.save("test.jpg")


if __name__ == '__main__':  # the following code is called only when
  unittest.main() 
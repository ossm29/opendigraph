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
    width = 600
    height = 600
    image = Image.new("RGB", (width, height), 'white')
    draw = ImageDraw.Draw(image)
    n1 = node(1, 'i', [], [])
    n2 = node(2, 'j', [], [])
    g = open_digraph([], [], [n1, n2])
    node_pos = {}
    node_pos[1] = point(100, 100)
    node_pos[2] = point(200, 200)
    draw.graph(g, node_pos, [], [])
    draw.arrows(point(300, 300), point(400, 400))
    draw.arrows(point(300, 300), point(300, 400))
    draw.arrows(point(300, 300), point(400, 300))
    draw.arrows(point(300, 300), point(200, 400))
    draw.arrows(point(300, 300), point(400, 100))
    draw.arrows(point(300, 300), point(100, 300))
    draw.arrows(point(300, 300), point(450, 75))
    draw.arrows(point(300, 300), point(86, 95))
    draw.arrows(point(300, 300), point(300, 50))
    image.save("test.jpg")
  


if __name__ == '__main__':  # the following code is called only when
  unittest.main() 
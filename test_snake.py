import unittest as ut
from grid import Grid

class TestGrid(ut.TestCase):
    def test_grid_count(self):
        grid = Grid(10,10)
        self.assertEqual(grid.count(), 100)
        print("Game passed grid unit test")

if __name__== '__main__':
    ut.main()
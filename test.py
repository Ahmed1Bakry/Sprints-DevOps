import unittest

from sprints import MyFunc


class TestMyFunc(unittest.TestCase):
    def test_mean_int(self):

        mylist = [1, 2, 3, 4, 5]
        mean, max_fl = MyFunc(mylist)
        self.assertEqual(mean, 3)

    def test_mean_negative(self):

        mylist = [-1, -2, -3, -4, -5]
        mean, max_fl = MyFunc(mylist)
        self.assertEqual(mean, -3)
        
    def test_max_float(self):

        mylist = [1, 2, 3, 4, 5, 1.5, 44.2, -90.42]
        mean, max_fl = MyFunc(mylist)
        self.assertEqual(max_fl, 44.2)
        
    def test_empty(self):

        mylist = []
        res = MyFunc(mylist)
        self.assertEqual(res, 0)
       
if __name__ == '__main__':
    unittest.main()

import unittest
import run

class TestRun(unittest.TestCase):
    """
    Test suite for run.py file
    """
    def test_quick_sort_works(self):
        """
        Test is to ensure the total size of the grid
        is equal to width * height
        """
        scores = [3,4,2,1,5]
        names = ["ben","jack","ted","lol","bing"]
        result = run.quicksort(scores, names, 0, len(scores) - 1)
        self.assertEqual(result, [1,2,3,4,5])
        
if __name__ == '__main__':
    unittest.main()
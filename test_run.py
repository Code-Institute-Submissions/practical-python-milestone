import unittest
import run

class TestRun(unittest.TestCase):
    """
    Test suite for run.py file
    """
    def test_quick_sort_works(self):
        """
        Test is to ensure that the quicksort method sorts the list.
        """
        scores = [3,4,2,1,5]
        names = ["ben","jack","ted","lol","bing"]
        result = run.quicksort(scores, names, 0, len(scores) - 1)
        self.assertEqual(result, [1,2,3,4,5])
        
    def test_csv_file_writer(self):
        """
        Test is to ensure that my csv file writer works.
        """
        result = run.write_to_csv_file("data/test.csv", [1,2,3], ["test","test1","test2"])
        self.assertEqual(result, True)
        
if __name__ == '__main__':
    unittest.main()
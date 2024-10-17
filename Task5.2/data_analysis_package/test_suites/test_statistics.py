# test_suites/test_statistics.py
import unittest
from data_analysis_package.statistics import mean, standard_deviation

class TestStatistics(unittest.TestCase):
    
    def test_mean(self):
        data = [2, 4, 6, 8, 10]
        print("Data for mean calculation:", data)
        result = mean(data)
        print("Calculated mean:", result)
        self.assertEqual(result, 6.0, f"The mean should be 6.0, but got {result}.")

    def test_standard_deviation(self):
        data = [1, 1, 1, 1, 1]
        print("Data for standard deviation calculation:", data)
        result = standard_deviation(data)
        print("Calculated standard deviation:", result)
        self.assertEqual(result, 0.0, f"The standard deviation should be 0.0, but got {result}.")

if __name__ == "__main__":
    unittest.main()





    


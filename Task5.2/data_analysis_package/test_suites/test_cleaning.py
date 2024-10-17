# test_suites/test_cleaning.py
import unittest
import pandas as pd
from data_analysis_package.cleaning import handle_missing_data

class TestCleaning(unittest.TestCase):

    def test_handle_missing_data_drop(self):
        data = pd.DataFrame({
            'A': [None, 2, None, 4, None],
            'B': [1, None, 3, None, None]
        })
        print("Original DataFrame (drop method):\n", data)  # Print original DataFrame
        cleaned_data = handle_missing_data(data, method='drop')
        print("Cleaned DataFrame (drop method):\n", cleaned_data)  # Print cleaned DataFrame
        self.assertEqual(cleaned_data.shape[0], 4, "There should be 4 rows after dropping missing data.")

    def test_handle_missing_data_fill(self):
        data = pd.DataFrame({
            'A': [None, 2, None, 4, 5],
            'B': [None, 2, 3, None, 5]
        })
        print("Original DataFrame (fill method):\n", data)  # Print original DataFrame
        cleaned_data = handle_missing_data(data, method='fill')
        print("Cleaned DataFrame (fill method):\n", cleaned_data)  # Print cleaned DataFrame
        self.assertFalse(cleaned_data.isnull().any().any(), "Data should have no missing values after cleaning.")

if __name__ == "__main__":
    unittest.main()





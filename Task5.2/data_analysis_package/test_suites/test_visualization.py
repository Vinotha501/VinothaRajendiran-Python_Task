# test_suites/test_visualization.py
import unittest
import matplotlib.pyplot as plt
from data_analysis_package.visualization import plot_histogram

class TestVisualization(unittest.TestCase):

    def test_histogram_properties(self):
        data = [1, 1, 2, 3, 5, 5, 5, 7, 8, 8, 9, 9, 9, 9, 10]
        print("Data for histogram:", data)
        fig, ax = plt.subplots()
        plot_histogram(data)

        # Assertions for the histogram properties
        self.assertEqual(len(ax.patches), 5)
        self.assertAlmostEqual(ax.patches[0].get_width(), 0.9, places=6)

if __name__ == "__main__":
    unittest.main()







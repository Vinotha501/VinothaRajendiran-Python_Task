# data_analysis_package/visualization.py
import matplotlib.pyplot as plt

def plot_histogram(data):
    plt.hist(data, bins=5, color='blue', rwidth=0.5)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()






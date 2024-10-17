# data_analysis_package/statistics.py

from math import sqrt

def mean(data):
    return sum(data) / len(data)

def standard_deviation(data):
    mean_val = mean(data)
    return sqrt(sum((x - mean_val) ** 2 for x in data) / len(data))

def t_test(sample1, sample2):
    mean1 = mean(sample1)
    mean2 = mean(sample2)
    std1 = standard_deviation(sample1)
    std2 = standard_deviation(sample2)
    n1 = len(sample1)
    n2 = len(sample2)
    
    pooled_std = sqrt(((n1 - 1) * std1 ** 2 + (n2 - 1) * std2 ** 2) / (n1 + n2 - 2))
    t_statistic = (mean1 - mean2) / (pooled_std * sqrt(1 / n1 + 1 / n2))
    df = n1 + n2 - 2
    
    return t_statistic, df

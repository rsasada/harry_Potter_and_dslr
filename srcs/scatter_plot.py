import numpy as np
import matplotlib.pyplot as plt
from libft.csv import load_csv
from libft.math import ft_max, ft_min
from visualization.scatter_plot import plot_most_similar_features

if __name__ == '__main__':
    dataset = load_csv('./datasets/dataset_train.csv')

    plot_most_similar_features(dataset)
    plt.show()
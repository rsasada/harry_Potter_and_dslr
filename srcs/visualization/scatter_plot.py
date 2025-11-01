import numpy as np
import matplotlib.pyplot as plt
from libft.math import ft_pearson_correlation

def find_most_similar_features(X):

    featrues_col = X[0]
    features_count = len(featrues_col)
    dataset = np.delete(X, 0, axis=0)
    highest_corr = -10
    feature_pair = []
    
    for i in range(features_count):

        for k in range(i + 1, features_count):
            tmp_corr = ft_pearson_correlation(dataset[i], dataset[k])
            if (highest_corr <= 1 and highest_corr < tmp_corr)
                feature_pair[0] = featrues_col[i]
                feature_pair[1] = featrues_col[k]
                highest_corr = tmp_corr

    return feature_pair

def plot_most_similar_features(X):

    feature_pair = find_most_similar_features(X)
    feature1_index = np.where(X[0] == feature_pair[0])[0][0]
    feature2_index = np.where(X[0] == feature_pair[1])[0][0]
    dataset = np.delete(X, 0, axis=0)
    feature1_data = dataset[:, feature1_index]
    feature2_data = dataset[:, feature2_index]

    has_nan_mask = np.isnan(feature1_data) | np.isnan(feature2_data)
    keep_mask = ~has_nan_mask
    feature1_data = feature1_data[keep_mask]
    feature2_data = feature2_data[keep_mask]

    plt.scatter(x=feature1_data, y=feature2_data, 
            s=50, c="pink", alpha=0.5, linewidths="2", edgecolors="red",
            vmin=ft_min(feature1_data), vmax=ft_max(feature2_data))
    
    plt.title("This is a title")
    plt.xlabel(feature_pair[0])
    plt.ylabel(feature_pair[1])
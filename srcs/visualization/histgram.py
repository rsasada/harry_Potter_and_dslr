import numpy as np
import matplotlib.pyplot as plt


def overlay_histgram(data, legend, title, xlabel, ylabel, bins, range):

	houses_array = data[:, 0]
	scores_array = np.array(data[:, 1], dtype=float)
	h1 = scores_array[houses_array == legend[0]]
	h2 = scores_array[houses_array == legend[1]]
	h3 = scores_array[houses_array == legend[2]]
	h4 = scores_array[houses_array == legend[3]]

	h1 = h1[~np.isnan(h1)]
	h2 = h2[~np.isnan(h2)]
	h3 = h3[~np.isnan(h3)]
	h4 = h4[~np.isnan(h4)]

	plt.hist(h1, color='red', alpha=0.5, density=True, 
			bins=bins, range=range, label=legend[0]) 
	plt.hist(h2, color='yellow', alpha=0.5, density=True, 
             bins=bins, range=range, label=legend[1])
	plt.hist(h3, color='blue', alpha=0.5, density=True, 
             bins=bins, range=range, label=legend[2])
	plt.hist(h4, color='green', alpha=0.5, density=True, 
             bins=bins, range=range, label=legend[3])
	plt.legend(loc='upper right', frameon=False) 
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
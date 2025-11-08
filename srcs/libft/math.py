import numpy as np

def count_(X):
	try:
		X = X.astype('float')
		X = X[~np.isnan(X)]
		return len(X)
	except:
		return len(X)

def ft_max(X):
     
	max = X[0]
	for x in X:
		if x > max:
			max = x

	return max


def ft_min(X):
	min = X[0]
	for x in X:
		if x < min:
			min = x
	return min

def ft_mean(X):

	sum = 0
	i = 0
	for x in X:
		if (np.isnan(x)):
			continue
		sum += x
		i += 1
	if i == 0:
		return 0
	return sum / i

def ft_std(X):
	i = 0
	mean = ft_mean(X)
	sum = 0

	for x in X:
		if np.isnan(x):
			continue
		diff = x - mean
		sum += diff * diff
		i+= 1
	if i == 0:
		return 0
	return np.sqrt(sum / i)

def ft_percentage(X, percent):
	if (len(X) == 0):
		return 0
	
	X.sort()
	index = (len(X) - 1) * percent
	f = np.floor(index)
	c = np.ceil(index)
	if c == f:
		return X[int(index)]

	return X[int(f)] + (X[int(c)] - X[int(f)]) * (index - f)

def ft_pearson_correlation(X, Y):
	
	if len(X) != len(Y):
		return 0
	
	x_mean = ft_mean(X)
	y_mean = ft_mean(Y)
	x_std = ft_std(X)
	y_std = ft_std(Y)
	sum = 0
	nan_count = 0

	for i, x in enumerate(X):
		if np.isnan(x) or np.isnan(Y[i]):
			nan_count += 1
			continue
		diff_x = x - x_mean
		diff_y = Y[i] - y_mean
		sum += diff_x * diff_y
	
	return (sum / (i - nan_count)) / (x_std * y_std)
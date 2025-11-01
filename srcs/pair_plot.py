import numpy as np
import matplotlib.pyplot as plt
from libft.csv import load_csv
import pandas as pd
import seaborn as sns


if __name__ == '__main__':
    dataset = load_csv('./datasets/dataset_train.csv')

    df = pd.DataFrame(dataset, columns=dataset[0])

    sns.pairplot(df, hue="Hogwarts House")
    plt.show()
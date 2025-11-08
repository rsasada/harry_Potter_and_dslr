import numpy as np
import matplotlib.pyplot as plt
from libft.csv import load_csv
import pandas as pd
import seaborn as sns


if __name__ == '__main__':
    dataset = load_csv('./datasets/dataset_train.csv')

    # ヘッダー行を除いてDataFrameを作成
    headers = dataset[0]
    data = dataset[1:]
    df = pd.DataFrame(data, columns=headers)
    
    # 数値列のみを選択（最初の6列はIndex, Hogwarts House, First Name, Last Name, Birthday, Best Handなので除外）
    numeric_columns = list(headers[6:])
    numeric_columns.append('Hogwarts House')  # hueとして使用するため追加
    
    # 必要な列だけを抽出
    df_filtered = df[numeric_columns].copy()
    
    # 数値列を明示的にfloat型に変換
    for col in headers[6:]:
        df_filtered[col] = pd.to_numeric(df_filtered[col], errors='coerce')
    
    sns.pairplot(df_filtered, hue="Hogwarts House")
    plt.show()
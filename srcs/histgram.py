import numpy as np
import matplotlib.pyplot as plt
from libft.csv import load_csv
from libft.math import ft_max, ft_min
from visualization.histgram import overlay_histgram

if __name__ == '__main__':
    dataset = load_csv('./datasets/dataset_train.csv')
    
    headers = dataset[0, :]
    data = dataset[1:, :]
    
    legend = ['Grynffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    NUM_BINS = 20
    
    # 寮の列（インデックス1）をあらかじめ取得しておく
    houses_col = data[:, 1]

    # 13個のヒストグラムを5x3のグリッドで表示（より縦長で見やすく）
    fig, axes = plt.subplots(5, 3, figsize=(18, 24))
    axes = axes.flatten()  # 2D配列を1D配列に変換
    
    for idx, i in enumerate(range(6, 19)): # 6から18までループ
        plt.sca(axes[idx])  # 現在のサブプロットを設定

        scores_col = data[:, i]
        
        data_for_hist = np.stack((houses_col, scores_col), axis=1)

        scores_float = np.array(scores_col, dtype=float)
        current_min = ft_min(scores_float)
        current_max = ft_max(scores_float)
        
        title = headers[i]
        
        # 2列に絞ったデータを渡す
        overlay_histgram(
            data_for_hist,  # [寮, 点数] の配列
            legend=legend,
            title=title,
            xlabel='Marks',
            ylabel='Density',
            bins=NUM_BINS,
            range=(current_min, current_max)
        )
    
    # 使わないサブプロットを非表示
    for idx in range(13, 15):
        axes[idx].axis('off')
    
    plt.tight_layout(pad=3.0)  # サブプロット間の余白を増やす
    plt.show()
from libft.csv import load_csv
from libft.math import ft_max, ft_min, ft_mean, ft_std, ft_percentage, count_
import numpy as np
import sys

def describe(dataset):
    """
    データセットの統計情報を計算して表示する
    """
    # ヘッダー行を除く
    headers = dataset[0]
    data = dataset[1:]
    
    # 数値列のインデックスを取得（最初の列はIndex、次の5列は非数値）
    numeric_start = 6  # Arithmancyから開始
    numeric_headers = headers[numeric_start:]
    
    # 統計情報を格納する辞書
    stats = {
        'Count': [],
        'Mean': [],
        'Std': [],
        'Min': [],
        '25%': [],
        '50%': [],
        '75%': [],
        'Max': []
    }
    
    # 各数値列に対して統計を計算
    for col_idx in range(numeric_start, len(headers)):
        # 列データを抽出（NaNを除外）
        column_data = []
        for row in data:
            try:
                val = float(row[col_idx])
                if not np.isnan(val):
                    column_data.append(val)
            except (ValueError, TypeError):
                continue
        
        if len(column_data) == 0:
            # データがない場合
            stats['Count'].append(0.0)
            stats['Mean'].append(0.0)
            stats['Std'].append(0.0)
            stats['Min'].append(0.0)
            stats['25%'].append(0.0)
            stats['50%'].append(0.0)
            stats['75%'].append(0.0)
            stats['Max'].append(0.0)
        else:
            column_array = np.array(column_data)
            
            # 統計値を計算
            stats['Count'].append(float(len(column_data)))
            stats['Mean'].append(ft_mean(column_array))
            stats['Std'].append(ft_std(column_array))
            stats['Min'].append(ft_min(column_array))
            stats['25%'].append(ft_percentage(column_array.copy(), 0.25))
            stats['50%'].append(ft_percentage(column_array.copy(), 0.50))
            stats['75%'].append(ft_percentage(column_array.copy(), 0.75))
            stats['Max'].append(ft_max(column_array))
    
    # 結果を表示
    # 各列の最大幅を計算（列名と数値の両方を考慮）
    col_widths = []
    for i, header in enumerate(numeric_headers):
        max_width = max(len(header), 15)  # 最小15文字
        col_widths.append(max_width)
    
    # ヘッダー行を表示
    header_line = " " * 8  # 統計名のスペース
    for i, header in enumerate(numeric_headers):
        header_line += f"{header:>{col_widths[i]}}"
    print(header_line)
    
    # 各統計行を表示
    stat_names = ['Count', 'Mean', 'Std', 'Min', '25%', '50%', '75%', 'Max']
    for stat_name in stat_names:
        line = f"{stat_name:8}"
        for i, value in enumerate(stats[stat_name]):
            line += f"{value:{col_widths[i]}.6f}"
        print(line)

def main():
    if len(sys.argv) != 2:
        print("Usage: python describe.py <dataset.csv>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        dataset = load_csv(filename)
        describe(dataset)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

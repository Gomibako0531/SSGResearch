import os
import pandas as pd

def calculate_ratio(file_path):
    # 使用pandas读取Excel文件
    df = pd.read_excel(file_path)
    
    # 直接使用列名'white_area_ratio'来引用数据，并计算大于4.5的数值比例
    ratio = (df['white_area_ratio'] > 3).mean()
    return ratio

def process_directory(directory_path, output_path):
    # 准备一个列表来收集结果
    results = []
    # 遍历目录下的所有文件
    for file in os.listdir(directory_path):
        if file.endswith('.xlsx') and not file.startswith('~$'):
            # 构造完整的文件路径
            file_path = os.path.join(directory_path, file)
            # 计算比例
            ratio = calculate_ratio(file_path)
            # 根据比例值决定出席状态
            status = '出席' if ratio > 0.2 else '欠席'
            # 将文件名、比例和出席状态添加到结果列表中
            results.append((file, ratio, status))

    # 将结果保存到新的Excel文件中，包括出席状态
    output_df = pd.DataFrame(results, columns=['FileName', 'Ratio', 'Status'])
    output_df.to_excel(output_path, index=False)

# 示例用法：
directory_path = 'C:\\Users\\okada\\Desktop\\22_立命高等学校\\ROI\\fujita\\出席確認'
output_path = 'C:\\Users\\okada\\Desktop\\22_立命高等学校\\ROI\\ratios_output2.xlsx'
process_directory(directory_path, output_path)

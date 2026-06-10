# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 15:02:15 2023

@author: okada
"""

import pandas as pd
import numpy as np
import csv
import cv2

Outputlist = [['number','sum','ave','attend']]
for i in range(30):
    # CSVファイルのパスを指定する
    csv_file_path = '/fujita/ROI_sabun/1min_sabun_sub'+str(i+1)+'.csv'
    # CSVファイルを読み込む
    df = pd.read_csv(csv_file_path)
    if (df['white_area_ratio'].sum() >= 1900) or (df['white_area_ratio'].mean() >= 1):
        Outputlist.append([i+1, df['white_area_ratio'].sum(), df['white_area_ratio'].mean(), 1])
    else:
        Outputlist.append([i+1,df['white_area_ratio'].sum(),df['white_area_ratio'].mean(),0])
        
#csv出力#####################################################################################
with open('/fujita/attend_result.csv', 'w', newline="") as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerows(Outputlist)
#############################################################################################

csv_file_path = '/fujita//attend_result.csv'
# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

print(str(df['attend'].sum())+'/30')
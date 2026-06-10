import pandas as pd
import numpy as np
import csv
import cv2
import csv
from os.path import splitext, dirname, basename, join

movie_path = "C:/Users/okada/Desktop/22_立命高等学校/ROI/fujita/.mp4"

output_csv_path = "C:/Users/okada/Desktop/22_立命高等学校/ROI/fujita/"
#output_image_path = "/fujita/1min_output/"

threshold = 15

csv_file = pd.read_csv("C:/Users/okada/Desktop/22_立命高等学校/ROI/ROI_left.csv", index_col=None).values.tolist()
# print(csv_file)
# print(csv_file[0])

#data = csv_file.value

subject_number = 0
for row in csv_file:
    subject_number += 1
    movie_name = splitext(basename(movie_path))[0]
    cap = cv2.VideoCapture(movie_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))-1
    # print(frame_count)
    
    Outputlist = [['frame', 'whole_area', 'white_area', 'black_area', 'white_area_ratio']]
    x1 = row[0]
    y1 = row[1]
    x2 = row[2]
    y2 = row[3]
    x3 = row[4]
    y3 = row[5]
    x4 = row[6]
    y4 = row[7]
    n = 0
    while True:
        if n>frame_count:
            #csv出力#####################################################################################
            with open(output_csv_path + movie_name + '_sabun_sub' + str(subject_number) +'.csv', 'w', newline="") as f:
                        writer = csv.writer(f, delimiter=",")
                        writer.writerows(Outputlist)
            #############################################################################################
            break
        ret, frame = cap.read()
        img_trm = frame[int(y1):int(y4), int(x1):int(x4)]
        
        if ret:
            if n == 0:
                I1 = img_trm.copy()
                n += 1
            elif n == 1:
                I2 = img_trm.copy()
                n += 1
            elif n == 2:
                I3 = img_trm.copy()
                n += 1
            else:
                I1=I2.copy()
                I2=I3.copy()
                I3=img_trm.copy()
                
                
                I1_gray = cv2.cvtColor(I1, cv2.COLOR_BGR2GRAY)
                I2_gray = cv2.cvtColor(I2, cv2.COLOR_BGR2GRAY)
                #I3_gray = cv2.cvtColor(I3, cv2.COLOR_BGR2GRAY)
                # cv2.imshow('I1', I1_gray)
                # cv2.imshow('I2', I2_gray)
                # cv2.imshow('I3', I3_gray)
                    
                nowtime = n/30
                    
                    
                    
                #絶対値の求めたのち、背景差分を求める
                img_diff1 = cv2.absdiff(I2_gray,I1_gray)
                #img_diff2 = cv2.absdiff(I3_gray,I2_gray)
                # cv2.imshow('diff1', img_diff1)
                # cv2.imshow('diff2', img_diff2)
                
                
                #論理積を算出するには、bitwise_and()関数
                #Im = cv2.bitwise_and(img_diff1, img_diff2)
                #cv2.imshow('Im', Im)
                
                
                #二値化処理
                img_th = cv2.threshold(img_diff1, threshold, 255, cv2.THRESH_BINARY)[1]
                cv2.imshow('Cropped Image', img_th)
                cv2.imshow('Oroginal Image', img_trm)
                cv2.waitKey(1)

                whole_area = img_th.size
                #print(img_th)
                white_area = cv2.countNonZero(img_th)
                
                black_area = whole_area - white_area
                   
                white_area_ratio = white_area / whole_area * 100
                
                Outputlist.append([n+3, whole_area, white_area, black_area, white_area_ratio])
                n += 1
                if n%30==0:
                    print(n*100/frame_count)

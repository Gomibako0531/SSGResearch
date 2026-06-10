# 動画解析による生徒の授業参加状態数値化システムの開発

## 概要
日本は教員の過重労働が問題となっている国の一つです。本研究は、教員の負担を軽減することを目的として開発されました。システムは二つのプロジェクトにより構成されています。
* **第1プロジェクト:** 教室における出欠を瞬時に取得します。
* **第2プロジェクト:** 教室における授業活動の状況（活発度）を可視化します。

本システムの最大の成果は、プライバシーに配慮しつつ動画解析によって出席をとり、授業中の活発度を可視化することで、教員が今後の授業準備に活用できる点です。

## 使用技術・動作環境
* **プログラミング言語:** Python
* **画像処理手法:** 差分法 (Different image processing)
* **ハードウェア:** iPhone 13 (iOS 16.1.1)、PC (VAIO Windows 9)

## 手法
本研究では、動画処理の差分法を用いています。これはあるフレームにある全ピクセルのフレームごとの輝度の違いから、動きを白ピクセルと黒ピクセルで画像に表す技術です。授業の活発度が高いと白ピクセルの割合は高くなり、逆も同様となります。

### 出席の取得（第1プロジェクト）
* 授業開始時に、録画中のカメラに向かい生徒に手や頭などを振ってもらいます。
* 後に手動で画像上の各座席にROI（Region Of Interest）を設定して人を抽出します。
* ROI内での輝度の違いを計測し、白ピクセルの割合の合計と平均が閾値を上回っていたら出席とカウントします。

### 活発度の可視化（第2プロジェクト）
* 授業（3時間）を、生徒の作ったYouTubeを見る授業、B4、M1、M2それぞれのプレゼンテーションを見る授業の4つのフェーズで構成しました。
* 検出された白ピクセルの数の合計をクラスの活発度とし、算出した値を用いて比較しました。

## 実験結果と考察
* **出欠確認:** ビデオ撮影に1分間、動画の解析に2分間、合計3分かけて出席を取ることができました。
* **活発度の比較:** 授業中の活発度と主観的アンケートを比較しましたが、結果は一致しませんでした。
* **不一致の理由:** 生徒はただ動画を見ていただけの状態や、質問を考えたりプレゼンテーションの準備をしたりする他のアクティビティでは、活発度のアンケート項目の興味関心を反映しなかったからだと考えられます。
* **成果と活用:** 授業における活動や参加度合いである活発度を評価することに成功しました。今後、教員がその数値を見て、次の授業の準備や計画に役立てることができます。
* **課題点:** 金髪の人がいると、金のピクセルが持つ輝度は違いをほとんど持たないため、出席を取るのが難しいことが判明しました。

## 今後の展望
このシステムは小学校、中学校、そして高校で使われ、特に活発的な授業の多い小学校では必要とされると考えています。今後はカメラの設置方法などを改善し、次回は立命館高校の授業で実施する予定です。システム使用後は、教員からフィードバックを得る必要があります。

## 謝辞
ご指導していただいた立命館大学理工学部ロボティクス学科生体工学研究室の岡田志麻教授、文本要氏、山本一天氏、CHOU QIANXU氏に、厚く御礼申し上げます。


# Development of a Student Class Participation Quantification System via Video Analysis

## Overview
Japan is one of the countries where the overwork of teachers is a serious issue. This research was developed with the aim of reducing the burden on teachers. The system consists of two projects:
* **Project 1:** Instantly captures classroom attendance.
* **Project 2:** Visualizes the status of class activities (activity level) in the classroom.

The greatest achievement of this system is that it takes attendance via video analysis while considering privacy, and visualizes the activity level during class, which teachers can utilize for future class preparation.

## Technologies & Environment
* **Programming Language:** Python
* **Image Processing Method:** Difference Image Processing
* **Hardware:** iPhone 13 (iOS 16.1.1), PC (VAIO Windows 9)

## Methodology
This study uses difference image processing for video. This is a technique that represents motion as white and black pixels in an image based on the difference in luminance of all pixels from frame to frame. The higher the class activity level, the higher the percentage of white pixels, and vice versa.

### Taking Attendance (Project 1)
* At the beginning of the class, students are asked to wave their hands or shake their heads toward the recording camera.
* Later, ROIs (Regions of Interest) are manually set for each seat on the image to extract the students.
* The difference in luminance within the ROI is measured, and if the total and average percentage of white pixels exceed the threshold, it is counted as present.

### Visualization of Activity Level (Project 2)
* The 3-hour class was divided into 4 phases: a class watching a YouTube video created by students, and classes watching presentations by B4 (4th-year bachelor's), M1 (1st-year master's), and M2 (2nd-year master's) students.
* The total number of detected white pixels was defined as the class activity level, and the calculated values were used for comparison.

## Results and Discussion
* **Attendance Check:** Attendance could be taken in a total of 3 minutes: 1 minute for video recording and 2 minutes for video analysis.
* **Comparison of Activity Levels:** The activity level during class was compared with a subjective questionnaire, but the results did not match.
* **Reason for Discrepancy:** It is considered that this is because students were just watching a video, or in other activities where they were thinking about questions or preparing for presentations, their physical movements did not reflect the "interest" item of the activity questionnaire.
* **Achievements and Utilization:** We succeeded in evaluating the activity level, which represents the degree of activity and participation in the class. In the future, teachers can look at these figures and use them to prepare and plan for the next class.
* **Challenges:** It was found that if there is a person with blonde hair, it is difficult to take attendance because the luminance of the blonde pixels has almost no difference from the white pixels.

## Future Prospects
This system can be used in elementary, junior high, and high schools, and we believe it is especially needed in elementary schools where there are many active classes. In the future, we plan to improve the camera setup methods and conduct the next trial in a class at Ritsumeikan High School. After using the system, it is necessary to obtain feedback from teachers.

## Acknowledgements
We would like to express our deep gratitude to Professor Shima Okada, Mr. Kanaru Fumimoto, Mr. Itten Yamamoto, and Mr. CHOU QIANXU of the Biophysical Engineering Lab, Department of Robotics, Faculty of Science and Engineering, Ritsumeikan University, for their guidance.

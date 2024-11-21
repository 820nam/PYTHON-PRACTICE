### Python 기본 계산 관련 함수
import numpy as np  # 수학 계산용
import random       # 랜덤 함수용
print(3 + 4**2)                     # 덧셈과 거듭제곱 연산자: 3 + 4^2 = 19
print(np.log(10))                   # 자연 로그 계산 (log_e): ln(10)
print(np.exp(2))                    # 지수 함수 계산 (e^2)
print(np.sqrt(10))                  # 제곱근 계산 (√10)
print(list(range(1, 31)))           # 숫자 나열 (1부터 30까지 생성)
print(sum(range(1, 51)))            # 1부터 50까지 합계
print(np.random.randn(12))          # 평균 0, 표준편차 1 정규분포 난수 생성
print(np.mean(np.random.randn(10))) # 정규분포 난수 10개의 평균
print(random.sample(range(1, 21), 20))  # 1부터 20까지 무작위 섞기
print(max(random.sample(range(1, 21), 20))) # 무작위 값 중 최대값

### mpg 데이터셋 분석 및 시각화
import seaborn as sns
import matplotlib.pyplot as plt
mpg = sns.load_dataset('mpg') # MPG 데이터셋 로드
sns.scatterplot(data=mpg, x='displacement', y='mpg', hue='cylinders', palette='tab10') # 실린더 수로 색상 구분
plt.title("Displacement vs MPG (Color: Cylinders)")
plt.show()

### diamonds 데이터셋 분석 및 시각화
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
diamonds = sns.load_dataset("diamonds") # diamonds 데이터셋 로드

sns.countplot(data=diamonds, x='cut') # 단순 막대 그래프
plt.title("Frequency by Cut")
plt.xlabel("Cut")
plt.ylabel("Count")
plt.show()

sns.countplot(data=diamonds, x='cut', hue='clarity') # clarity별 색상 추가
plt.title("Clarity Distribution by Cut")
plt.xlabel("Cut")
plt.ylabel("Count")
plt.legend(title="Clarity")
plt.show()

sns.countplot(data=diamonds, x='cut', hue='clarity', dodge=True) # clarity별 막대 분리 (dodge)
plt.title("Separated Clarity Bars by Cut")
plt.xlabel("Cut")
plt.ylabel("Count")
plt.legend(title="Clarity")
plt.show()

diamonds['cut_counts'] = diamonds['cut'].map(diamonds['cut'].value_counts()) # 극좌표 그래프
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})  # 극좌표 설정
sns.histplot(data=diamonds, x='cut_counts', hue='cut', multiple='stack', ax=ax)
plt.title("Polar Coordinate Graph (Cut)")
plt.show()

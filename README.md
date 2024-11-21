**PRACTICE.py**

1. 기본 연산 및 통계
   
Python에서 제공하는 기본 수학 연산 및 통계 기능을 활용하여 간단한 계산과 요약 통계를 수행.

지원 기능: 덧셈 및 거듭제곱: +, ** 로그 계산: np.log() 지수 계산: np.exp() 제곱근: np.sqrt()

숫자 나열: range() 합계 및 평균: sum(), np.mean() 정규분포 난수 생성: np.random.randn() 리스트 섞기 및 최대값 찾기: random.sample(), max()

2. Matplotlib & Seaborn 시각화
   
Python의 Seaborn과 Matplotlib 라이브러리를 사용하여 다양한 데이터를 시각화.

산점도 (Scatter Plot): 자동차 배기량과 연비의 관계를 실린더 수를 기준으로 색상으로 구분.

사용 데이터셋: mpg (미국 자동차 연비 데이터).

막대 그래프 (Bar Plot):
다이아몬드 데이터셋을 기반으로 다이아몬드 절단 품질별 빈도수와 투명도(clarity)의 분포를 시각화.

극좌표 그래프 (Polar Coordinate Plot):
다이아몬드 데이터셋의 절단 품질 데이터를 극좌표 형태로 표현.

3. Pandas 데이터 처리 작업

Python의 Pandas 라이브러리를 활용하여 데이터 처리 작업을 수행.

필터링 (Filter):
특정 조건에 따라 데이터를 선택합니다.
예: flights 데이터셋에서 1월 1일 데이터만 필터링.

정렬 (Sort):
특정 열을 기준으로 데이터를 오름차순 또는 내림차순 정렬.
예: 출발 지연 시간(dep_delay)을 기준으로 내림차순 정렬.

열 선택 (Select):
분석에 필요한 특정 열만 선택.
예: year, month, day 열만 선택.

변수 생성 (Mutate):
기존 데이터를 기반으로 새로운 열을 생성.
예: 출발 지연 시간과 도착 지연 시간의 차이를 계산하여 gain 열 생성.

긴 형식 변환 (Pivot Longer):
데이터를 열에서 행으로 변환하여 긴 형식의 데이터를 생성.
예: melt를 사용하여 다중 열 데이터를 하나의 열로 병합.
열 분리 (Separate):

하나의 열에 포함된 정보를 여러 열로 분리.
예: key 열을 _를 기준으로 나누어 새로운 열 생성.

불필요한 열 제거 (Select):
분석에 필요하지 않은 열을 제거하여 데이터 구조를 최적화.

작업	Pandas 함수
필터링 (Filter)	DataFrame.loc[], 조건 필터링
정렬 (Sort)	DataFrame.sort_values()
열 선택 (Select)	DataFrame[['col1', 'col2']]
변수 생성 (Mutate)	DataFrame['new_column'] = ...
긴 형식 변환	DataFrame.melt()
열 분리	str.split(), str.extract()
불필요한 열 제거	DataFrame.drop(columns=...)


**Reference dataset**

**1. mpg 데이터셋**

1.1 내용: 1970년대와 1980년대 자동차 모델의 연비(Miles per Gallon)와 관련된 데이터.

1.2 활용: 배기량(displacement), 연비(mpg), 실린더 수(cylinders), 자동차 제조국(origin) 간의 관계를 분석하고 시각화.

**2. diamonds 데이터셋**

2.1 내용: 다이아몬드의 크기, 품질, 투명도, 가격 정보를 포함한 가상 데이터셋.

2.2 활용: 다이아몬드 특성과 가격(price) 간의 관계를 분석 및 시각화 및 품질(cut)과 투명도(clarity)별 분포를 시각화.

**3. nycflights13 데이터셋**

3.1 내용: 2013년 뉴욕 공항 출발 항공편 데이터를 포함. 각 항공편의 출발 및 도착 시간, 지연 시간, 거리, 항공사 정보 등.

3.2 활용: 항공편의 지연 시간 분석 및 데이터 정리.

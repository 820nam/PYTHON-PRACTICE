import numpy as np  # 수학 계산용
import random       # 랜덤 함수용

### Python 기본 계산 관련 함수
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

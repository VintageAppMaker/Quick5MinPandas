import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patheffects

# 리스트로 데이터프레임 생성
df = pd.DataFrame({
    "이름": ["홍길동", "김유신", "이순신"],
    "나이": [30, 40, 50],
    "성별": ["남", "남", "남"]
})


# 특정 행 
print(">>>특정행")
print("---->" + df[["이름", "성별"][1]])
print(df)

# 행 인덱싱  
print(">>>행 인덱싱")
dfResult = df[0:2]
print(dfResult)

# 열 인덱싱
print(">>>열 인덱싱")
dfResult = df[["이름", "나이"]]
print(dfResult)

# 조건 인덱싱
print(">>>조건 인덱싱")
dfResult = df[df["나이"] < 40]
print(dfResult)

# 산술 연산
print(">>>산술연산")
df["나이"] += 1
print(df)

# 논리 연산
print(">>>논리연산")
dfResult = df[df["나이"] >= 40]
print(dfResult)

# 비교 연산
print(">>>비교연산")
dfResult = df[df[["이름"][0]] == "홍길동"]
print(dfResult)

# 정리
print(">>>정리")
df.describe()

# 히스토그램
print(">>>히스토그램")
df["나이"].hist()

# 상관관계
print(">>>상관관계")
df.corr()
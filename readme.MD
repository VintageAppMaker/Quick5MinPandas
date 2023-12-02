# Pandas로 업무자동화
> 업무자동화(Excel)를 위해서 Pandas의 기초만 학습한다. 

- [예제소스](quickstart_pandas.py)
- [ChatGPT에게 Prompt](ask_chatgpt.MD)

1. 데이터프레임 생성
~~~python
import pandas as pd

# 리스트로 데이터프레임 생성
df = pd.DataFrame({
    "이름": ["홍길동", "김유신", "이순신"],
    "나이": [30, 40, 50],
    "성별": ["남", "남", "남"]
})

~~~

2. 데이터프레임 슬라이싱
데이터프레임의 행과 열을 선택하는 방법

~~~python

# 특정 행 
df[["이름", "성별"][1]]

# 행 인덱싱
df[0:2]

# 열 인덱싱
df[["이름", "나이"]]

# 조건 인덱싱
df[df["나이"] > 40]
~~~

3. 데이터프레임 연산

~~~python

# 산술 연산
df["나이"] += 1

# 논리 연산
df[df["나이"] >= 40]

# 비교 연산
df[df["이름"] == "홍길동"]

~~~

4. 함수

~~~ython
# 요약 통계
df.describe()

# 히스토그램
df["나이"].hist()

~~~

5. 파일로 저장/읽기
~~~python
# CSV 파일로 저장
df.to_csv("data.csv")

# JSON 파일로 저장
df.to_json("data.json")

# Excel 파일로 저장
df.to_excel("data.xlsx")

# CSV 파일로 불러오기
df = pd.read_csv("data.csv")

# JSON 파일로 불러오기
df = pd.read_json("data.json")

# Excel 파일로 불러오기
df = pd.read_excel("data.xlsx")
~~~
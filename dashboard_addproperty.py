import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# 리스트로 데이터프레임 생성
df = pd.DataFrame({
    "이름": ["홍길동", "김유신", "이순신"],
    "나이": [30, 40, 50],
    "성별": ["남", "남", "남"]
})

# 나이가 40세 미만인 경우 붉은색으로 표시하기 위한 색상 설정
df['색상'] = df['나이'].apply(lambda x: 'red' if x < 40 else 'blue')

# Dash 앱 초기화
app = dash.Dash(__name__)

# 그래프 생성
fig = px.bar(df, x='이름', y='나이', title='이름별 나이 비교', color='색상')

# 대시보드 레이아웃 설정
app.layout = html.Div([
    html.H1('이름별 나이 비교'),
    html.Article("이름:"),
    html.Article(df["이름"].map(lambda x: " " + x )),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server(debug=True)
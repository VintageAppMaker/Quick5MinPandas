import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# 샘플 데이터 생성
data = {
    'Fruit': ['Apple', 'Orange', 'Banana', 'Apple', 'Orange', 'Banana'],
    'Amount': [4, 1, 2, 2, 4, 5],
    'City': ['NYC', 'NYC', 'NYC', 'SF', 'SF', 'SF']
}
df = pd.DataFrame(data)

# Dash 애플리케이션 생성
app = dash.Dash(__name__)

# 대시보드 레이아웃
app.layout = html.Div([
    html.H1("Fruit Amount Dashboard"),  # 대시보드 제목

    dcc.Graph(
        id='bar-chart',  # 차트 ID
        figure=px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')  # Plotly 바 차트
    )
])

# 애플리케이션 실행
if __name__ == '__main__':
    app.run_server(debug=True)

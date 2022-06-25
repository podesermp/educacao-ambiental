import string
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import json


def load_data(file_name:string) -> pd.DataFrame:
    with open(file_name) as file:
        data = json.load(file)
    vazao = []
    for i in data['sensor_data']:
        vazao.append(i['vazaoL/m'])
    data={
        "time": range(1,len(vazao)+1),
        "vazaoL/m":vazao
    }
    df = pd.DataFrame(data)
    return df

app = Dash(__name__)

# carregando os dados
torneira_1 = load_data(file_name='torneira-1.json')
torneira_2 = load_data(file_name='torneira-2.json')

#transformando os gráficos
fig_torneira_1 = px.histogram(torneira_1, x="time", y="vazaoL/m", nbins=torneira_1.shape[0])
fig_torneira_2 = px.line(torneira_2, x="time", y="vazaoL/m")


app.layout = html.Div(children=[
    html.H1(children='Dados de consumo de água', style={'text-align': 'center'}),
    
    html.H4(children='''
        Dados de consumo de água na torneira 1
    ''', style={'margin': 0, 'padding': 0}),

    dcc.Graph(
        id='torneira1',
        figure=fig_torneira_1
    ),
    
    html.H4(children='''
        Dados de consumo de água na torneira 2
    ''', style={'margin': 0, 'padding': 0}),
    
    dcc.Graph(
        id='torneira2',
        figure=fig_torneira_2
    ),
    
    html.H4(children='''
        Dados de consumo das torneiras
    ''', style={'margin': 0, 'padding': 0}),
])

if __name__ == '__main__':
    app.run_server(debug=True)
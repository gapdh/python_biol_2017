
# coding: utf-8

# In[ ]:

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

import os

server = app.server
server.secret_key = os.environ.get('SECRET_KEY', 'my-secret-key')

app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Prestiž zaměstnání'),

    html.Div(children='''
        Prestiž zaměstnání v Kanadě v roce 1971
    '''),
    dcc.Markdown('''
#### Data pochází z průzkumu provedeného v Kanadě v roce 1971

**Sledované proměnné**
* Vzdělání: průměrný počet let vzdělání zaměstnanců
* Příjem: průměrný příjem v USD  
* Prestiž: vyjádření prestiže pomocí Pineo-Porterova skóre 
    
**Zdroj dat**
Canada (1971) Census of Canada. Vol. 3, Part 6. Statistics Canada [pp. 19-1–19-21]
'''),
    
    dcc.Graph(
        id='example-graph',
    ),
    dcc.Dropdown(
        options=[
            {'label': 'Závislost prestiže zaměstnání na délce studia', 'value': '1'},
            {'label': 'Závislost výše mzdy na déle studia', 'value': '2'},
            {'label': 'Závislost výše mzdy na poměrném zastoupení žen v jednotlivých zaměstnáních', 'value': '3'},
        ],
        value='1',
        id = 'dropdown-input'
    ),
    dcc.RadioItems(
        options=[
            {'label': 'Skrýt popisky', 'value': 'A'},
            {'label': 'Zobrazit popisky', 'value': 'B'}
        ],
        value='A',
        id='radio-input'
    )
])

@app.callback(
    Output(component_id='example-graph', component_property='figure'),
    [Input(component_id='dropdown-input', component_property='value'),
     Input(component_id='radio-input', component_property='value')]
)
def update_figure(data_type, plot_type):    
  
    
    trace1 = go.Scatter(
        x = prestige.women if data_type == '3' else prestige.education, y = prestige.prestige if data_type == '1' else prestige.income, 
        mode = 'markers' if plot_type == 'A' else 'markers+text', text = (prestige.iloc[:,0]).tolist(), 
        marker = dict(
            color = '#000080', line = dict(width = 1)
    ))
   
    
    data = [trace1]
    
    layout = go.Layout(title='Závislost prestiže zaměstnání na délce studia'if data_type == '1' else 'Závislost výše mzdy na déle studia' if data_type == '2' else 'Závislost výše mzdy na poměrném zastoupení žen v jednotlivých zaměstnáních',
    xaxis=dict(title='podíl zaměstnaných žen (procenta)' if data_type == '3' else 'délka studia (roky)',
        tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='lightgrey'
        )),
    yaxis=dict(title='prestiž (Pineo-Porterovo skóre)' if data_type == '1' else 'výše mzdy (USD)',
               tickfont=dict(
            family='Old Standard TT, serif',
            size=14,
            color='lightgrey'
        )),
        
    )

    figure={
        'data': data,
        'layout': layout,

    }
    return figure

prestige = pd.read_csv('https://raw.githubusercontent.com/vincentarelbundock/Rdatasets/master/csv/car/Prestige.csv')
prestige.columns.values[0] = 'profession'

if __name__ == '__main__':
    app.run_server()


# In[ ]:




# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
colors = {
    'background': '#131312',
    'text': '#7FDBFF'
}

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    html.Button('Submit',
                id='button',
                style={'backgroundColor': '#111111',
                       'color':'white','width':'5%',
                       'height': '50px',
                       'text-align':'center',
                       'marginLeft': '30px',
                       'marginTop': 10
                       }, 
                       
                 ), 
    html.Button('Submit2', id='button2'),
    html.Div(children='Dash: A web application framework for Python.'),
    html.H2(children='test 1 simple layout for dash'),
    html.Div(children='Press CTRL+C to quit'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    )
],
style={'background-image': 'http://rotranslation.com/wp-content/uploads/2018/02/test-300x300.png',
'background-repeat': 'no-repeat',
'background': '#3343B1',
'background-position': 'right top',
'background-size': '150px 100px'} 
    
    
    )

if __name__ == '__main__':
    app.run_server()

import dash
from dash import html, dcc
import plotly.graph_objects as go
import html2dash

def render_tab(df):

    grouped = df[df['total_amt']>0].groupby('Store_type')['total_amt'].sum()

    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Store type'))


    layout = html.Div([html.H1('Pipelines',style={'text-align':'center'}),
                       
                        html.Div([dcc.DatePickerRange(id='pipes-range',
                                                    start_date=df['tran_date'].min(),
                                                    end_date=df['tran_date'].max(),
                                                    display_format='YYYY-MM-DD')], style={'width':'100%','text-align':'center'}),
                        html.Div([dcc.Dropdown(id='prod_dropdown',
                                        options=[{'label':store_type,'value':store_type} for store_type in df['Store_type'].unique()],
                                        value=df['Store_type'].unique()[0])]),
                        html.Div(
                            [html.Div([dcc.Graph(id='bar-pipes')],style={'width':'50%'}),
                            html.Div([dcc.Graph(id='heatmap-pipes', figure=fig)],style={'width':'50%'})],style={'display':'flex'})
                        ])

    return layout
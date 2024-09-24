from dash import Dash, html, dash_table, dcc, Input, Output, callback
import pandas as pd
import numpy as np
import plotly.express as px

# Data
#df = pd.read_csv("/Users/erv/Desktop/python/Dash/data/iris.csv")
df = pd.read_csv('https://raw.githubusercontent.com/learndataa/render_demo/main/iris.csv', on_bad_lines='skip')
dfy = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv', on_bad_lines='skip')

# Initialize app
app = Dash(__name__)
server = app.server

# Layout
app.layout = html.Div(
    children = [
                html.Div("My First Dash Dashboard!",
                         style={'border':'2px solid black',
                                'textAlign':'center',
                                'width':'800px',
                                'height':'20px',
                                'margin':'auto',
                                'padding':'10px',
                                'backgroundColor':'#add8e6',
                                'fontSize':'25px'
                                }
                         ),

                html.Div(
                    children = [
                        dash_table.DataTable(data=df.to_dict('records'),
                                             page_size=5,
                                             style_table={'overflowX':'auto', 'padding':'10x'},
                                             style_header={'backgroundColor':'lightyellow', 'fontWeight':'bold'},
                                             style_cell={'textAlign':'left', 'padding':'10px'}

                        ),


                        dash_table.DataTable(data=df.to_dict('records'),
                                             page_size=5,
                                             style_table={'overflowX':'auto', 'padding':'10x'},
                                             style_header={'backgroundColor':'lightblue', 'fontWeight':'bold'},
                                             style_cell={'textAlign':'left', 'padding':'10px'}
                                             )
                    ], style={'display':'flex',
                              'justifyContent':'space-between',
                              'width':'auto',
                              'height':'auto',
                              'margin':'20px'
                              }
                ),

                html.Div(
                    children = [
                        html.Div(dcc.Graph(figure=px.bar(df, x='name', y='sepal_length').update_layout(margin=dict(l=10,r=10,t=10,b=10),width=300,height=300)), style={'display':'inline-block','width':'300px', 'height':'300px','margin':'20px'}),
                        html.Div(dcc.Graph(figure=px.histogram(df, x='sepal_length').update_layout(margin=dict(l=10,r=10,t=10,b=10),width=300, height=300)), style={'display':'inline-block','width':'300px', 'height':'300px','margin':'20px'}),
                        html.Div(dcc.Graph(figure=px.box(df, x='name', y='sepal_length').update_layout(margin=dict(l=10,r=10,t=10,b=10), width=300, height=300)), style={'display':'inline-block','width':'300px','height':'300px','margin':'20px'})
                    ],
                    #style={'display':'flex',
                    #       'justifyContent':'space-between'}

                ),

                html.Div(
                    children = [
                        #html.Div(
                            dcc.Graph(id='plot_with_slider'),
                            #NOTE: dcc.Slider(min=0, max=20, step=5, value=10, id='my-slider')
                            dcc.Slider(min = dfy['year'].min(),
                                       max = dfy['year'].max(),
                                       step =None,
                                       value = dfy['year'].min(),
                                       marks = {str(year): str(year) for year in dfy['year'].unique()},
                                       id = 'year_slider'
                                       )
                        #)


                    ],
                    style={'border':'2px solid black',
                           #'textAlign':'center',
                           'width':'1000px',
                           'height':'300px'
                           }
                )


    ],
    style={'border':'2px solid black',
           #'textAlign':'center',
           'width':'100%',
           'height':'1200px',
           'margin':'auto',
           'padding':'10px',
           'backgroundColor':'#D3D3D3',
           #'fontSize':'25px'
           }

)

@callback(
    Output('plot_with_slider', 'figure'), # 'figure' required
    Input('year_slider', 'value') # 'value' required
)
def update_figure(selected_year):
    filtered_dfy = dfy[dfy['year'] == selected_year]

    fig = px.scatter(filtered_dfy,
                     x="gdpPercap", y="lifeExp",
                     size="pop", color='continent', hover_name="country",
                     log_x=True, # log scale for x
                     size_max=55 # number of markers
                     )
    fig.update_layout(transition_duration=500) #milliseconds

    return fig

# Run app
if __name__ == "__main__":
    #app.run(debug=True)
    app.run_server(debug=False)


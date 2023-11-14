from dash import Dash, html, dcc, callback, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

my_H1 = html.H1("My Dash App", 
                style={"textAlign": "center", "color": "red", "backgroundColor": "blue"}, 
                className="my-class",
                n_clicks=0,
                )
my_H2 = html.H2("Choose option: ",
                style={"textAlign": "center", "color": "red", "backgroundColor": "blue"}, 
                className="my-class", 
                id="my-h2", 
                n_clicks=0,)
my_dropdown = dcc.Dropdown(options=[{"label": "Option 1", "value": "Option 1"},
                                    {"label": "Option 2", "value": "Option 2"},
                                    {"label": "Option 3", "value": "Option 3"}], 
                        value="Option 1",
                        multi=False,
                        clearable=False,
                        )

df = px.data.gapminder()

my_graph = dcc.Graph(figure=px.scatter(df, x="gdpPercap", 
                                    y="lifeExp", 
                                    color="continent", 
                                    size="pop", 
                                    size_max=60,
                                    hover_name="country",
                                    log_x=True,
                                    animation_frame="year",
                                    animation_group="country",
                                    range_x=[100,100000],
                                    range_y=[25,90],
                                    labels={"gdpPercap": "GDP per capita", "lifeExp": "Life expectancy"}
                                    ))

my_button = html.Button("click me", n_clicks=0, style={"color": "red", 
                                                    "backgroundColor": "blue",
                                                    "borderRadius": "50px",
                                                    "padding": "10px",
                                                    "fontSize": "20px",
                                                    "border": "2px solid green",
                                                    "boxShadow": "10px 10px 5px 0px rgba(0,0,0,0.75)",
                                                    "cursor": "pointer",
                                                    "transition": "all 0.3s ease-in-out",
                                                    ":hover": {"backgroundColor": "red",
                                                                "color": "blue",
                                                                "border": "2px solid green",
                                                                "boxShadow": "0px 0px 5px 0px rgba(0,0,0,0.75)",
                                                                "transform": "scale(1.1)"
                                                                }})

app.layout = html.Div(children=[my_H1, my_H2, my_dropdown, my_graph, my_button])

@callback(
    Output(my_H2, component_property="children"), 
    Input(my_dropdown, component_property="value"))

@callback(
    Output(my_H1, "children"), 
    Input(my_button, "n_clicks"),)

def update_option(option):
    return option

def button_clicked(n):
    return f"Button clicked {n} times"


app.run_server(debug=True)

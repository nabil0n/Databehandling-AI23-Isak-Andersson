from dash import Dash, html, dcc, callback, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

app = Dash(__name__, external_stylesheets=[dbc.themes.DARKLY],
        meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"},],)

my_H1 = html.H1("My Dash App",  
                className="my-class",
                n_clicks=0,
                style={"textAlign": "center",
                    },
                )
my_H2 = html.H2("Choose option: ", 
                className="my-class", 
                id="my-h2", 
                n_clicks=0,
                style={"textAlign": "center",}
                )

my_test = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Input(type="text",
                        placeholder="Firstname: ")),
        dbc.Col(dbc.Input(type="text",
                        placeholder="Lastname: ")),
        dbc.Col(dbc.Input(type="text",
                        placeholder="Email: ")),
    ]),
    dbc.Row([
        dbc.Button("Submit",
                    color="primary",
                    className="sm-1",
                )],
            justify="center",
            )
])

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
                                    labels={"gdpPercap": "GDP per capita", "lifeExp": "Life expectancy"},
                                    template="plotly_dark"
                                    ))

my_button = dbc.Button("click me",
                        n_clicks=0,
                        color="primary",
                        )

app.layout = html.Div(children=[my_H1, my_H2, my_graph, my_button, my_test])

@callback(
    Output(my_H1, "children"), 
    Input(my_button, "n_clicks"),)

def update_option(option):
    return option

def button_clicked(n):
    return f"Button clicked {n} times"


app.run_server(debug=True)

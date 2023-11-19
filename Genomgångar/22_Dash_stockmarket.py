from dash import Dash, dcc, html, Input, Output, callback, dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash_bootstrap_templates import load_figure_template

load_figure_template("darkly")

stocks = pd.read_csv("C:/CodeProd/ITHS/Databehandling-AI23-Isak-Andersson/Data/stocks.csv", parse_dates=["Date"], index_col="Date")

app = Dash(__name__,
        external_stylesheets=[dbc.themes.DARKLY],
        meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"},],
)

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Stockmarket Dashboard", className="text-center text-primary mt-3"),
        ], width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id="single_dropdown", multi=False, searchable=False, 
                className="mb-2",
                options=[stock for stock in stocks["Symbols"].unique()],
                style={"color": "#333"},
                value="AAPL"
            ),
            dcc.Graph(id="volume_graph",
                        figure= {})
        ], xs=12, sm=11, md=10, lg=5),
        
        dbc.Col([
            dcc.Dropdown(
                id="multi_dropdown", multi=True, searchable=False, 
                className="mb-2",
                options=[stock for stock in stocks["Symbols"].unique()],
                style={"color": "#333"},
                value=["AAPL", "MSFT", "MRNA", "BNTX", "PFE"]
            ),
            dcc.Graph(id="closing_graph",
                        figure= {})
        ], xs=12, sm=11, md=10, lg=5),
    ], justify="evenly"),
    dbc.Row([
        dbc.Col([
            dash_table.DataTable(
                stocks.to_dict("records"), 
                id="stock_table", 
                columns=[{"name": i, "id": i} for i in stocks.columns], 
                page_size=10, 
                style_cell={"textAlign": "left", "backgroundColor": "#333", "color": "#fff"}, 
                style_header={"backgroundColor": "#333", "color": "#fff"}, 
                style_data={"backgroundColor": "#333", "color": "#fff"}
                ),
        ], width=12)
    ]),
    
], fluid=True)

@callback(
    Output("volume_graph", "figure"),
    Input("single_dropdown", "value")
)
def update_volume_graph(symbol):
    df = stocks.query("Symbols == @symbol")
    return px.line(df, x=df.index, y="Volume")

@callback(
    Output("closing_graph", "figure"),
    Input("multi_dropdown", "value")
)
def update_closing_graph(symbols):
    if symbols is None: symbols = []
    df = stocks[stocks["Symbols"].isin(symbols)]
    return px.line(df, x=df.index, y="Close", color="Symbols")

app.run(debug=True)
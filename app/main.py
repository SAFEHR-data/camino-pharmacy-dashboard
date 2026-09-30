from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = pd.read_csv("./gapminder_unfiltered.csv")

app = Dash(external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# Requires Dash 2.17.0 or later
app.layout = dbc.Container(
    [
        html.Div(
            [
                html.Img(src=app.get_asset_url("logo.png"), style={"height": "50px"}),
                html.H1(
                    children="Camino Pharmacy Dashboard", style={"textAlign": "center"}
                ),
            ],
            className="d-flex align-items-center justify-content-center gap-3 my-4",
        ),
        dcc.Dropdown(df.country.unique(), "Canada", id="dropdown-selection"),
        dcc.Graph(id="graph-content"),
    ],
    fluid=True,
)


@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x="year", y="pop")


if __name__ == "__main__":
    app.run(debug=True)

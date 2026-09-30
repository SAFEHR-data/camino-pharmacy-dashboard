from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd

df = pd.read_csv("./gapminder_unfiltered.csv")

app = Dash()
server = app.server

# Requires Dash 2.17.0 or later
app.layout = [
    html.Div(
        [
            html.Img(src=app.get_asset_url("logo.png"), style={"height": "50px"}),
            html.H1(
                children="Camino Pharmacy Dashboard", style={"textAlign": "center"}
            ),
        ],
        style={"display": "flex", "alignItems": "center", "justifyContent": "center"},
    ),
    dcc.Dropdown(df.country.unique(), "Canada", id="dropdown-selection"),
    dcc.Graph(id="graph-content"),
]


@callback(Output("graph-content", "figure"), Input("dropdown-selection", "value"))
def update_graph(value):
    dff = df[df.country == value]
    return px.line(dff, x="year", y="pop")


if __name__ == "__main__":
    app.run(debug=True)

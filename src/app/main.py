from dash import Dash, html
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
import duckdb

conn = duckdb.connect("./dev/data/RestrictedAntimicrobials.csv")
df = conn.sql("SELECT SIMPLE_GENERIC, SIMPLE_GENERIC_C FROM file").df()

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
        dag.AgGrid(
            id="data-grid",
            rowData=df.to_dict("records"),
            columnDefs=[{"field": column} for column in df.columns],
            defaultColDef={"sortable": True, "filter": True, "resizable": True},
            columnSize="autoSize",
            dashGridOptions={"pagination": False, "domLayout": "autoHeight"},
            style={"width": "450px", "margin": "0 auto"},
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run(debug=True)

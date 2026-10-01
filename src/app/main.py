from dash import Dash, dash_table, html
import dash_bootstrap_components as dbc
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
        dash_table.DataTable(
            id="data-grid",
            columns=[{"name": column, "id": column} for column in df.columns],
            data=df.to_dict("records"),
            sort_action="native",
            filter_action="native",
            style_table={"width": "fit-content", "margin": "0 auto"},
            style_cell={
                "fontFamily": "var(--bs-font-sans-serif)",
                "fontSize": "0.95rem",
                "color": "var(--bs-body-color)",
                "textAlign": "left",
                "padding": "0.65rem 0.85rem",
            },
            style_header={
                "fontFamily": "var(--bs-font-sans-serif)",
                "fontWeight": "600",
                "color": "var(--bs-emphasis-color)",
                "backgroundColor": "var(--bs-tertiary-bg)",
                "borderBottom": "2px solid var(--bs-border-color)",
            },
            style_cell_conditional=[
                {"if": {"column_id": "SIMPLE_GENERIC"}, "width": "260px"},
                {"if": {"column_id": "SIMPLE_GENERIC_C"}, "width": "180px"},
            ],
        ),
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run(debug=True)

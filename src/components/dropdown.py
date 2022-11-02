from dash import Dash, html, dcc
from dash.dependencies import  Input, Output
from . import ids


def render(app:Dash) -> html.Div:
    all_nations = ["China", "Canada", "South Korea"]

    @app.callback(
        Output(ids.NATION_DROPDOWN, "value"),
        Input(ids.SELELCT_ALL_BUTTON, "n_clicks")
    )
    def select_all(_:int) -> list[str]:
        return all_nations

    return html.Div(
        children=[
            html.H6("Variable"),
            dcc.Dropdown(
                options=[{"label":nation, "value":nation} for nation in all_nations],
                value=all_nations,
                multi = True,
                id = ids.NATION_DROPDOWN
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELELCT_ALL_BUTTON
            )

        ]
    )
import sys
from dash import Dash
from components.layout import create_layout
from dash_bootstrap_components.themes import BOOTSTRAP
def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Eddy Dashboard"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()

    
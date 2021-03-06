import pandas as pd
from dash import Dash, html, dcc, Input, Output

from plotly.express import line


COLORS = {"primary": "#FEDBFF", "secondary": "#D598EB", "font": "#522A61"}

data = pd.read_csv("Task_2_pink_morsel_sales.csv")
data = data.sort_values(by="date")

dashAPP = Dash(__name__)


def generate_figure(chart_data):

    line_chart = line(chart_data, x="date", y="sales ($)", title="Pink Morsel Sales")
    line_chart.update_layout(
        plot_bgcolor=COLORS["secondary"],
        paper_bgcolor=COLORS["primary"],
        font_color=COLORS["font"]
    )
    return line_chart


visualization = dcc.Graph(id="visualization",figure=generate_figure(data))

header = html.H1("Pink Morsel Visualizer",id="header",
    style={
        "background-color": COLORS["secondary"],
        "color": COLORS["font"],
        "border-radius": "20px"
    }
)

region_picker = dcc.RadioItems(["north", "east", "south", "west", "all"],"north",id="region_picker", inline=True)


region_picker_wrapper = html.Div([region_picker], style={ "font-size": "150%"})


@dashAPP.callback(Output(visualization, "figure"),Input(region_picker, "value"))


def update_graph(region):
    if region == "all":
        trimmed_data = data
    else:
        trimmed_data = data[data["region"] == region]

    figure = generate_figure(trimmed_data)
    return figure


dashAPP.layout = html.Div([header,visualization,region_picker_wrapper],
    style={
        "textAlign": "center",
        "background-color": COLORS["primary"],
        "border-radius": "20px"
    }
)

if __name__ == '__main__':



    dashAPP.run_server()

    pass



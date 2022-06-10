from dash import Dash,html, dcc

import pandas as pd


from plotly.express import line 

data = pd.read_csv('Task_2_pink_morsel_sales.csv')
data = data.sort_values(by="date")


dashAPP = Dash(__name__)

line_chart = line(data, x="date", y="sales ($)", title="Pink Morsel Sales")

visualization = dcc.Graph(id= "visualization", figure=line_chart)

header = html.H1("Pink Morsel Visualizer", id="header")

dashAPP.layout = html.Div([header, visualization])



if __name__ == '__main__':

    print(data)
    dashAPP.run_server()


    pass

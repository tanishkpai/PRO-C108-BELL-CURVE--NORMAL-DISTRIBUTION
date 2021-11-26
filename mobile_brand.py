import pandas as pd
import scipy
import plotly.figure_factory as ff

df = pd.read_csv("mobile.csv")
fig = ff.create_distplot([df["Mobile Brand"].tolist()], ["Mobile Brand"], show_hist=false)
fig.show()
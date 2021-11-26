import pandas as pd
import scipy
import plotly.figure_factory as ff

df = pd.read_csv("mobile.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Avg Rating"], show_hist=false)
fig.show()
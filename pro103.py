import pandas as pd
import plotly.express as px

df  = pd.read_csv("Copy+of+data+-+data.csv")
#change the path from your end
fig = px.scatter(df,'date','cases',color='country')
fig.show()

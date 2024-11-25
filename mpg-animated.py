import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('mpg.csv')
df.dropna(inplace=True)

fig = px.scatter(df,
            x="mpg",
            y="horsepower",
            animation_frame="model_year",
            # animation_group="origin",
            size="mpg",
            color="origin",
            hover_name="name",
            size_max=30,
            range_x=[5,50],
            range_y=[0,300])

event = st.plotly_chart(fig, key="mpg", on_select="rerun")

event.selection

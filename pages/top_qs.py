import streamlit as st
import pandas as pd

df = pd.read_csv("notebooks/data.csv")

st.header("Top 15 QS Universities")


st.bar_chart(df, y="Institution Name", x="QS Overall Score", horizontal=True)

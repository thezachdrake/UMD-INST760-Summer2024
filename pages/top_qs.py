import streamlit as st
import pandas as pd

df = pd.read_csv("notebooks/data.csv")
df = df.sort_values("QS Overall Score", ascending=False).head(15)
count_df = df.groupby("Location Full").count()
count_df.rename(columns={"Size":"count"}, inplace=True)
count_df = count_df.sort_values("count", ascending=False)

st.header("Top 15 QS Universities")
st.bar_chart(count_df["count"], horizontal=True)


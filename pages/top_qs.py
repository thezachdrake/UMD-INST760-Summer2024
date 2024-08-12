import streamlit as st
import pandas as pd

df = pd.read_csv("notebooks/data.csv")
# df = df.sort_values("QS Overall Score", ascending=False).head(15)
# df_g = df.groupby("Location Full").value_counts()

# st.header("Top 15 QS Universities")
# st.bar_chart(df, y="Institution Name", x="QS Overall Score")
st.write(df)

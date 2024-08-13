import streamlit as st
import pandas as pd

df = pd.read_csv("notebooks/data.csv")

# Zach Drake
zd_df = df.copy()
st.subheader("Your Name")
st.text("Tell me about your plot")
st.divider()

# Sandra Staub
ss_df = df.copy()
st.subheader("Sandra Staub")
st.text("Tell me about your plot")
st.divider()

# Andrea Murano
am_df = df.copy()
st.subheader("Andrea Murano")
st.text("Tell me about your plot")
am_scored_columns = df.select_dtypes(include=['float64'])
am_score_matrix = am_scored_columns.corr()
st.write(am_score_matrix)
st.divider()

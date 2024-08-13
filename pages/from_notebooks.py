import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(am_score_matrix, ax=ax, cmap="YlOrRd", annot=True)
st.pyplot(fig)
st.divider()

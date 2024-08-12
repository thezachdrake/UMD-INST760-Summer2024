import streamlit as st
import pandas as pd

df = pd.read_csv("notebooks/data.csv")

# Zach Drake
st.subheader("Your Name")
st.text("Tell me about your plot")
st.divider()

# Sandra Staub
st.subheader("Sandra Staub")
st.text("Tell me about your plot")
st.divider()

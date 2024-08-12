import streamlit as st
import pandas as pd

df = pd.read_csv("notebooks/data.csv")

st.subheader("Your Name")
st.text("Tell me about your plot")
st.divider()

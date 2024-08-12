import streamlit as st
import pandas as pd

df = pd.read_csv("notebooks/data.csv")

st.header("Top 15 QS Universities")

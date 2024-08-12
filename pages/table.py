import streamlit as st
import pandas as pd


df = pd.read_csv("notebooks/data.csv")

st.write(df)

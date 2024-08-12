import streamlit as st
import pandas as pd


df = pd.read_csv("notebooks/data.csv")

table_page = st.Page("pages/table.py", title="Raw Table", icon=":material/add_circle:")
name_page = st.Page("pages/names.py", title="Class Names", icon=":material/add_circle:")
pg = st.navigation([table_page, name_page])
st.set_page_config(page_title="Home", page_icon=":material/edit:")
st.title("Welcome!")
pg.run()
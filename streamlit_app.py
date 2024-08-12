import streamlit as st
import pandas as pd


df = pd.read_csv("notebooks/data.csv")

table_page = st.Page("pages/table.py", title="Raw Table", icon=":material/table:")
name_page = st.Page("pages/names.py", title="Class Names", icon=":material/groups:")
pg = st.navigation([table_page, name_page])
st.set_page_config(page_title="UMD INST 760 - S24", page_icon=":material/edit:")
pg.run()

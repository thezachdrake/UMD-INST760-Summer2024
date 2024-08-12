import streamlit as st
import pandas as pd


df = pd.read_csv("notebooks/data.csv")

top_15_page = st.Page("pages/top_qs.py", title="Top 15", icon=":material/trophy:")
submissions_page = st.Page("pages/from_notebooks.py", title="Submissions", icons=":material/assignment:")
table_page = st.Page("pages/table.py", title="Raw Table", icon=":material/table:")
name_page = st.Page("pages/names.py", title="Class Roster", icon=":material/groups:")
pg = st.navigation([top_15_page,submissions_page, table_page, name_page])
st.set_page_config(page_title="UMD INST 760 - S24", page_icon=":material/edit:")
pg.run()

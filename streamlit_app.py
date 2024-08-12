import streamlit as st
import pandas as pd


df = pd.read_csv("notebooks/data.csv")

create_page = st.Page("pages/table.py", title="Raw Table", icon=":material/add_circle:")

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.title("Zach Drake")
#test
st.title("Ivy Roberts")
#test
st.title("Kristen Purvis")
#test
st.title("Victoria Nathaniel")
#test
st.title("Savannah McNair")
#test
st.title("Sue McCarty")
#test
st.title("Lillian Getachew")
#test
st.title("Nuwan Hewabethmage")
#test
st.title("Andrea Murano")
#test
st.title("Sandy Staub")
#added name
st.title("Goutham Patchipulusu")
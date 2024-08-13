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
st.markdown("**An Exploration of Metric Correlation:**")
st.text("The heatmap below displays strong, moderate, and weak correlations between each of the metrics that contributed to the QS score. The metrics that contributed to the QS score include: *Academic Reputation, Employer Reputation, Faculty/Student Ratio, Citations per Faculty, International Faculty Ratio, International Research Network, Employment Outcomes, and Sustainability*.
Strong Positive Correlations: Academic Reputation and Employer Reputation are strongly correlated with each other. Possibly unsurprisingly, there is a strong positive correlation between International Students and International Faculty.
Moderately Positive Correlations: Citations per Faculty member has moderately positive correlations with Academic Reputation and International Research Network. Sustainability shows a moderately positive correlation to Academic Reputation and International Research Network.
Weak Correlation: Overall, Faculty Student Ratio shows the weakest correlation across the board to other metrics.")
am_scored_columns = df.select_dtypes(include=['float64'])
am_score_matrix = am_scored_columns.corr()
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(am_score_matrix, ax=ax, cmap="YlOrRd", annot=True)
st.pyplot(fig)
st.divider()

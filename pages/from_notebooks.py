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
st.markdown("**Employment Outcome Correlations in US and International Schools**")
st.text("Description in progress.")

am_US_schools = am_df['Location'] == 'US'
am_int_schools = am_df['Location'] != 'US'

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
sns.regplot(x='Employment Outcomes', y='Academic Reputation', data=am_df[am_US_schools], ax=axs[0, 0])
axs[0, 0].set_xlabel(' ')
axs[0, 0].set_ylabel('Academic Reputation')
sns.regplot(x='Employment Outcomes', y='Academic Reputation', data=am_df[am_int_schools], ax=axs[0, 1])
axs[0, 1].set_xlabel(' ')
axs[0, 1].set_ylabel(' ')
sns.regplot(x='Employment Outcomes', y='Employer Reputation', data=am_df[am_US_schools], ax=axs[1, 0])
axs[1, 0].set_xlabel('Employment Outcomes')
axs[1, 0].set_ylabel('Employer Reputation')
sns.regplot(x='Employment Outcomes', y='Employer Reputation', data=am_df[am_int_schools], ax=axs[1, 1])
axs[1, 1].set_xlabel(' ')
axs[1, 1].set_ylabel(' ')

plt.subplots_adjust(wspace=0.3, hspace=0.3)
st.pyplot(fig)

st.divider()

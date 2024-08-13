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
st.markdown("**Employment Outcome Reputation Metric Correlations in US and International Schools**")
st.text("Description in progress.")

am_US_schools = am_df['Location'] == 'US'
am_int_schools = am_df['Location'] != 'US'

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
sns.regplot(x='Employment Outcomes', y='Academic Reputation', data=am_df[am_US_schools], ax=axs[0, 0], color='mediumblue', scatter_kws={'s':15})
axs[0, 0].set_title('US Schools', fontsize=15, color='mediumblue', y=1.01, fontweight='bold')
axs[0, 0].set_xlabel('')
axs[0, 0].set_ylabel('')
sns.regplot(x='Employment Outcomes', y='Academic Reputation', data=am_df[am_int_schools], ax=axs[0, 1], color='darkorange', scatter_kws={'s':15})
axs[0, 1].set_title('International Schools', fontsize=15, color='darkorange', y=1.01, fontweight='bold')
axs[0, 1].set_xlabel('')
axs[0, 1].set_ylabel('')
sns.regplot(x='Employment Outcomes', y='Employer Reputation', data=am_df[am_US_schools], ax=axs[1, 0], color='mediumblue', scatter_kws={'s':15})
axs[1, 0].set_xlabel('')
axs[1, 0].set_ylabel('')
sns.regplot(x='Employment Outcomes', y='Employer Reputation', data=am_df[am_int_schools], ax=axs[1, 1], color='darkorange', scatter_kws={'s':15})
axs[1, 1].set_xlabel('')
axs[1, 1].set_ylabel('')
fig.text(0.5, 0, 'Employment Outcomes', ha='center', va='center', fontsize=15)
fig.text(0.08, 0.73, 'Academic Reputation', ha='center', va='center', rotation='vertical', fontsize=12)
fig.text(0.08, 0.28, 'Employer Reputation', ha='center', va='center', rotation='vertical', fontsize=12)

plt.subplots_adjust(wspace=0.3, hspace=0.4)
st.pyplot(fig)
st.divider()


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

sns.regplot(x='employment_outcomes', y='academic_reputation', data=am_df[am_US_schools], ax=axs[0, 0])
axs[0, 0].set_title('US Schools')
axs[0, 0].set_xlabel('')
axs[0, 0].set_ylabel('')
sns.regplot(x='employment_outcomes', y='academic_reputation', data=am_df[am_int_schools], ax=axs[0, 1])
axs[0, 1].set_title('International Schools')
axs[0, 1].set_xlabel('')
axs[0, 1].set_ylabel('')
sns.regplot(x='employment_outcomes', y='employer_reputation', data=am_df[am_US_schools], ax=axs[1, 0])
axs[1, 0].set_xlabel('')
axs[1, 0].set_ylabel('')
sns.regplot(x='employment_outcomes', y='employer_reputation', data=am_df[am_int_schools], ax=axs[1, 1])
axs[1, 1].set_xlabel('')
axs[1, 1].set_ylabel('')
fig.text(0.5, 0.04, 'Employment Outcomes', ha='center', va='center')
fig.text(0.06, 0.5, 'Reputation', ha='center', va='center', rotation='vertical')

plt.subplots_adjust(wspace=0.3, hspace=0.3)
st.pyplot(fig)

st.divider()

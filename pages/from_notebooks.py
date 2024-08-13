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
st.write("##### **Employment Outcome Correlations in US and International Schools**")
st.write("Note that the following description is in progress. The following plots display the correlation between employment outcomes and two strongly correlated factors, academic reputation and employer reputation. The employment outcomes score resulting from US schools shows a positive correlation to academic reputation and employer reputation scores. International schools show a moderately positive correlation between employment outcomes and these two factors. It seems that the concentration of lower scoring international schools with regards to the two factors is affecting the overall relationship to employment outcome. It worth exploring what the relationship would look like if the international schools were limited based on a score threshold in the two factors.")

am_US_schools = am_df['Location'] == 'US'
am_int_schools = am_df['Location'] != 'US'

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
sns.regplot(x='Employment Outcomes', y='Academic Reputation', data=am_df[am_US_schools], ax=axs[0, 0], color='mediumblue', scatter_kws={'s':15})
axs[0, 0].set_title('US Schools', fontsize=18, color='mediumblue', y=1.01, fontweight='bold')
axs[0, 0].set_xlabel('')
axs[0, 0].set_ylabel('')
axs[0, 0].set_facecolor("mistyrose")
sns.regplot(x='Employment Outcomes', y='Academic Reputation', data=am_df[am_int_schools], ax=axs[0, 1], color='darkorange', scatter_kws={'s':15})
axs[0, 1].set_title('International Schools', fontsize=18, color='darkorange', y=1.01, fontweight='bold')
axs[0, 1].set_xlabel('')
axs[0, 1].set_ylabel('')
sns.regplot(x='Employment Outcomes', y='Employer Reputation', data=am_df[am_US_schools], ax=axs[1, 0], color='mediumblue', scatter_kws={'s':15})
axs[1, 0].set_xlabel('')
axs[1, 0].set_ylabel('')
sns.regplot(x='Employment Outcomes', y='Employer Reputation', data=am_df[am_int_schools], ax=axs[1, 1], color='darkorange', scatter_kws={'s':15})
axs[1, 1].set_xlabel('')
axs[1, 1].set_ylabel('')
fig.text(0.5, 0.06, 'Employment Outcomes', ha='center', va='center', fontsize=15)
fig.text(0.07, 0.71, 'Academic Reputation', ha='center', va='center', rotation='vertical', fontsize=15)
fig.text(0.07, 0.29, 'Employer Reputation', ha='center', va='center', rotation='vertical', fontsize=15)

plt.subplots_adjust(wspace=0.3, hspace=0.4)
st.pyplot(fig)
st.divider()

# Ivy Roberts
ir_df = df.copy()
st.subheader("Ivy Roberts")
st.write("In this plot, I discovered from the data that our mystery student will be happiest at a top college in France. This plot shows the top schools in France that align with her ideals.")
st.divider()

# Kristen Purvis
kp_df = df.copy()
st.subheader("Kristen Purvis")
st.write("Our prospective student would like to know if institution size influence international research networks. The student is interested in research and possibly an internship in an international location. In general, the larger the institution, the larger the research network.")

sns.barplot(x= "International Research Network", y="Size", hue="Size", data=kp_df)
plt.show() 
st.divider()

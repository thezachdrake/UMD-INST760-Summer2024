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
st.write("Note that the following description is in progress. The following plots display the correlation between employment outcomes and two other scored factors, academic reputation and employer reputation. The employment outcomes score resulting from US schools shows a positive correlation to academic reputation and employer reputation scores. The apparent strength of these relationships in these plots gives some confidence to the claim that US schools with high academic reputation and employer reputation schools are likely to have a high employment outcome score. The visualizations showing non-US schools do not instill this same confidence, though there is a moderately positive correlation. It would be worth breaking this down by country, as well, but for the sake of the question regarding factors might contribute to future employability of students who attended US and non-US schools, it appears that US schools with high academic reputation and employer reputation scores should be considered.") 

am_US_schools = am_df['Location'] == 'US'
am_int_schools = am_df['Location'] != 'US'

fig, axs = plt.subplots(2, 2, figsize=(10, 10))
sns.regplot(x='Employment Outcomes', y='Academic Reputation', data=am_df[am_US_schools], ax=axs[0, 0], color='cornflowerblue', scatter_kws={'s':10}, line_kws={"color": "navy"})
axs[0, 0].set_title('US Schools', fontsize=18, color='black', y=1.01, fontweight='bold')
axs[0, 0].set_xlabel('')
axs[0, 0].set_ylabel('')
axs[0, 0].set_facecolor("whitesmoke")
sns.regplot(x='Employment Outcomes', y='Academic Reputation', data=am_df[am_int_schools], ax=axs[0, 1], color='mediumpurple', scatter_kws={'s':10}, line_kws={"color": "indigo"})
axs[0, 1].set_title('International Schools', fontsize=18, color='black', y=1.01, fontweight='bold')
axs[0, 1].set_xlabel('')
axs[0, 1].set_ylabel('')
axs[0, 1].set_facecolor("whitesmoke")
sns.regplot(x='Employment Outcomes', y='Employer Reputation', data=am_df[am_US_schools], ax=axs[1, 0], color='cornflowerblue', scatter_kws={'s':10}, line_kws={"color": "navy"})
axs[1, 0].set_xlabel('')
axs[1, 0].set_ylabel('')
axs[1, 0].set_facecolor("whitesmoke")
sns.regplot(x='Employment Outcomes', y='Employer Reputation', data=am_df[am_int_schools], ax=axs[1, 1], color='mediumpurple', scatter_kws={'s':10}, line_kws={"color": "indigo"})
axs[1, 1].set_xlabel('')
axs[1, 1].set_ylabel('')
axs[1, 1].set_facecolor("whitesmoke")
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
#New dataset for all schools in France
France = df[df.Location=="FR"]
France
sns.catplot(x="institution_name", y="2025_rank", data=France, kind="bar")
plt.xlim(0, 3)
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()
st.pyplot(fig)
st.divider()

# Kristen Purvis
kp_df = df.copy()
st.subheader("Kristen Purvis")
st.write("Our prospective student would like to know if institution size influence international research networks. The student is interested in research and possibly an internship in an international location. In general, the larger the institution, the larger the research network.")
fig=plt.figure()
sns.barplot(x= "International Research Network", y="Size", hue="Size", data=kp_df, order=['S', 'M', 'L', 'XL'], ci=None)
st.pyplot(fig)
st.divider()

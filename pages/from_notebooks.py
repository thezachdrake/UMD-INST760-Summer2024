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

# Kristen Purvis
kp_df = df.copy()
st.subheader("Kristen Purvis")
st.write("Our prospective student would like to know if institution size influence international research networks. The student is interested in research and possibly an internship in an international location. In general, the larger the institution, the larger the research network.")
fig=plt.figure()
sns.barplot(x= "International Research Network", y="Size", hue="Size", data=kp_df, order=['S', 'M', 'L', 'XL'], ci=None)
st.pyplot(fig)
st.divider()

# Ivy Roberts
ir_df = df.copy()
st.subheader("Ivy Roberts")
st.write("In this plot, I discovered from the data that our mystery student will be happiest at a top college in France. This plot shows the top schools in France that align with her ideals.")
#create a dataframe just of schools in France
ir_France = ir_df['Location'] == 'FR'
# plot
fig=plt.figure()
sns.barplot(x="Institution Name", y="2025 Rank", data=ir_df[ir_France])
plt.xlim(0, 3)
plt.xticks(rotation=40)
plt.yticks(rotation=0)
st.pyplot(fig)
st.divider()

# Goutham Patchipulusu
pg_df = df.copy()
st.subheader("Goutham Patchipulusu")
st.write("**Universities Size & Environmental Impact**")
st.write("When deciding where to apply, considering a university’s investment in environmental sustainability is key. It reflects the school’s commitment to the planet and offers students a chance to engage in green initiatives and learn about innovative environmental practices within a forward-thinking community.")
size_mapping = {'S': 1, 'M': 2, 'L': 3, 'XL': 4}
pg_df['Size Numeric'] = pg_df['Size'].map(size_mapping)

fig=plt.figure()
ax = sns.barplot(x='Size Numeric', y='Sustainability', hue='Size', data=pg_df, palette='Set2')

for p in ax.patches:
    ax.annotate(format(p.get_height(),'.1f'), (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 9),
                textcoords = 'offset points', fontsize=10, color='black')

ax.set_xlabel('University Size')
ax.set_ylabel('Sustainability Score')
ax.set_title('University Size vs. Sustainability Score')

size_labels = ['', '', '', '']
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(size_labels)
st.pyplot(fig)
st.divider()

# Shanikka Richardson

sr_df = df.copy()
st.subheader("Shanikka Richardson")
st.write("**Academic Reputation and Employment Outcomes by Institution Size**")
st.write("Selecting a university can be overwhelming for graduating HS seniors. With rising tuition costs, higher education is seen as an investment in one's future. With the below plot, I wanted to visualize the relationship between academic reputation and employment outcomes of each insititution.")

# Create selection function on plot
size_options = st.multiselect(
    "Select Institution Sizes to Display:",
    options=sr_df['Size'].unique(),
    default=sr_df['Size'].unique()
)

#Filter based on user selection 
filtered_schools = sr_df[sr_df['Size'].isin(size_options)]

#plot
st.scatter_chart(
    data=filtered_schools,
    x='Academic Reputation',
    y='Employment Outcomes',
    color='Size',
    size='Size',
    width=700,
    height=400,
    use_container_width=True
)
st.divider()

# Josh Hochman

jh_df = df.copy()
st.subheader("Josh Hochman")
st.write("**A deeper dive into Sustainability as a deciding factor in university selection**")
st.write("My explanation will go here soon")

# kp_df = df.copy()
# st.subheader("Kristen Purvis")
# st.write("Our prospective student would like to know if institution size influence international research networks. The student is interested in research and possibly an internship in an international location. In general, the larger the institution, the larger the research network.")
# fig=plt.figure()
# sns.barplot(x= "International Research Network", y="Size", hue="Size", data=kp_df, order=['S', 'M', 'L', 'XL'], ci=None)
# st.pyplot(fig)
# st.divider()



# plot
jh_df['domestic_schools'] = jh_df['Location'] == 'US'
fig=plt.figure()
chicken = sns.boxplot(x="Sustainability",y="Size",data=jh_df)
chicken.set_title("Sustainability Scores Based on School Size")
st.pyplot(fig)

fig=plt.figure()
# sns.boxplot(data=df,x='Sustainability',y='Size',hue='domestic_schools')
squirrel = sns.boxplot(x="Sustainability",y="Size",hue="domestic_schools",data=jh_df)
squirrel.set_title("Sustainability Scores Based on School Size AND Location")
st.pyplot(fig)

# plotSustainabilityScores2.set_title("Sustainability Scores Based on School Size")
# plotRankChanges.set_xticklabels(["Outside of the US","Within the US"])
# plotSustainabilityScores2.set(xlabel="Sustainability Score",ylabel="Size Class")

st.divider()


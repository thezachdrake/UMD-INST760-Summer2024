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
st.write("**Employment Reputation and Outcomes by Institution Size**")

# Create Order
sr_size_order = ['S', 'M', 'L', 'XL']
sr_df['Size'] = pd.Categorical(sr_df['Size'], categories=sr_size_order, ordered=True)

# Color and Size Map
sr_color_map = {'S': '#FF6347', 'M': '#4682B4', 'L': '#32CD32', 'XL': '#FFD700'}  # Example colors
sr_size_map = {'S': 50, 'M': 100, 'L': 150, 'XL': 200}  # Example sizes

sr_df['Color'] = sr_df['Size'].map(sr_color_map)
sr_df['Point Size'] = sr_df['Size'].map(sr_size_map)

# Create selection function on plot
size_options = st.multiselect(
    "Select Institution Sizes to Display:",
    options=sr_df['Size'].cat.categories.tolist(),
    default=sr_df['Size'].cat.categories.tolist()
)

#Filter based on user selection 
filtered_schools = sr_df[sr_df['Size'].isin(size_options)]

#plot in Streamlit
st.subheader("Employment Reputation and Outcomes by Institution Size")
st.scatter_chart(
    data=filtered_schools,
    x='Employer Reputation',
    y='Employment Outcomes',
    color='Size',
    size=None,
    width=700,
    height=400,
    use_container_width=True
)

#plot using  Matplotlib
#fig, ax = plt.subplots()
#for size in sr_size_order:
    subset = sr_df[sr_df['Size'] == size]
    ax.scatter(subset['Employer Reputation'], subset['Employment Outcomes'], 
               s=subset['Point Size'], c=subset['Color'], label=size, alpha=0.6, edgecolors='w', linewidth=0.5)

# ax.set_xlabel('Employer Reputation')
# ax.set_ylabel('Employment Outcomes')
# ax.set_title('Customized Scatter Plot')
# ax.legend(title='Size')
# st.pyplot(fig)
st.divider()



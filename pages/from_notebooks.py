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

# Andrea Murano
am_df = df.copy()
st.subheader("Andrea Murano")
st.write("##### **Employment Outcome Correlations in US and International Schools**")
st.write("The plots below analyze correlations between employment outcomes and other factors in US and International schools. US schools exhibit a strong positive correlation between employment outcomes and both academic and employer reputations. The clustering of the schools with the highest QS Overall Score in the upper right corner suggests that those schools perform well in all three areas. International Schools show a weaker correlation, indicating some variability, though there is an indication of some positive relationships. The same clustering of schools with high QS Overall Scores is seen amongst International Schools as well, meaning that it is likely that these institutions are high performing in all three areas. This suggests that while academic and employer reputations are reliable indicators of employment outcomes in the US, they are less definitive for schools outside of the US. Overall, the findings emphasize the importance of academic reputation and employer reputation in predicting employment outcomes, particularly for US schools.")
am_US_schools = am_df['Location'] == 'US'
am_int_schools = am_df['Location'] != 'US'

fig, axs = plt.subplots(2, 2, figsize=(18, 20))


def emp_outcome_corr(x, y, data, ax, title, color):
    scatter = sns.scatterplot(x=x, y=y, data=data, 
                               hue='QS Overall Score', palette='viridis', 
                               size='QS Overall Score', sizes=(50, 200), 
                               alpha=0.7, edgecolor='none', ax=ax, legend=False)
    
    sns.regplot(x=x, y=y, data=data, 
                scatter=False, ax=ax, color=color)
    
    ax.set_title(title, fontsize=26, color='black', y=1.1, fontweight='bold')
    ax.set_xlabel('Employment Outcomes', fontsize=20, labelpad=15)
    ax.set_ylabel(y, fontsize=20, labelpad=15)
    ax.set_facecolor("whitesmoke")
    

emp_outcome_corr('Employment Outcomes', 'Academic Reputation', am_df[am_US_schools], axs[0, 0], 
                  'US Schools', 'navy')

emp_outcome_corr('Employment Outcomes', 'Academic Reputation', am_df[am_int_schools], axs[0, 1], 
                  'International Schools', 'indigo')

emp_outcome_corr('Employment Outcomes', 'Employer Reputation', am_df[am_US_schools], axs[1, 0], 
                  '', 'navy')

emp_outcome_corr('Employment Outcomes', 'Employer Reputation', am_df[am_int_schools], axs[1, 1], 
                  '', 'indigo')


plt.margins(x=0.1, y=0.1)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.2, wspace=0.2, hspace=0.3)
cbar_ax = fig.add_axes([0.15, 0.11, 0.7, 0.02])

sm = plt.cm.ScalarMappable(cmap='viridis_r', norm=plt.Normalize(vmin=0, vmax=100))
sm.set_array([])
cbar = fig.colorbar(sm, cax=cbar_ax, orientation='horizontal')
cbar.set_label('QS Overall Score', fontsize=20, labelpad=15) 
cbar.ax.tick_params(labelsize=14)  
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
st.write("Let's look at sustainability a bit more. I'm assuming our student really wants to go to a school that's invested in sustainability. We want to see if larger schools are better ranked on sustainability than smaller schools. Let’s look at plots for each of the four sizes, side by side. We want to look at their sustainability scores within each size category, and see if the average sustainability score / spread is better for a particular size category.")

# First plot
jh_df['domestic_schools'] = jh_df['Location'] == 'US'
fig=plt.figure()
chicken = sns.boxplot(x="Sustainability",y="Size",data=jh_df,order=['S', 'M', 'L', 'XL'],width=0.7,gap=0.1,flierprops={"marker": "x"})
chicken.set_title("Sustainability Scores Based on School Size")
chicken.set(xlabel="Sustainability Score",ylabel="Size Class")
st.pyplot(fig)

# Commentary for first plot
st.write("Aha! It appears that the median sustainability score tends to be much lower at small and medium sized schools. 75% of medium schools had a sustainability score below 20, though there are many outliers. Large and XL sized schools have a greater spread in their data, but we can see that their median sustainability scores are 10 points higher, and almost half of their scores are over 20 points higher!")
st.write("What about when we compare domestic vs. international options again?")

# Second plot

fig=plt.figure()
# sns.boxplot(data=df,x='Sustainability',y='Size',hue='domestic_schools')
squirrel = sns.boxplot(x="Sustainability",y="Size",hue="domestic_schools",data=jh_df,order=['S', 'M', 'L', 'XL'],legend="auto",width=0.7,gap=0.1,flierprops={"marker": "x"})
squirrel.set_title("Sustainability Scores Based on School Size AND Location")
squirrel.set(xlabel="Sustainability Score",ylabel="Size Class")
st.pyplot(fig)

# Commentary for second plot
st.write("Oh my! While we see similarity in the median US/OUS values within each size class, there's a very clear difference in the XL schools. It looks like if you've got your heart set on a very large school that values sustainability, you're going to do much better with the US schools; their data is centered on a much higher median and average for the sustainability score.")

# Bottom divider
st.divider()


# Nuwan Hewabethmage
nch_df = df.copy()
st.subheader("Nuwan Hewabethmage")
st.text("The below graph shows how changes in the Ranking of the top 20 schools")
nch_df["2024 Rank"] = pd.to_numeric(nch_df["2024 Rank"],  errors='coerce')
nch_df["2025 Rank"] = pd.to_numeric(nch_df["2025 Rank"],  errors='coerce')

# in the viualization I focused on the top 20 Universities 
top_20_uni = nch_df.head(20).copy()
top_20_uni['rank_change'] = top_20_uni["2024 Rank"] - top_20_uni["2025 Rank"]
st.title("Top 20 Universities Ranking Changes from 2024 to 2025")

# becasuse we are using the stream-lit if we want to show the raw data for the graph we can show this way
if st.checkbox("Show the Raw Data"):
    st.write(top_20_uni)

st.subheader("Bar plot of the Rank Changes")
plt.figure(figsize=(16,8))
sns.barplot(x='rank_change', y='Institution Name', data=top_20_uni, palette='viridis')
plt.title('Changes in Rankings from 2024 to 2025 for Top 20 universities')
plt.xlabel('Rank Change')
plt.ylabel("Universities")

st.pyplot(plt)

st.divider()

# Savannah McNair
import numpy as np

smm_df = df.copy()
st.subheader("Savannah McNair")
st.text("This plot will create a correlation matrix of the numerical variables in this dataset to explore the correlations and potential relationships between variables for further investigation. To aid in investigating which relationships might be useful to look into, I will also add a slider tool to allow the user to select a threshold above which correlations will be highlighted.")

# define columns of interest
cols = ['Academic Reputation','Employer Reputation','Faculty Student','Citations per Faculty','International Faculty','International Students','International Research Network','Employment Outcomes','Sustainability','QS Overall Score']
df_corr = smm_df[cols]

# remove NAs and convert to float to create corr matrix
for col in cols:
    df_corr[col] = pd.to_numeric(df[col].replace('-', np.nan), errors='coerce')
df_corr_num = df_corr.dropna()

# new df for corrs
df_no_nas = df_corr_num[cols].corr()

# plot corr matrix
# update color palette to be reverse rocket for more color range
#fig, ax = plt.subplots(figsize=(10, 8))
#sns.heatmap(df_no_nas, cmap='rocket_r', annot=True, fmt=".2f", ax=ax)
#plt.title("Correlation Matrix of Numerical Variables")

#st.pyplot(fig)

#add in a user selected slider widget
threshold = st.slider('Select Correlation Threshold', min_value=0.0, max_value=1.0, value=0.5, step=0.01)

#mask values below user selected threshold
mask = np.abs(df_no_nas) < threshold

#filtered df
filtered_corr = df_no_nas.copy()
filtered_corr[mask] = np.nan

#plot filtered df corr matrix
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(filtered_corr, cmap='rocket_r', annot=True, fmt=".2f", ax=ax, vmin=-1, vmax=1, annot_kws={"size":10}, linewidths=0.5, linecolor='black')
plt.title(f"Filtered Correlation Matrix (Threshold: {threshold})")

st.pyplot(fig)

st.divider()

# Sue McCarty
sgm_df = df.copy()
st.subheader("Sue McCarty")
st.text("This plot shows the spending on sustainability by colleges")
st.text("broken down by school size. A student interested in sustainability") 
st.text("would prefer a larger school.")
#plot 
pretty_plot = sns.catplot(data=sgm_df, x = 'Size', y = 'Sustainability', order= ["S", "M", "L", "XL"], hue='Size')
st.pyplot(pretty_plot)
#the end
st.divider()

# Sandra Staub
ss_df = df.copy()
st.subheader("Sandra Staub")
st.write("If they are looking for employment in the US after graduation, it makes the most")
st.write("sense to look at US schools, so which ones have the best employer reputation as well as employment outcomes.")
ss_df_us = ss_df[ss_df['Location'] == 'US']
sns.set(style="whitegrid")
# Create scatter plot
plt.figure(figsize=(12, 8))
sns.scatterplot(x="Employer Reputation", y="Employment Outcomes", data=ss_df_us, hue="Size")
# List of specific points to label (Employer Reputation > 90 and Employment Outcomes > 90)
points_to_label = ss_df_us[(ss_df_us['Employer Reputation'] > 90) & (ss_df_us['Employment Outcomes'] > 90)]
# Add labels
for index, row in points_to_label.iterrows():
    plt.annotate(
        row['Institution Name'],
        xy=(row['Employer Reputation'], row['Employment Outcomes']),
        xytext=(row['Employer Reputation'] + 5, row['Employment Outcomes'] + 2),
        arrowprops=dict(facecolor='black', arrowstyle="->"),
        fontsize=7,
        ha='right')
# for index, row in points_to_label.iterrows():
#    plt.text(row['Employer Reputation'], row['Employment Outcomes'], row['Institution Name'], fontsize=5, ha='right')


plt.title("US Schools Employer Stats")
st.pyplot(plt)
st.divider()

# Victoria Nathaniel
vn_df = df.copy()
st.subheader("Victoria Nathaniel")
st.write("Showing the academic reputation, and employment outcomes in USA")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=location_in_us, x='employment_outcomes', y='academic_reputation', hue='size', palette='Set2', alpha=0.7, ax=ax)
ax.set_xlabel('Percentage Employment')
ax.set_ylabel('Academic Reputation')
ax.set_title('Statistical Representation In USA')
ax.legend(title='School Size')
st.pyplot(fig)
st.divider()

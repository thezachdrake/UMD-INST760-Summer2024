import streamlit as st
import pandas as pd

df = pd.read_csv("notebooks/data.csv")
df = df.sort_values("QS Overall Score", ascending=False).head(15)
count_df = df.groupby("Location Full").count()
count_df.rename(columns={"Size":"count"}, inplace=True)
count_df = count_df.sort_values("count", ascending=False)

st.header("Top 15 QS Universities")
st.bar_chart(count_df["count"], horizontal=True)




nch01_df = df.copy()
st.subheader("Nuwan Hewabethmage")
st.text("Tell me about your plot")

nch01_df["2025 Rank"] = pd.to_numeric(nch01_df["2025 Rank"],  errors='coerce')

st.title("University Ranking by Location")


num_institutions = st.sidebar.slider("Number of Top Institutions to Display", min_value=10, max_value=100, value=50)

# Filter the top institutions based on the user's selection
top_institutions = df.nsmallest(num_institutions, '2025 Rank')

# Group by location and calculate the mean rank
location_grouped = top_institutions.groupby('Location')['2025 Rank'].mean().reset_index()

# Plotting the bar plot
st.subheader("Average 2025 Rank by Location")
plt.figure(figsize=(10, 6))
sns.barplot(x='2025 Rank', y='Location', data=location_grouped, palette='viridis')
plt.title(f'Average 2025 Rank for Top {num_institutions} Institutions by Location')
plt.xlabel('Average Rank')
plt.ylabel('Location')

# Display the plot in Streamlit
st.pyplot(plt)

# Optional: Show the raw data
if st.sidebar.checkbox("Show Raw Data"):
    st.write(location_grouped)


st.divider()

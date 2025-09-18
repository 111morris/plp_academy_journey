import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load cleaned data
df = pd.read_csv("metadata.csv")
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
df['year'] = df['publish_time'].dt.year

st.title("CORD-19 Research Papers Explorer")
st.write("Explore COVID-19 related research using the metadata from CORD-19.")

# Sidebar
years = df['year'].dropna().astype(int).unique()
year_range = st.slider("Select year range", int(min(years)), int(max(years)), (2020, 2021))

# Filter data
filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# Show data sample
st.subheader("Sample Data")
st.dataframe(filtered_df[['title', 'journal', 'publish_time']].head(10))

# Plot publications by year
st.subheader("Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(year_counts.index, year_counts.values)
ax.set_title("Publications Over Time")
ax.set_xlabel("Year")
ax.set_ylabel("Count")
st.pyplot(fig)

# Top journals
st.subheader("Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig, ax = plt.subplots()
ax.barh(top_journals.index, top_journals.values)
ax.set_title("Top 10 Journals")
ax.set_xlabel("Number of Papers")
st.pyplot(fig)

# Word Cloud
st.subheader("Title Word Cloud")
titles = ' '.join(filtered_df['title'].dropna().tolist())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)
fig, ax = plt.subplots()
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)


# Data loading and exploration 

import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# load the csv 
df = pd.read_csv("metadata.csv")

print(df.head())

# Dimensions
print("Shape:", df.shape)

# Data types
print(df.dtypes)

# Missing values
print(df.isnull().sum())

# Basic statistics
print(df.describe(include='all'))



# cleaning and preparation 
# Drop rows without titles or publish_time
df = df.dropna(subset=['title', 'publish_time'])

# Convert publish_time to datetime
df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')

# Extract year
df['year'] = df['publish_time'].dt.year

# Add abstract word count
df['abstract_word_count'] = df['abstract'].fillna('').apply(lambda x: len(x.split()))


# data analysis and visualization 
# Count by year 
year_counts = df['year'].value_counts().sort_index()

plt.figure(figsize=(8, 5))
sns.barplot(x=year_counts.index, y=year_counts.values, palette="viridis")
plt.title("Publications by Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.tight_layout()
plt.savefig("publications_by_year.png")
plt.show()


# Top journals

top_journals = df['journal'].value_counts().head(10)

plt.figure(figsize=(10, 6))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="magma")
plt.title("Top 10 Journals")
plt.xlabel("Number of Papers")
plt.tight_layout()
plt.savefig("top_journals.png")
plt.show()


titles = ' '.join(df['title'].dropna().tolist())

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(titles)

plt.figure(figsize=(12, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Word Cloud of Paper Titles")
plt.savefig("title_wordcloud.png")
plt.show()


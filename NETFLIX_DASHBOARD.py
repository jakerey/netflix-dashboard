import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

st.title("🎬 Netflix Data Dashboard")
st.markdown("Explore what's trending on Netflix!")

# Load your cleaned dataset
df = pd.read_csv("netflix_titles.csv")
df['date_added'] = pd.to_datetime(df['date_added'])
df['year_added'] = df['date_added'].dt.year

# Filter by type
type_filter = st.multiselect("Choose Content Type", options=df['type'].unique(), default=df['type'].unique())
filtered_df = df[df['type'].isin(type_filter)]

# Plot content by year
st.subheader("📈 Content Added Over the Years")
yearly = filtered_df['year_added'].value_counts().sort_index()
fig, ax = plt.subplots()
yearly.plot(kind='line', marker='o', ax=ax)
st.pyplot(fig)

# Top genres
st.subheader("🎭 Top Genres on Netflix")
genre_counter = Counter()
filtered_df['listed_in'].dropna().apply(lambda x: genre_counter.update(x.split(', ')))
genres, counts = zip(*genre_counter.most_common(10))
fig, ax = plt.subplots()
sns.barplot(x=list(counts), y=list(genres), ax=ax)
st.pyplot(fig)

# Country breakdown
st.subheader("🌎 Top Countries by Content")
top_countries = filtered_df['country'].value_counts().head(10)
fig, ax = plt.subplots()
top_countries.plot(kind='barh', ax=ax, color='skyblue')
st.pyplot(fig)
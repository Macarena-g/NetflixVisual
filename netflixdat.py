import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
netflix = pd.read_csv(r'C:\Users\MACARENA\OneDrive\Documentos\smarthome\netflix_titles.csv', sep = (','))
fig, axs = plt.subplots(2, 2, figsize=(18, 10))
netflix = netflix.dropna(subset=['country', 'type'])
netflix['main_country'] = netflix['country'].apply(lambda x: x.split(",")[0].strip())
country_type_counts = netflix.groupby(['main_country', 'type']).size().reset_index(name='count')
top_countries = netflix['main_country'].value_counts().head(10)
top_country_names = top_countries.index
filtered = country_type_counts[country_type_counts['main_country'].isin(top_country_names)]
top_genres = netflix['type'].value_counts().head(100)
sns.barplot(data=filtered,ax = axs [0,0],x='main_country',y='count',hue='type',palette= 'Set2' )
axs[0, 0].set_title("Top Countries by Number of Movies and TV Shows", fontsize = 9)
axs[0, 0].tick_params(axis='x', rotation=45)
axs[0, 0].tick_params(axis='x', labelsize=9, colors='gray')
axs[0, 0].tick_params(axis='y', labelsize=9, colors='gray')

sns.countplot(data=netflix, x='release_year', ax=axs[0, 1],
              order=netflix['release_year'].value_counts().index[:10])
axs[0, 1].set_title("Titles by Release Year", fontsize = 9)
axs[0, 1].tick_params(axis='x', rotation=45)
axs[0, 1].tick_params(axis='x', labelsize=9, colors='gray')
axs[0, 1].tick_params(axis='y', labelsize=9, colors='gray')

top_countries.plot(kind='barh', ax=axs[1, 0],color='lightcoral')
axs[1, 0].set_xlabel("Top Countries")
axs[1, 0].invert_yaxis()
axs[1, 0].tick_params(axis='x', labelsize=9, colors='gray')
axs[1, 0].tick_params(axis='y', labelsize=9, colors='gray')

type_counts = netflix['type'].value_counts()
axs[1, 1].pie(type_counts, labels=type_counts.index, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])
axs[1, 1].set_title("Content Type Distribution")

plt.tight_layout()
plt.suptitle("Netflix Data Dashboard", fontsize=15, y=1.00)
plt.show()

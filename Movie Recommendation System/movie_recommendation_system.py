# -*- coding: utf-8 -*-
"""Movie Recommendation System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qDHnHTX9-ZfqKDyy-9WpoYtYnMIRGiF7

# **Movie Recommendation System**

**Recommender** **System** is a system that seeks to predict or filter preferences according to users choices. Recommender systems are utilized in variaty of areas in including movies, music, news, books, research articles, search queries, social tags, and products in general. Recommender Systems produce a list of recommendations in any of the two ways -

**collaborative filtering:** collaborative filtering approaches build a model from the uers past behavior (i.e. items purchased or searched by the user) as well as similar decisions made by other users. this model is then used to predictitems(or ratings for items) that users may have an iterest in.

**content-based filtering:** content based filtering approaches uses a series of discrete characterstics of an item in order to recommend additional items with similar properties. content based filtering methods are totally based on a description of the item and a profile of the users preferences.it recommends items based on the uers past preferences. lets develop a basic recommendation system using python and pandas.

lets develop a basic recommendation system by suggetsing items that are most similar to perticular item, in this case, movies. it just tells what movies/items are most similar to the users movies choice.

# **Import Library**
"""

import pandas as pd

import numpy as np

"""# **Import Dataset**"""

df = pd.read_csv('/content/sample_data/Movies Recommendation.csv')

df

df.head()

df.info()

df.shape

df.columns

"""# **Get Features Selection**"""

df_features = df[['Movie_Genre','Movie_Keywords','Movie_Tagline','Movie_Cast','Movie_Director']].fillna('')

"""Selected five existing features to recommend movies. it may vary from one project to another. Like one can add vote counts, budget, language etc."""

df_features.shape

df_features

x = df_features['Movie_Genre']+' '+df_features['Movie_Keywords']+' '+df_features['Movie_Tagline']+' '+df_features['Movie_Cast']+' '+df_features['Movie_Director']

x

x.shape

"""# **Get Feature Text Conversion to Tokens**"""

from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()

x = tfidf.fit_transform(x)

x.shape

print(x)

"""# **Get Similarity Score using Cosine Simalirity**

cosine_similarity computes the L2 normalized dot product of vectors. Euclidean(L2) normalization projects the vectors onto the unit sphere. and their dot product is then the cosine of the angle between the points denoted by the vectors.
"""

from sklearn.metrics.pairwise import cosine_similarity

Similarity_Score = cosine_similarity(x)

Similarity_Score

Similarity_Score.shape

"""# **Get Movie Name as Input from User and Validate for Closest Spelling**"""

Favourite_Movie_Name = input('Enter your Favourite Movie Name : ')

All_Movies_Title_List = df['Movie_Title'].tolist()

import difflib

Movie_Recommendation = difflib.get_close_matches(Favourite_Movie_Name, All_Movies_Title_List)

print(Movie_Recommendation)

Close_Match = Movie_Recommendation[0]

print(Close_Match)

Index_of_Close_Match_Movie = df[df.Movie_Title==Close_Match]['Movie_ID'].values[0]

print(Index_of_Close_Match_Movie)

# getting a list of similar movies

Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))

print(Recommendation_Score)

len(Recommendation_Score)

"""# **Get ALL Movies Sort Based on Recommendation Score wrt Favourite Movie**"""

# sorting the movies based on their similarity score

Sorted_Similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)

print(Sorted_Similar_Movies)

# print the name of similar movies based on the index

print('Top 30 Movies Suggested for you : \n')
i=1

for movie in Sorted_Similar_Movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if(i<31):
    print(i, '.', title_from_index)
    i+=1

"""# **Top 10 Movie Recommendation System**"""

Movie_Name = input('Enter Your Favourite Movie Name : ')
list_of_all_titles = df['Movie_Title'].tolist()
Find_Close_Match = difflib.get_close_matches(Movie_Name, list_of_all_titles)
Close_Match = Find_Close_Match[0]
Index_of_Movie = df[df.Movie_Title==Close_Match]['Movie_ID'].values[0]
Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))
sorted_similar_movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)
print('Top 10 Movies Suggested for you : \n')
i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.Movie_ID == index]['Movie_Title'].values
  if(i<11):
    print(i, '.', title_from_index)
    i+=1

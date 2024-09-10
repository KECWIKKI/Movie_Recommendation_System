import pandas as pd

data = pd.read_csv("tmdb_movies_data.csv")

data.head()

data.isnull().sum()

data.columns

data = data[['id', 'original_title', 'overview', 'genres']]

data['tags'] = data['overview']+ data['genres']

data1 = data.drop(columns=['overview', 'genres'])

data1

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=10000, stop_words='english')

vectors = cv.fit_transform(data1['tags'].values.astype('U')).toarray()

vectors.shape

from sklearn.metrics.pairwise import cosine_similarity

similar = cosine_similarity(vectors)

data1[data1['original_title'] == 'The Avengers'].index[0]

dis = sorted(list(enumerate(similar[4361])), reverse=True, key=lambda vectors:vectors[1])

for i in dis[0:10]:
  print(data1.iloc[i[0]].original_title)

def picbold(data):
  index = data1[data1['original_title'] == data].index[0]
  dis = sorted(list(enumerate(similar[index])), reverse=True, key=lambda vectors:vectors[1])

  for i in dis[0:10]:
    print(data1.iloc[i[0]].original_title)

picbold('Iron Man')

import pickle

pickle.dump(data1, open('model.pkl', 'wb'))

pickle.dump(similar, open('similar.pkl', 'wb'))


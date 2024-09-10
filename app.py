from flask import Flask, render_template, request, jsonify
import pickle
import requests


app = Flask(__name__)

import json

def fetch_poster(movie_title):
    url = "https://movie-database-alternative.p.rapidapi.com/"
    querystring = {"s": movie_title}
    headers = {
        "x-rapidapi-key": "8502975a8cmsh915d921e0396310p1f4335jsndca2464c54d8",
        "x-rapidapi-host": "movie-database-alternative.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring).text
    
    data = json.loads(response)

    if 'Search' in data and len(data['Search']) > 0:
        poster_path = data['Search'][0]['Poster']
        return poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Poster+Available"

movies = pickle.load(open("model.pkl", 'rb'))
similarity = pickle.load(open("similar.pkl", 'rb'))
movies_list = movies['original_title'].values

@app.route('/')
def index():
    return render_template('index.html', movies=movies_list)

@app.route('/recommend', methods=['POST'])
def recommend():
    movie_title = request.form.get('movie')
    if movie_title not in movies['original_title'].values:
        return jsonify({'error': 'Movie not found'}), 404
    
    index = movies[movies['original_title'] == movie_title].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    
    recommend_movie = []
    recommend_poster = []
    for i in distance[1:7]:
        recommended_movie_title = movies.iloc[i[0]]['original_title']
        recommend_movie.append(recommended_movie_title)
        recommend_poster.append(fetch_poster(recommended_movie_title))
    
    return jsonify({'titles': recommend_movie, 'posters': recommend_poster})

if __name__ == '__main__':
    app.run(debug=True)

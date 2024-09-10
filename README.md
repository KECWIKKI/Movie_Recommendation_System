# Movie Recommendation System

A Movie Recommendation System built using Machine Learning and Flask. The system recommends movies to users based on their preferences, utilizing a pre-trained machine learning model. The model has been trained and serialized into a `.pkl` file for fast and efficient inference. The frontend is developed using HTML and CSS for a seamless user experience.

## Features

- **Personalized Movie Recommendations**: Suggests movies based on user preferences.
- **Machine Learning Model**: A trained model using content-based or collaborative filtering (adjust according to your model).
- **Flask Backend**: Powers the backend, processes requests, and serves the machine learning model.
- **HTML/CSS Frontend**: A simple, responsive user interface.

## How It Works

1. **User Input**: The user selects or inputs their movie preferences on the web interface.
2. **ML Model**: The user input is sent to the backend, where the pre-trained machine learning model processes it.
3. **Recommendations**: The model returns a list of recommended movies, which is then displayed to the user on the frontend.

## Prerequisites

To run this project locally, you need to have the following installed:

- Python 3.x
- Flask
- Pickle (to load the model)
- Any additional libraries listed in `requirements.txt`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/KECWIKKI/movie-recommendation-system.git
   ```
2. Run the python model.py
   ```bash
   python model.py
   ```
   It generated a pickel file for model and similar file
3. Run app.py
   ```bash
   python app.py
   ```

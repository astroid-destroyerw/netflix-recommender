# Flask Movie & TV Show Recommendation App

## Overview

This is a Flask-based web application that provides personalized recommendations for movies and TV shows based on user input. The app suggests a list of media titles using machine learning techniques, similar to how Netflix recommends content to its users.

## Live Demo
Visit the live application at: [Netflix Recommender](https://netflix-recommender.onrender.com)

## Screenshots
### Main Page
Here the user can enter their movie of choice, for example I have entered La Casa De Papel a Spanish Netflix original show.
![](Screenshots/screenshot1.PNG)

### Recommendation Page
Here the user will get recommendations, for example I received Elite(another spanish Netflix original) as my top recommendation
![](Screenshots/screenshot2.PNG)

## Problem Description

Netflix uses a recommendation system called Cinematch to predict user preferences and suggest content accordingly. While Cinematch performs well, there is always room for improvement in prediction accuracy. This project explores alternative approaches to movie and TV show recommendations, aiming to enhance the accuracy of predictions using different models and datasets.

## How It Works

1. Users provide input (e.g., a movie or TV show they like)
2. The system analyzes user preferences and compares them with historical rating data
3. A list of recommended movies/TV shows is generated based on prediction models

## Dataset

This project uses the Netflix Prize Data, which includes anonymous user ratings for thousands of movies. The dataset contains:

- Source: Kaggle - Netflix Prize Data
- Files Used:
  - combined_data_1.txt, combined_data_2.txt, combined_data_3.txt, combined_data_4.txt (contain movie ratings)
  - movie_titles.csv (contains movie title metadata)
- Format:
  - MovieID: (Movie identifier)
  - CustomerID, Rating, Date (User ratings with timestamps)
  - Ratings are on a 1-5 star scale

## Tech Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- Database: SQLite / PostgreSQL (Optional for storing user interactions)
- Machine Learning: Scikit-learn, Pandas, NumPy (for recommendation models)

## Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/astroid-destroyerw/netflix-recommender.git
cd netflix-recommender
```

2. Install Dependencies
```bash
pip install -r requirements.txt
```

3. Run the Flask Application
```bash
python app.py
```

Then, open http://127.0.0.1:5000/ in your browser.

## Future Enhancements

- Implementing collaborative and content-based filtering techniques
- Deploying the app using AWS/GCP
- Enhancing the UI for a better user experience

# Movie Recommendation System

## Live Demo

Try the live application here:

https://movie-recommender-22dchrzerduvs5ydpcnecn.streamlit.app/

The application is fully deployed using Streamlit Cloud and provides movie recommendations in real time.

---

## Project Overview

The Movie Recommendation System is a machine learning application that recommends similar movies using content-based filtering techniques.

The system analyzes movie metadata such as genres, keywords, cast members, and crew information to identify relationships between movies and generate personalized recommendations.

This project demonstrates recommendation systems, natural language processing, feature engineering, and model deployment.

---

## Business Problem

With thousands of movies available across streaming platforms, users often struggle to discover content that matches their interests.

This project addresses that challenge by recommending movies similar to a selected movie, helping users discover relevant content quickly and efficiently.

---

## Dataset

Dataset Source:
TMDB Movie Dataset

Features Used:

* Movie Title
* Genres
* Keywords
* Cast
* Crew
* Overview

Dataset Size:

* 5,000+ movies

---

## Machine Learning Approach

### Content-Based Filtering

The recommendation engine uses content-based filtering.

Movies are represented using metadata such as:

* Genres
* Keywords
* Cast
* Director

These features are combined into a single text representation.

### Text Vectorization

Movie metadata is converted into numerical vectors using:

* CountVectorizer

### Similarity Calculation

Recommendations are generated using:

* Cosine Similarity

Movies with higher similarity scores are returned as recommendations.

---

## System Workflow

1. Load movie dataset
2. Clean and preprocess data
3. Combine important movie features
4. Convert text into vectors
5. Calculate cosine similarity matrix
6. User selects a movie
7. System returns top similar movie recommendations

---

## Features

* Content-based movie recommendations
* Similarity score matching
* TMDB movie poster integration
* Fast recommendation generation
* Interactive Streamlit interface
* Real-time movie suggestions

---

## Technologies Used

| Category             | Tools             |
| -------------------- | ----------------- |
| Programming Language | Python            |
| Data Processing      | Pandas, NumPy     |
| Machine Learning     | Scikit-Learn      |
| NLP                  | CountVectorizer   |
| Similarity Engine    | Cosine Similarity |
| API                  | TMDB API          |
| Frontend             | Streamlit         |
| Deployment           | Streamlit Cloud   |

---

## Project Structure

```text
movie-recommender/
│
├── app.py
├── movies.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
└── screenshots/
```

---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Screenshots

### Home Page

<img width="1921" height="890" alt="Screenshot (175)" src="https://github.com/user-attachments/assets/2a6d9fca-ed9f-419c-97a8-4d2e2c6af434" />
<img width="1917" height="894" alt="Screenshot (179)" src="https://github.com/user-attachments/assets/d82269d1-e883-497b-acc3-f22b0bd91046" />


### Recommendation Results

<img width="1913" height="885" alt="Screenshot (180)" src="https://github.com/user-attachments/assets/a1a554a1-aeb7-4903-9881-f851b5f7c2e2" />

---

## Skills Demonstrated

* Recommendation Systems
* Machine Learning
* Natural Language Processing
* Feature Engineering
* Data Preprocessing
* API Integration
* Model Deployment
* Streamlit Development

---

## Future Improvements

* Hybrid recommendation system
* Collaborative filtering
* User preference tracking
* Personalized recommendations
* Advanced ranking algorithms

---

## Author

Kausar Jahan

Aspiring Machine Learning Engineer

GitHub: https://github.com/Kausarjahan123

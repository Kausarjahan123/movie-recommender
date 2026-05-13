import streamlit as st
import pickle
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Netflix AI Recommender", layout="wide")

# ---------------- NETFLIX UI ---------------- #
st.markdown("""
<style>
.stApp {
    background-color: #0b0f19;
    color: white;
}

/* Title */
h1 {
    text-align: center;
    color: #E50914 !important;
    font-size: 55px;
    font-weight: 900;
}

/* Subheaders */
h2, h3 {
    color: #E50914 !important;
}

/* Buttons */
.stButton > button {
    background-color: transparent;
    color: #E50914;
    border: 1px solid #E50914;
    border-radius: 8px;
    width: 100%;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #E50914;
    color: white;
    transform: scale(1.03);
}

/* remove padding clutter */
.block-container {
    padding: 2rem 3rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #
st.markdown("<h1>NETFLIX AI RECOMMENDER</h1>", unsafe_allow_html=True)

# ---------------- LOAD DATA ---------------- #
movies = pickle.load(open('movies.pkl','rb'))

# ---------------- BUILD MODEL (NO similarity.pkl) ---------------- #
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

# ---------------- POSTER FUNCTION ---------------- #
def fetch_poster(title):
    try:
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "0b729b5ddc03c63ac4e22345966c00f0",   # 🔴 PUT YOUR TMDB KEY HERE
            "query": title
        }

        response = requests.get(url, params=params, timeout=5)
        data = response.json()

        results = data.get("results")

        if results and len(results) > 0:
            poster_path = results[0].get("poster_path")

            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path

    except:
        pass

    return "https://via.placeholder.com/300x450?text=No+Image"


# ---------------- RECOMMEND FUNCTION ---------------- #
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    names = []
    posters = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        names.append(title)
        posters.append(fetch_poster(title))

    return names, posters


# ---------------- SEARCH ---------------- #
movie_list = movies['title'].values
selected_movie = st.selectbox("🔍 Search a movie", movie_list)

if st.button("Show Recommendations"):
    names, posters = recommend(selected_movie)

    st.markdown("---")
    st.markdown(f"## 🎯 Because you watched: {selected_movie}")

    cols = st.columns(5)

    for i in range(len(names)):
        with cols[i % 5]:
            st.image(posters[i], use_container_width=True)
            st.caption(names[i])

# ---------------- HOME GRID ---------------- #
st.markdown("---")
st.markdown("## 🔥 Trending Movies")

cols = st.columns(6)

for i in range(18):
    title = movies.iloc[i].title
    poster = fetch_poster(title)

    with cols[i % 6]:
        st.image(poster, use_container_width=True)
        st.caption(title)

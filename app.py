import streamlit as st
import pickle
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title="Netflix AI", layout="wide")

# Load data
movies = pickle.load(open('movies.pkl','rb'))

# 🔥 REBUILD MODEL INSIDE APP (NO similarity.pkl NEEDED)
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

# TMDB poster fetch
def fetch_poster(title):
    try:
        url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": "0b729b5ddc03c63ac4e22345966c00f0",
            "query": title
        }

        response = requests.get(url, params=params)
        data = response.json()

        # check if results exist
        if data.get("results") and len(data["results"]) > 0:

            poster_path = data["results"][0].get("poster_path")

            if poster_path:
                return "https://image.tmdb.org/t/p/w500" + poster_path

    except:
        pass

    # fallback image (VERY IMPORTANT)
    return "https://via.placeholder.com/300x450?text=No+Image"

# Recommendation function
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    names = []
    posters = []

    for i in movie_list:
        names.append(movies.iloc[i[0]].title)
        posters.append(fetch_poster(movies.iloc[i[0]].title))

    return names, posters


# ---------------- UI ---------------- #

st.markdown(
    "<h1 style='text-align:center;color:#E50914;'>NETFLIX AI RECOMMENDER</h1>",
    unsafe_allow_html=True
)

st.markdown("---")

# 🎬 HOMEPAGE GRID (ALL MOVIES)
st.subheader("🔥 Browse Movies")

cols = st.columns(6)

selected_movie = None

for i in range(18):
    with cols[i % 6]:
        title = movies.iloc[i].title
        poster = fetch_poster(title)

        if st.button(title):
            selected_movie = title

        st.image(poster, use_container_width=True)


# ---------------- RECOMMENDATIONS ---------------- #

if selected_movie:
    st.markdown("---")
    st.subheader(f"🎯 Because you selected: {selected_movie}")

    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i in range(len(names)):
        with cols[i % 5]:
            st.image(posters[i])
            st.caption(names[i])
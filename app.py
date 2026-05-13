import streamlit as st
import pickle
import requests
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE ---------------- #
st.set_page_config(page_title="Netflix CLONE", layout="wide")

# ---------------- NETFLIX CSS ---------------- #
st.markdown("""
<style>
.stApp {
    background-color: #0b0f19;
    color: white;
}

/* Title */
h1 {
    text-align: center;
    color: #E50914;
    font-size: 55px;
    font-weight: 900;
}

/* Netflix row style */
.row {
    display: flex;
    overflow-x: auto;
    padding: 10px 0px;
}

.movie {
    min-width: 160px;
    margin-right: 12px;
    transition: transform 0.3s, box-shadow 0.3s;
}

.movie:hover {
    transform: scale(1.1);
    box-shadow: 0px 0px 15px #E50914;
}

/* scrollbar hide */
.row::-webkit-scrollbar {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown("<h1>NETFLIX AI CLONE</h1>", unsafe_allow_html=True)

# ---------------- DATA ---------------- #
movies = pickle.load(open('movies.pkl','rb'))

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()
similarity = cosine_similarity(vectors)

# ---------------- TMDB ---------------- #
def fetch_poster(title):
    url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": "YOUR_API_KEY",
        "query": title
    }

    try:
        data = requests.get(url, params=params).json()

        if data.get("results"):
            poster = data["results"][0]["poster_path"]
            rating = data["results"][0].get("vote_average", "N/A")
            genre = data["results"][0].get("genre_ids", [])

            return (
                "https://image.tmdb.org/t/p/w500" + poster,
                rating
            )
    except:
        pass

    return "https://via.placeholder.com/300x450", "N/A"


# ---------------- RECOMMEND ---------------- #
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]

    names = []
    posters = []
    ratings = []

    for i in movie_list:
        title = movies.iloc[i[0]].title
        p, r = fetch_poster(title)

        names.append(title)
        posters.append(p)
        ratings.append(r)

    return names, posters, ratings


# ---------------- SEARCH BAR ---------------- #
selected_movie = st.text_input("🔍 Search a movie")

if selected_movie:
    st.markdown("---")
    st.markdown(f"## Results for: {selected_movie}")

    names, posters, ratings = recommend(selected_movie)

    st.markdown('<div class="row">', unsafe_allow_html=True)

    for i in range(len(names)):
        st.markdown(f"""
        <div class="movie">
            <img src="{posters[i]}" width="160">
            <p style="color:white;margin:5px 0;">{names[i]}</p>
            <p style="color:gray;">⭐ {ratings[i]}</p>
            <a href="https://www.youtube.com/results?search_query={names[i]}+trailer" target="_blank">
            🎬 Trailer
            </a>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- NETFLIX ROWS (HOME PAGE) ---------------- #
st.markdown("## 🔥 Trending Now")

cols = st.columns(6)

for i in range(18):
    title = movies.iloc[i].title
    poster, rating = fetch_poster(title)

    with cols[i % 6]:
        st.image(poster, use_container_width=True)
        st.caption(title)
        st.caption(f"⭐ {rating}")

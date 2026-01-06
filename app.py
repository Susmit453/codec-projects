import pickle
import streamlit as st
import requests

st.set_page_config(layout="wide")


@st.cache_data
def load_data():
    movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
    similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))
    return movies, similarity


@st.cache_data(show_spinner=False)
def fetch_poster(movie_id_x):
    url = f"https://api.themoviedb.org/3/movie/{movie_id_x}?api_key=74cf14196e98cd56acaf17a0bfd6deb5&language=en-US"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return None

        data = response.json()
        poster_path = data.get("poster_path")
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
        return None

    except requests.exceptions.RequestException:
        return None


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    names = []
    posters = []

    for i in distances[1:6]:
        movie_id_x = movies.iloc[i[0]]['movie_id_x']
        names.append(movies.iloc[i[0]]['title'])
        posters.append(fetch_poster(movie_id_x))

    return names, posters


st.header("🎬 Movie Recommendation System")

movies, similarity = load_data()

selected_movie = st.selectbox(
    "Select a movie",
    movies['title'].values
)

if st.button("Show Recommendations"):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            if posters[i]:
                st.image(posters[i])
            else:
                st.text("Poster not available")

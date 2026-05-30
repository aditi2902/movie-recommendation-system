import streamlit as st
import pandas as pd
import pickle
import requests

API_KEY = "a6dbfcc3"

movies=pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]
    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies=[]
    recommended_posters = []

    for i in movies_list:
        movie_name=movies.iloc[i[0]].title
        recommended_movies.append(
            movie_name
        )
        recommended_posters.append(
        fetch_poster(movie_name)
        )

    return recommended_movies,recommended_posters
def fetch_poster(movie_name):

    url = f"https://www.omdbapi.com/?t={movie_name}&apikey={API_KEY}"

    data = requests.get(url).json()

    if data.get("Response") == "True":

        return {
            "poster": data.get("Poster"),
            "rating": data.get("imdbRating"),
            "year": data.get("Year")
        }

    return {
        "poster": None,
        "rating": "N/A",
        "year": "N/A"
    }

st.set_page_config(
            page_icon="🎬",
            page_title="Movie Recommender",
            layout="centered"
    )

st.title("🎬 Movie Recommender System")

selected_movie=st.selectbox("Choose a movie",movies['title'].values)
if st.button("Recommend"):

    names, details = recommend(selected_movie)

    cols = st.columns(5)

    for col, name, detail in zip(cols, names, details):

        with col:

            if detail["poster"] and detail["poster"] != "N/A":
                st.image(
                    detail["poster"],
                    use_container_width=True
                )

            st.markdown(f"**{name}**")
            st.write(f"⭐ {detail['rating']}")
            st.write(f"📅 {detail['year']}")
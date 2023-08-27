import streamlit as st
import pandas as pd
import pickle
import os
import requests
st.title('Movie Recommender System')

# pickle_file_path = '../artifacts/movie_dict.pkl'  # Update this with the correct path

# # Check if the pickle file exists
# if os.path.exists(pickle_file_path):
#     # Load the pickle file
#     with open(pickle_file_path, 'rb') as f:
#         movies_list = pickle.load(f)
#     # Process the loaded data as needed
#     print(movies_list)
# else:
#     print("Pickle file not found at the specified path.")


movies_list = pickle.load(open('artifacts\\movie_dict.pkl','rb'))

movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('artifacts\\similarity.pkl','rb'))

def fetch_poster_path(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=a607c2242d7abef5c4240953843874c4&language=en-US".format(movie_id))
    data =response.json()
    return 'https://image.tmdb.org/t/p/w500/'+ data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    m_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]


    recommended_movies =[]
    recommended_movies_poster=[]
    for i in m_list:
        
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster_path(movie_id))
    return recommended_movies,recommended_movies_poster

selected_movie_name = st.selectbox(
'Type or select a movie from the dropdown',
(movies['title'].values))

st.write('You selected:', selected_movie_name)



if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters= recommend(selected_movie_name)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])




import streamlit as st
import pickle
import pandas as pd
import difflib


movies_dict = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))


def show_predict_page():
       
        st.write("Get recommendations based on your favourites!")
        selected_movie_name = st.selectbox(
                "Type in or select",movies['title'].values)
        if st.button('Show Recommendations'):
         global recommendations
         recommendations = recommend(selected_movie_name)

         for m in recommendations:
          st.write(m)



def recommend(movie_name):
         list_of_all_titles = movies['title'].tolist()
         find_close_match = difflib.get_close_matches(movie_name,list_of_all_titles)
         close_match = find_close_match[0]
         index_of_the_movie = movies[movies.title == close_match]['index'].values[0]
         similarity_score = list(enumerate(similarity[index_of_the_movie]))

         sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1],reverse = True)[1:11]
         print('Movies you may like:\n')

         recommended_movies = []
         for i in sorted_similar_movies:
                 index = i[0]
                 recommended_movies.append(movies[movies.index==index]['title'].values[0])
         return recommended_movies
                



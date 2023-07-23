import streamlit as st
from predict_page import show_predict_page
from streamlit_lottie import st_lottie
import requests

st.title("Movie Recommendation System")

def load_lottie(url):
  r = requests.get(url)
  if r.status_code !=200:
      return None
  return r.json()

lottie_icon =   load_lottie("https://assets7.lottiefiles.com/private_files/lf30_bb9bkg1h.json")

col1,col2 = st.columns(2)
with col2:
   st_lottie(lottie_icon)

show_predict_page()
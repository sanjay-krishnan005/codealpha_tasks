import streamlit as st
import pandas as pd
import joblib
import requests
from PIL import Image
from io import BytesIO

# ---------- App Config ----------
st.set_page_config(page_title="🎵 Music Recommender", layout="wide")
st.markdown("<h1 style='text-align: center;'>🎵 Music Recommender System</h1>", unsafe_allow_html=True)

# ---------- Load Data and Model ----------
@st.cache_data
def load_data():
    return pd.read_csv("spotify.csv")

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

df = load_data()
model = load_model()

# ---------- Song Selection ----------
song_list = df['name'].unique().tolist()
selected_song = st.selectbox("Type or select a song from the dropdown", song_list)

if st.button("🎧 Show Recommendation", use_container_width=True):
    st.markdown("---")

    # Get cluster of selected song
    selected_cluster = df[df['name'] == selected_song]['artists'].values[0]

    # Filter songs from same cluster
    recommended_songs = df[(df['artists'] == selected_cluster) & (df['name'] != selected_song)]

    st.markdown("### Recommended Songs:")

    cols = st.columns(5)
    for i, (_, row) in enumerate(recommended_songs.iterrows()):
        with cols[i % 5]:
            try:
                response = requests.get(row['image_url'])
                img = Image.open(BytesIO(response.content))
                st.image(img, use_column_width=True)
            except:
                st.text("")
            st.caption(row['name'])

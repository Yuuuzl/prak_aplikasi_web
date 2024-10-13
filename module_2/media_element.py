import streamlit as st
from PIL import Image

# Image
image = Image.open("Sources/img/Merbabu.jpg")

st.image(image, caption="Merapi Mountain View from Merbabu Mountain", use_column_width=True)

# Audio
audio = open("Sources/sounds/Merbabu.mp3", "rb").read()

st.audio(audio, format="audio/mp3")

# Video
video = open("Sources/video/Merbabu.mp4", "rb").read()

st.video(video, format="video/mp4")

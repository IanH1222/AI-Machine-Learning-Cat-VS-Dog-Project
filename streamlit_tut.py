import streamlit as st

st.set_page_config(page_title="Tab Title")
st.title("Streamlit Tutorial")
st.text("Created by Ian Hernandez")
st.info("This is an info box")
st.success("Success!")
st.error("Error :(")
st.markdown("Hi world")
st.markdown("<h1 style='color': blue;>Hello, World!</h1>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Choose an image...", type=[".jpg", ".jpeg", ".png"])

if uploaded_file:
    st.image(uploaded_file)
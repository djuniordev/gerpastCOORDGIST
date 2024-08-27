import streamlit as st
from PIL import Image

def configPage():
    im = Image.open("./pages/favicon.ico")

    st.set_page_config(layout="wide", page_title="Sistema GERPAST", page_icon=im)

    with open('./pages/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


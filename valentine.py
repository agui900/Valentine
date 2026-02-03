import pathlib
import streamlit as st

st.set_page_config(page_title="Valentine", page_icon="💘", layout="centered")

html_path = pathlib.Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

st.components.v1.html(html, height=800, scrolling=True)

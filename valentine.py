import pathlib
import streamlit as st

st.set_page_config(page_title="Valentine", page_icon="💘", layout="centered")

html_path = pathlib.Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

css_path = pathlib.Path(__file__).with_name("styles.css")
js_path = pathlib.Path(__file__).with_name("script.js")

css = css_path.read_text(encoding="utf-8")
js = js_path.read_text(encoding="utf-8")

html = html.replace(
    '<link rel="stylesheet" href="styles.css" />',
    f"<style>{css}</style>",
)
html = html.replace(
    '<script src="script.js"></script>',
    f"<script>{js}</script>",
)

st.components.v1.html(html, height=800, scrolling=True)

import streamlit as st
from pathlib import Path

st.markdown("# Electromagnetismo Secundario")
st.sidebar.markdown("# Electromagnetismo Secundario") 





def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()

intro_markdown = read_markdown_file("Descripción.md")
st.markdown(intro_markdown, unsafe_allow_html=True)

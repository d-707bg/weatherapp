import streamlit as st
import Test as en
import bg 
hide_deploy = """
    <style>
        header [data-testid="stToolbar"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_deploy, unsafe_allow_html=True)
hide_menu_style = """<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>"""
st.markdown(hide_menu_style, unsafe_allow_html=True)
st.sidebar.title("Навигация")
lang = st.sidebar.radio("Език",["en","bg"])
if lang == "bg":
    bg.main()
elif lang == "en":
    en.main()
import streamlit as st

st.set_page_config(
    page_title="Reddit Depression Detection",
    page_icon="🍀",
    layout="wide"
)

from st_on_hover_tabs import on_hover_tabs
from DetectDepression import show_predict_page
from AnalysisAndResult import show_tabs
from ProjectFlow import show_project_flow

st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Home', 'Project Flow', 'Analysis & Result'], 
                         iconName=['house-fill', 'list-ol', 'layers-fill'], default_choice=0)

if tabs =='Home':
    show_predict_page()

elif tabs == 'Project Flow':
    show_project_flow()

elif tabs == 'Analysis & Result':
    show_tabs()
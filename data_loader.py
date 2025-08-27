import streamlit as st
import pandas as pd


@st.cache_data
def load_data():
    tabela = pd.read_excel("Base.xlsx")
    return tabela

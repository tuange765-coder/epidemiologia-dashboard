import streamlit as st
import pandas as pd

st.set_page_config(page_title="Epidemiología 2026", layout="wide")
st.title("📊 Dashboard Epidemiológico 2026")

# --- SIS PRO ---
@st.cache_data
def cargar_sispro():
    xls = pd.ExcelFile('SIS PRO AÑO 2026.xls')
    df = pd.read_excel(xls, sheet_name='CONSOLIDADO', header=None)
    return df

# --- EPI 12 ---
@st.cache_data
def cargar_epi12():
    df = pd.read_excel('CONSOLIDADO EPI12 2026.xls', sheet_name='EPI 12', header=[8, 9])
    return df

# --- EPI 15 ---
@st.cache_data
def cargar_epi15():
    xls = pd.ExcelFile('CONSOLIDADO EPI15.xlsx')
    df = pd.read_excel(xls, sheet_name='ANUAL', header=None)
    return df

st.header("1. SIS PRO 2026")
try:
    df_sis = cargar_sispro()
    st.write("Forma:", df_sis.shape)
    st.dataframe(df_sis.head(10))
except Exception as e:
    st.error(f"Error: {e}")

st.header("2. EPI 12 2026")
try:
    df_e12 = cargar_epi12()
    st.write("Forma:", df_e12.shape)
    st.dataframe(df_e12.head(10))
except Exception as e:
    st.error(f"Error: {e}")

st.header("3. EPI 15 2026")
try:
    df_e15 = cargar_epi15()
    st.write("Forma:", df_e15.shape)
    st.dataframe(df_e15.head(10))
except Exception as e:
    st.error(f"Error: {e}")

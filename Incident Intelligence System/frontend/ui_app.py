import streamlit as st
import requests
import pandas as pd


API_URL = "http://127.0.0.1:8000"


st.set_page_config(layout="wide")
st.subheader("⚙️ Data Pipeline Control")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("📥 Generate Data"):
        res = requests.get(f"{API_URL}/generate-data")
        st.success(res.json())

with col2:
    if st.button("⚙️ Run Processing"):
        res = requests.get(f"{API_URL}/run-processing")
        st.success(res.json())

with col3:
    if st.button("🔄 Refresh Dashboard"):
        res = requests.get(f"{API_URL}/refresh-powerbi")
        st.info(res.json())


st.markdown("---")
st.subheader("📊 Incident Data")

col1, col2 = st.columns(2)

with col1:
    if st.button("📄 Load All Incidents"):
        res = requests.get(f"{API_URL}/incidents")
        df = pd.DataFrame(res.json())
        st.dataframe(df, use_container_width=True)

with col2:
    if st.button("🚨 Show Critical Incidents"):
        res = requests.get(f"{API_URL}/critical")
        df = pd.DataFrame(res.json())
        st.dataframe(df, use_container_width=True)



st.markdown("---")
st.subheader("⚠️ Data Management")

if st.button("🗑️ Clear Processed Data"):
    res = requests.delete(f"{API_URL}/delete-processed")
    st.warning(res.json())

st.markdown("---")
st.subheader("📊 Power BI Dashboard")


if st.button("🚀 Open Dashboard"):
    st.components.v1.iframe(
        "IFRAMEURL",
        height=900,
        scrolling=True
    )


st.markdown("""
    <style>
    div.stButton > button {
        width: 100%;
        height: 50px;
        font-size: 16px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)
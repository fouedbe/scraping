import streamlit as st
import requests
import time

st.title("تحكم في السكرايبينغ (Backend Flask)")

# Choix des pages à scraper
col0, col1 = st.columns(2)
with col0:
    start_page = st.number_input("Page de départ", min_value=1, max_value=100, value=1)
with col1:
    end_page = st.number_input("Page de fin", min_value=1, max_value=100, value=1)

col2, col3, col4, col5 = st.columns(4)
if col2.button("🚀 Start", key="start_backend"):
    requests.post("http://localhost:5001/start", json={"start_page": int(start_page), "end_page": int(end_page)})
if col3.button("⏸️ Pause", key="pause_backend"):
    requests.post("http://localhost:5001/pause")
if col4.button("▶️ Resume", key="resume_backend"):
    requests.post("http://localhost:5001/resume")
if col5.button("🛑 Stop", key="stop_backend"):
    requests.post("http://localhost:5001/stop")

status = requests.get("http://localhost:5001/status").json()
st.write(f"Progress: {status['progress']} / {status['total']}")
if status["paused"]:
    st.warning("⏸️ السكرايبينغ موقوف مؤقتا")
if status["stopped"]:
    st.error("🛑 السكرايبينغ توقف")

# تحديث تلقائي كل ثانية
time.sleep(1)
st.rerun()

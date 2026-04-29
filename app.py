import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap
from streamlit_js_eval import get_geolocation
import pandas as pd
import numpy as np
import time

st.set_page_config(layout="wide", page_title="RestAI World Monitor", page_icon="📡")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #020202;
        color: #00FF41;
        font-family: 'Share Tech Mono', monospace;
    }
    .stApp { background-color: #020202; }
    .monitor-box {
        background: rgba(0, 20, 0, 0.4);
        border: 1px solid #00FF41;
        padding: 15px;
        box-shadow: inset 0 0 10px #00FF41;
        margin-bottom: 20px;
    }
    .neon-text-green { color: #00FF41; text-shadow: 0 0 5px #00FF41; font-weight: bold; }
    .neon-text-red { color: #FF3131; text-shadow: 0 0 5px #FF3131; font-weight: bold; }
    .neon-text-blue { color: #3182FF; text-shadow: 0 0 5px #3182FF; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

if "location" not in st.session_state:
    st.session_state.location = {"lat": 41.9028, "lon": 12.4964}

with st.sidebar:
    st.title("COMMAND_CENTER")
    if st.button("📡 SCAN MY POSITION"):
        loc = get_geolocation()
        if loc:
            st.session_state.location["lat"] = loc['coords']['latitude']
            st.session_state.location["lon"] = loc['coords']['longitude']
            st.rerun()

lat = st.session_state.location["lat"]
lon = st.session_state.location["lon"]

st.markdown(f"<h1 class='neon-text-green'>RESTAI_WORLD_MONITOR</h1>", unsafe_allow_html=True)

left_col, right_col = st.columns([2, 1])

with left_col:
    m = folium.Map(location=[lat, lon], zoom_start=15, tiles='CartoDB dark_matter')
    folium.Marker([lat, lon], popup="HUB_MAIN", icon=folium.Icon(color='green')).add_to(m)
    st_folium(m, width="100%", height=600)

with right_col:
    st.markdown("<div class='monitor-box'>", unsafe_allow_html=True)
    st.markdown("<p class='neon-text-green'>[ INTEL_SUMMARY ]</p>", unsafe_allow_html=True)
    st.write("✅ PROS: High Quality, Fast Delivery")
    st.write("❌ CONS: High Noise, Small Space")
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='monitor-box'>", unsafe_allow_html=True)
    st.markdown("<p class='neon-text-blue'>[ REVENUE_PREDICTION ]</p>", unsafe_allow_html=True)
    traffic = st.slider("Traffic %", 0, 100, 50)
    st.metric("Potential Revenue", f"{traffic * 1200} RUB")
    st.markdown("</div>", unsafe_allow_html=True)

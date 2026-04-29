import streamlit as st
from streamlit_folium import st_folium
import folium
from folium.plugins import HeatMap
from streamlit_js_eval import get_geolocation
import pandas as pd
import numpy as np
import time


# --- ИНИЦИАЛИЗАЦИЯ И СТИЛЬ ---
st.set_page_config(layout="wide", page_title="RestAI World Monitor", page_icon="📡")


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&display=swap');


    /* Глобальный стиль Terminal/Cyber */
    html, body, [data-testid="stAppViewContainer"] {
        background-color: #020202;
        color: #00FF41;
        font-family: 'Share Tech Mono', monospace;
    }
    
    .stApp { background-color: #020202; }
    
    /* Стилизация карточек под мониторы */
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


    /* Удаление стандартных отступов Streamlit */
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; gap: 10px; }
    .stTabs [data-baseweb="tab"] { border: 1px solid #333; padding: 10px; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# --- ЛОГИКА ГЕОЛОКАЦИИ ---
if "location" not in st.session_state:
    st.session_state.location = {"lat": 41.9028, "lon": 12.4964}


with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2563/2563062.png", width=80)
    st.title("COMMAND_CENTER")
    if st.button("📡 SCAN MY POSITION"):
        loc = get_geolocation()
        if loc:
            st.session_state.location["lat"] = loc['coords']['latitude']
            st.session_state.location["lon"] = loc['coords']['longitude']
            st.success("COORDINATES LOCKED")


lat, lon = st.session_state.location["lat"], st.session_state.location["lon"]


# --- ШАПКА МОНИТОРА ---
c1, c2, c3 = st.columns([2, 2, 1])
with c1:
    st.markdown(f"<h1 class='neon-text-green'>RESTAI_WORLD_MONITOR v3.0</h1>", unsafe_allow_html=True)
with c2:
    st.markdown(f"<p style='margin-top:25px;'>LAT: {lat} | LON: {lon} | STATUS: <span class='neon-text-green'>SECURE</span></p>", unsafe_allow_html=True)
with c3:
    st.button("REBOOT_SYSTEM")


st.markdown("---")


# --- ОСНОВНОЙ МОНИТОР ---
left_col, right_col = st.columns([2, 1])


with left_col:
    st.markdown("<p class='neon-text-blue'>[ TACTICAL_MAP_VIEW ]</p>", unsafe_allow_html=True)
    m = folium.Map(location=[lat, lon], zoom_start=15, tiles='CartoDB dark_matter', control_scale=True)
    
    # Зоны влияния (Heatmap)
    heat_data = [[lat+0.002, lon+0.002, 0.5], [lat-0.001, lon-0.003, 0.8]]
    HeatMap(heat_data).add_to(m)


    # Маркеры объектов
    folium.Marker([lat, lon], popup="HUB_MAIN", icon=folium.Icon(color='green', icon='home')).add_to(m)
    folium.Circle([lat+0.001, lon+0.001], radius=200, color='#FF3131', fill=True, popup="COMPETITOR_ZONE").add_to(m)
    folium.Marker([lat-0.002, lon+0.001], popup="OFFICE_CENTER_DELTA", icon=folium.Icon(color='blue', icon='briefcase')).add_to(m)
    
    st_folium(m, width="100%", height=600)


with right_col:
    # 1. AI REVIEWS (SUMMARIZATION)
    st.markdown("<div class='monitor-box'>", unsafe_allow_html=True)
    st.markdown("<p class='neon-text-green'>[ AI_REVIEW_SUMMARY ]</p>", unsafe_allow_html=True)
    col_p, col_m = st.columns(2)
    with col_p:
        st.markdown("<p class='neon-text-green'>STRENGTHS:</p>", unsafe_allow_html=True)
        st.caption("- Fast Kitchen\n- Interior Vibes\n- Craft Cocktails")
    with col_m:
        st.markdown("<p class='neon-text-red'>THREATS:</p>", unsafe_allow_html=True)
        st.caption("- Wait Times\n- Music Volume\n- Price/Value")
    st.markdown("</div>", unsafe_allow_html=True)


    # 2. PROXIMITY INTEL
    st.markdown("<div class='monitor-box'>", unsafe_allow_html=True)
    st.markdown("<p class='neon-text-blue'>[ PROXIMITY_INTEL ]</p>", unsafe_allow_html=True)
    st.write(f"🏢 **OFFICES**: 1,200 employees within 500m")
    st.write(f"🏨 **HOTELS**: 350 keys (82% occupancy)")
    st.write(f"⚔️ **COMPETITORS**: 4 active units found")
    st.markdown("</div>", unsafe_allow_html=True)


    # 3. REVENUE PREDICTOR (Креативная функция)
    st.markdown("<div class='monitor-box'>", unsafe_allow_html=True)
    st.markdown("<p class='neon-text-green'>[ REVENUE_PREDICTOR ]</p>", unsafe_allow_html=True)
    base_traffic = st.slider("Traffic Level (%)", 0, 100, 65)
    conversion = 0.05 # 5% заходящих в ресторан
    avg_check = 1200
    potential_revenue = (1200 * base_traffic * conversion) * avg_check / 100
    
    st.metric("EST. REVENUE (LUNCH)", f"{potential_revenue:,.0f} RUB", "+12% vs LW")
    st.progress(base_traffic / 100)
    st.markdown("</div>", unsafe_allow_html=True)


# --- НИЖНИЙ СКАНЕР (DATA TICKER) ---
st.markdown("---")
ticker_cols = st.columns(4)
data_points = ["WEATHER: CLEAR (+5% Walk-in)", "COMPETITOR: 'Pasta_Hub' - SALE DETECTED", "HOTEL_ARRIVALS: 45 GUESTS", "ALERT: LUNCH PEAK STARTING"]


for i, col in enumerate(ticker_cols):
    with col:
        st.markdown(f"<div style='border-left: 2px solid #00FF41; padding-left: 10px; font-size: 11px;'>{data_points[i]}</div>", unsafe_allow_html=True)


# Имитация живых данных
time.sleep(0.1)


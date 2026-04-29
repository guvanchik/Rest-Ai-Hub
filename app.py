import streamlit as st
from streamlit_folium import st_folium
import folium

# --- CONFIG & THEME ---
st.set_page_config(layout="wide", page_title="RestAI Hub", page_icon="🟢")

# Custom CSS for the Palantir / Cyber Vibe
st.markdown("""
<style>
    /* Main Background */
    .stApp {
        background-color: #050505;
        color: #e0e0e0;
    }
    
    /* Custom Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: rgba(10, 10, 10, 0.95);
        border-left: 1px solid #333;
        min-width: 400px !important;
    }

    /* Neon Borders and Tickers */
    .intel-box {
        border-left: 3px solid #22c55e;
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        margin-bottom: 10px;
        font-family: 'Courier New', Courier, monospace;
    }
    
    .spy-report {
        border: 1px solid #3b82f6;
        background: rgba(59, 130, 246, 0.05);
        padding: 15px;
        border-radius: 5px;
    }

    .directive {
        color: #3b82f6;
        font-weight: bold;
        text-transform: uppercase;
        font-size: 0.8rem;
    }

    .neon-text {
        color: #22c55e;
        text-shadow: 0 0 10px #22c55e;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- MOCK DATA ---
restaurant_data = {
    "name": "Trattoria Al Forno",
    "location": "Rome, Sector 01",
    "intel": [
        "🟢 Footfall Spike Imminent (+22%)",
        "🔵 Rain Detected - Delivery Up 18%",
        "🔴 Competitor 'Roma Pasta' Active"
    ],
    "pros": ["Handmade Rigatoni", "Fast Turnaround", "Affordable Wine"],
    "cons": ["Acoustics/Noise", "Limited Seating", "Cash-only"],
    "directive": "INCREASE 'COZY DATE NIGHT' ADS. DEPLOY 15% DISCOUNT FOR GROUPS OF 2 TO OFFSET NOISE COMPLAINTS."
}

# --- TOP NAVIGATION ---
col1, col2 = st.columns([1, 3])
with col1:
    st.markdown("<h1 style='margin-top:-20px;'>RESTAI <span style='color:#22c55e'>HUB</span></h1>", unsafe_allow_html=True)
with col2:
    st.text_input("", placeholder="EXECUTE_GLOBAL_SEARCH...", label_visibility="collapsed")

# --- MAIN LAYOUT ---
# We use two columns: Left for Map, Right for Data
map_col, data_col = st.columns([2, 1])

with map_col:
    # Create the Folium Map
    m = folium.Map(location=[41.9028, 12.4964], zoom_start=15, tiles='CartoDB dark_matter')
    
    # Custom Neon Marker
    folium.CircleMarker(
        location=[41.9028, 12.4964],
        radius=10,
        color="#22c55e",
        fill=True,
        fill_color="#22c55e",
        fill_opacity=0.7,
        popup="Trattoria Al Forno - ACTIVE"
    ).add_to(m)
    
    # Display Map
    st_folium(m, width=1100, height=700)

with data_col:
    st.markdown(f"### {restaurant_data['name']}")
    st.markdown(f"<p style='font-family:monospace; color:#666;'>{restaurant_data['location']}</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Intelligence Feed
    st.markdown("<p style='font-size:10px; font-family:monospace;'>INTELLIGENCE_FEED</p>", unsafe_allow_html=True)
    for note in restaurant_data['intel']:
        st.markdown(f"<div class='intel-box'>{note}</div>", unsafe_allow_html=True)
    
    # Spy Report
    st.markdown("<p style='font-size:10px; font-family:monospace; margin-top:20px;'>SPY_REPORT (AI_ANALYSIS)</p>", unsafe_allow_html=True)
    with st.container():
        st.markdown("<div class='spy-report'>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("<p style='color:#22c55e; font-size:11px;'>PROS</p>", unsafe_allow_html=True)
            for p in restaurant_data['pros']: st.markdown(f"- {p}")
        with c2:
            st.markdown("<p style='color:#ef4444; font-size:11px;'>CONS</p>", unsafe_allow_html=True)
            for c in restaurant_data['cons']: st.markdown(f"- {c}")
        
        st.markdown(f"<p class='directive'>System Directive:</p><p style='font-size:12px;'>{restaurant_data['directive']}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # Social Sticker
    st.markdown("<p style='font-size:10px; font-family:monospace; margin-top:20px;'>SOCIAL_ASSET</p>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c", caption="Review Analysis: Rigatoni Carbonara")
    st.button("EXPORT_FOR_INSTAGRAM", use_container_width=True)

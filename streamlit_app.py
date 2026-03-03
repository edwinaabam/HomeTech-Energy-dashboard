import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="HomeTech SmartSense Dashboard",
    page_icon="⚡",
    layout="wide",
)

# --- CUSTOM CSS FOR ENERGY THEME ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    .stMetric {
        background-color: #ffffff;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    .banner {
        background: linear-gradient(90deg, #2e7d32 0%, #1b5e20 100%);
        padding: 2rem;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER BANNER ---
st.markdown("""
    <div class="banner">
        <h1>🏠 HomeTech SmartSense Platform</h1>
        <p>Optimizing Rental Unit Efficiency through IoT & Data Analytics</p>
    </div>
    """, unsafe_allow_html=True)

# --- EMBEDDED EXCEL DASHBOARD ---
st.subheader("Interactive Excel Dashboard")

excel_embed_url = "https://1drv.ms/x/c/62ed36bcf96b63c6/IQTReiVIWbsOS5OupYuHIIlIAdvsv_naDcjm9k72CfGl7qk"

components.html(
    f"""
    <iframe src="{excel_embed_url}"
    width="100%"
    height="950"
    frameborder="0"
    scrolling="yes">
    </iframe>
    """,
    height=950,
)

# --- FOOTER ---
st.divider()
st.caption("© 2026 HomeTech Solutions | Scottsdale, AZ | SmartSense Data Analytics Portal")
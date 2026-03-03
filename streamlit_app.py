import streamlit as st
import streamlit.components.v1 as components

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="HomeTech SmartSense Dashboard",
    page_icon="⚡",
    layout="wide", 
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Main background */
    .stApp {
        background-color: #F0F2F6;
    }

    /* Soft Navy Banner - Centered & Slim */
    .banner {
        background-color: #2C3E50;   /* Executive Navy */
        padding: 1.2rem;             /* Balanced padding */
        border-radius: 10px;
        color: white;
        text-align: center;          /* Centering text */
        margin-top: 1rem;
        margin-bottom: 2rem;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .banner h1 {
        margin: 0;
        font-size: 1.6rem; 
        font-weight: 700;
        color: white !important;
        letter-spacing: 1px;
    }

    .banner p {
        margin: 0.3rem 0 0 0;
        font-size: 0.95rem;
        opacity: 0.85;
        font-weight: 300;
    }

    /* Hide Sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Top margin to prevent cut-off */
    .block-container {
        padding-top: 2.5rem !important; 
        max-width: 95%; 
    }
    </style>
""", unsafe_allow_html=True)

# --- CENTERED HEADER ---
st.markdown("""
    <div class="banner">
        <h1>HomeTech SmartSense Platform</h1>
        <p>IoT Energy & Property Analytics Portal</p>
    </div>
""", unsafe_allow_html=True)

# --- EMBED EXCEL ---
excel_embed_url = "https://1drv.ms/x/c/62ed36bcf96b63c6/IQTReiVIWbsOS5OupYuHIIlIAdvsv_naDcjm9k72CfGl7qk?em=2&wdHideGridlines=True&wdHideHeaders=True&wdDownloadButton=False"

components.html(
    f"""
    <div style="display: flex; justify-content: center; width: 100%;">
        <div style="width: 100%; max-width: 1250px; overflow: hidden; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.05);">
            <iframe 
                src="{excel_embed_url}"
                width="100%" 
                height="800" 
                frameborder="0" 
                scrolling="no" 
                style="border: none; background-color: white;">
            </iframe>
        </div>
    </div>
    """,
    height=810,
)

# --- FOOTER ---
st.markdown("<div style='text-align: center; margin-top: 2rem;'>", unsafe_allow_html=True)
st.divider()
st.caption("© 2026 HomeTech Solutions | Data Integrity Verified")
st.markdown("</div>", unsafe_allow_html=True)
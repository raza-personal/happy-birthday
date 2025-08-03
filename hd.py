import streamlit as st
import time

st.set_page_config(page_title="🎉 Happy Birthday!", layout="wide")

# ---- CSS: Background, Centering, Styling ----
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Caveat:wght@500&display=swap');

    html, body, .main {
        height: 100%;
        margin: 0;
        padding: 0;
        background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .block-container {
        padding-top: 0rem !important;
    }

    .overlay {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 3rem 2rem;
        border-radius: 15px;
        margin: 2rem auto;
        max-width: 1000px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    h1 {
        text-align: center;
        font-family: 'Pacifico', cursive;
        color: #d63384;
        margin-top: 0 !important;
        font-size: 3.5rem;
        line-height: 1.2;
    }

    p {
        text-align: center;
        font-size: 22px;
        font-family: 'Caveat', cursive;
        color: #6f42c1;
    }

    .button-container {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 30px;
        gap: 15px;
        flex-wrap: wrap;
    }

    .stButton>button {
        font-size: 20px;
        padding: 0.7em 1.5em;
        border-radius: 12px;
        background-color: #ff66cc;
        color: white;
        border: none;
        transition: all 0.3s ease-in-out;
        font-family: 'Caveat', cursive;
    }

    .stButton>button:hover {
        background-color: #ff1493;
        transform: scale(1.08);
    }
    </style>
""", unsafe_allow_html=True)

# ---- Overlay Wrapper ----
st.markdown('<div class="overlay">', unsafe_allow_html=True)

# ---- Static Header and Message ----
st.markdown("<h1>🎉 Happy Birthday! 🎂</h1>", unsafe_allow_html=True)
st.markdown("<p>Wishing you a day filled with love, laughter, and everything you enjoy the most! 💖✨</p>", unsafe_allow_html=True)

# ---- Session State for Step Control ----
if "step" not in st.session_state:
    st.session_state.step = 0

# ---- Step 0: Intro Button ----
if st.session_state.step == 0:
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    if st.button("💌 Make it more special"):
        st.session_state.step = 1
    st.markdown('</div>', unsafe_allow_html=True)

# ---- Step 1: First Video ----
if st.session_state.step >= 1:
    st.video("video1.mp4")
    time.sleep(1)
    st.markdown("<p style='font-size:24px;'>🌟 It is not over yet...</p>", unsafe_allow_html=True)

    if st.session_state.step == 1:
        st.markdown('<div class="button-container">', unsafe_allow_html=True)
        if st.button("🎁 See more"):
            st.session_state.step = 2
        st.markdown('</div>', unsafe_allow_html=True)

# ---- Step 2: Final Video & Message ----
if st.session_state.step >= 2:
    st.video("video2.mp4")
    time.sleep(1)
    st.markdown("""
        <p style="font-size:22px;">
        🥳 May your year be as sweet and sparkly as you are!<br><br>
        With love and best wishes,<br>
        <b style="color:#d63384;">— Your Name 💫</b>
        </p>
    """, unsafe_allow_html=True)

# ---- Close Wrapper ----
st.markdown('</div>', unsafe_allow_html=True)
